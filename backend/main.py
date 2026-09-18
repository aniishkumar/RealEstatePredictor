import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.config import CURRENCY, MODEL_VERSION
from backend.predictor import ModelUnavailableError, load_metadata, predict
from backend.schemas import PredictionResponse, PropertyInput

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="EstateValue API", version=MODEL_VERSION)
app.add_middleware(
    CORSMiddleware,
    # Vite may expose its development server under either hostname on Windows.
    # Both are explicit development origins; production origins should come from config.
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {"service": "EstateValue API", "docs": "/docs"}


@app.get("/health")
def health() -> dict[str, str]:
    try:
        load_metadata()
    except ModelUnavailableError as error:
        raise HTTPException(status_code=503, detail=str(error)) from error
    return {"status": "healthy"}


@app.get("/model-info")
def model_info() -> dict:
    try:
        return load_metadata()
    except ModelUnavailableError as error:
        raise HTTPException(status_code=503, detail=str(error)) from error


@app.post("/predict", response_model=PredictionResponse)
def create_prediction(payload: PropertyInput) -> PredictionResponse:
    try:
        metadata = load_metadata()
        value = predict(payload.model_dump())
    except ModelUnavailableError as error:
        logger.error("Prediction requested without a model artifact")
        raise HTTPException(status_code=503, detail="Prediction service is not ready.") from error
    except Exception as error:  # Keep implementation details out of the client response.
        logger.exception("Prediction failed")
        raise HTTPException(status_code=500, detail="Unable to generate a prediction right now.") from error
    return PredictionResponse(
        predicted_price=round(max(value, 0), 2), currency=CURRENCY,
        model_version=metadata["version"], model_name=metadata["model_name"],
        disclaimer="This is a machine-learning estimate, not a certified property valuation.",
    )
