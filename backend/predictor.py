import json
from functools import lru_cache
from typing import Any

import joblib
import pandas as pd

from backend.config import METADATA_PATH, MODEL_PATH


class ModelUnavailableError(RuntimeError):
    pass


@lru_cache
def load_pipeline() -> Any:
    """Load once per process; retraining is never part of a request path."""
    if not MODEL_PATH.exists():
        raise ModelUnavailableError("Model artifact is missing. Run `python -m ml.train` first.")
    return joblib.load(MODEL_PATH)


@lru_cache
def load_metadata() -> dict[str, Any]:
    if not METADATA_PATH.exists():
        raise ModelUnavailableError("Model metadata is missing. Run training first.")
    return json.loads(METADATA_PATH.read_text(encoding="utf-8"))


def predict(features: dict[str, float]) -> float:
    frame = pd.DataFrame([features])
    # Target is stored by the source in units of $100,000; training converts it to USD.
    return float(load_pipeline().predict(frame)[0])
