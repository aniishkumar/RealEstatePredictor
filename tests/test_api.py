import pytest
from fastapi.testclient import TestClient

from backend.main import app
from backend.predictor import load_metadata, load_pipeline

client = TestClient(app)
VALID_PAYLOAD = {"median_income": 3.87, "house_age": 28, "average_rooms": 5.43,
                 "average_bedrooms": 1.1, "population": 1425, "average_occupancy": 3.07,
                 "latitude": 34.21, "longitude": -118.45}


@pytest.fixture(autouse=True)
def require_trained_artifact():
    try:
        load_pipeline()
        load_metadata()
    except Exception:
        pytest.skip("Run `python -m ml.train` before API integration tests.")


def test_health_is_healthy():
    assert client.get("/health").json() == {"status": "healthy"}


def test_prediction_has_contract():
    response = client.post("/predict", json=VALID_PAYLOAD)
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["predicted_price"], float)
    assert body["predicted_price"] >= 0
    assert body["currency"] == "USD"


def test_invalid_area_equivalent_is_rejected():
    response = client.post("/predict", json={**VALID_PAYLOAD, "median_income": -1})
    assert response.status_code == 422
