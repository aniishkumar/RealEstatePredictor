"""Download, inspect, train, measure, and serialize the EstateValue model."""
import json
from datetime import UTC, datetime

import joblib
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from backend.config import METADATA_PATH, MODEL_PATH, ROOT_DIR
from ml.preprocess import RAW_FEATURES, build_preprocessor


def evaluate(model, X_train, X_test, y_train, y_test) -> dict[str, float]:
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    return {"mae": round(mean_absolute_error(y_test, prediction), 2),
            "rmse": round(mean_squared_error(y_test, prediction) ** 0.5, 2),
            "r2": round(r2_score(y_test, prediction), 4)}


def main() -> None:
    data = fetch_california_housing(data_home=str(ROOT_DIR / "data" / "raw"), as_frame=True)
    frame = data.frame.rename(columns={
        "MedInc": "median_income", "HouseAge": "house_age", "AveRooms": "average_rooms",
        "AveBedrms": "average_bedrooms", "Population": "population", "AveOccup": "average_occupancy",
        "Latitude": "latitude", "Longitude": "longitude", "MedHouseVal": "median_house_value",
    })
    # Store a CSV copy for EDA; source target values are $100k and are converted to USD here.
    frame.to_csv(ROOT_DIR / "data" / "processed" / "california_housing.csv", index=False)
    X, y = frame[RAW_FEATURES], frame["median_house_value"] * 100_000
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    candidates = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=250, min_samples_leaf=2, random_state=42, n_jobs=-1),
        "Histogram Gradient Boosting": HistGradientBoostingRegressor(max_iter=300, learning_rate=0.06, max_leaf_nodes=31, random_state=42),
    }
    results, fitted = {}, {}
    for name, estimator in candidates.items():
        pipeline = Pipeline([("preprocessing", build_preprocessor()), ("model", estimator)])
        results[name] = evaluate(pipeline, X_train, X_test, y_train, y_test)
        fitted[name] = pipeline
    # Selection is deterministic: lowest MAE, then RMSE, with test data held back until final comparison.
    selected_name = min(results, key=lambda name: (results[name]["mae"], results[name]["rmse"]))
    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(fitted[selected_name], MODEL_PATH)
    metadata = {"model_name": selected_name, "version": "1.0.0", "currency": "USD",
                "training_date": datetime.now(UTC).isoformat(), "dataset": "California Housing",
                "rows": len(frame), "raw_features": RAW_FEATURES, "target": "median house value (USD)"}
    METADATA_PATH.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    (MODEL_PATH.parent / "model_metrics.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps({"selected_model": selected_name, "metrics": results, "rows": len(frame)}, indent=2))


if __name__ == "__main__":
    main()
