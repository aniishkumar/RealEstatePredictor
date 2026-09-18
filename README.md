# EstateValue — Real Estate Price Prediction

EstateValue is a small, explainable full-stack machine-learning project. A React form sends California Housing characteristics to a FastAPI endpoint. The endpoint validates the JSON and uses one serialized scikit-learn pipeline to return an estimated median house value in USD.

> Status: source code is complete; model artifacts are intentionally generated locally by the reproducible training command. This prevents the repository from claiming unmeasured metrics or shipping a binary artifact whose provenance cannot be inspected.

## Architecture

`React form → POST /predict → Pydantic validation → joblib Pipeline → JSON response → React result panel`

The pipeline contains the feature transformer, median imputer, scaler, and selected model. The API never reimplements preprocessing.

## Dataset

Training downloads the [California Housing dataset](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset) via scikit-learn and saves an inspectable copy in `data/processed/`. It contains 20,640 census-block records. The target is `MedHouseVal`, which the source expresses in $100,000 units; this project converts it to USD before fitting.

Inputs: median income, house age, average rooms, average bedrooms, population, average occupancy, latitude, and longitude. The project does **not** claim a property-specific appraisal: these are census-block aggregate inputs and California-only training data.

## ML approach

`python -m ml.train` makes a reproducible 80/20 split (`random_state=42`), fits Linear Regression, Random Forest, and Histogram Gradient Boosting, and writes the measured MAE, RMSE, and R² into `models/model_metrics.json`. The selection rule is lowest held-out MAE, breaking ties with RMSE. The exact selected model and measured results are printed by training and stored alongside the model.

- **MAE:** average absolute dollar error.
- **RMSE:** square-root mean squared error; it penalizes larger misses more heavily.
- **R²:** improvement over predicting the test-set mean; it is not an accuracy percentage.

Feature engineering adds bedroom-to-room ratio and people-per-room ratio using inputs only. Median imputation and scaling happen inside a `ColumnTransformer` within the saved pipeline, fitted only on training data.

## Run locally

Prerequisite: Python 3.10+ and Node 20+.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m ml.train
pytest
uvicorn backend.main:app --reload
```

In another terminal:

```powershell
cd frontend
npm install
Copy-Item ..\.env.example .env
npm run dev
```

Open the Vite URL (normally `http://localhost:5173`). Set `VITE_API_URL` in `frontend/.env` if the API runs elsewhere.

## API

- `GET /health` — 200 only when model metadata is available; otherwise 503.
- `GET /model-info` — selected model, feature schema, source, and training date.
- `POST /predict` — validated raw feature values → estimated USD value.

Example request:

```json
{"median_income":3.87,"house_age":28,"average_rooms":5.43,"average_bedrooms":1.1,"population":1425,"average_occupancy":3.07,"latitude":34.21,"longitude":-118.45}
```

## Tests

`tests/test_api.py` covers health, a valid response contract, invalid numeric input, and artifact loading. It skips safely when no trained artifact exists; run training first for the integration checks.

## Limitations and next steps

This dataset is old, California-specific, geographically aggregated, and capped in its target distribution. It lacks property condition, lot size, school quality, and current market context. Production work would add current licensed data, monitor drift/error by geography, version artifacts in storage, authenticate/rate-limit the API, and use a prediction interval rather than a single point estimate.

## Project structure

- `ml/`: feature construction, preprocessing, training, evaluation.
- `backend/`: API request/response schemas and inference service.
- `frontend/`: React UI and dedicated API service.
- `docs/`: project-specific interview study notes.
- `notebooks/`: targeted EDA notebook.
