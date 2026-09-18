"""Print measured artifacts produced by ml.train; never contains copied metric claims."""
import json
from backend.config import ROOT_DIR

if __name__ == "__main__":
    print((ROOT_DIR / "models" / "model_metrics.json").read_text(encoding="utf-8"))
