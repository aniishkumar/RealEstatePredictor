from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT_DIR / "models" / "real_estate_price_pipeline.joblib"
METADATA_PATH = ROOT_DIR / "models" / "model_metadata.json"
MODEL_VERSION = "1.0.0"
CURRENCY = "USD"
