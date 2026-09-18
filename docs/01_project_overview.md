# Project overview
**What:** EstateValue estimates California census-block median home value. **Why:** it demonstrates a complete ML inference path without pretending to be a certified appraisal. **How here:** `frontend/src/App.jsx` collects controlled form state; `backend/main.py` validates and predicts with `models/real_estate_price_pipeline.joblib`. **Interview:** “I separated the UI, HTTP validation, and reusable ML code so each responsibility is testable.”

Checkpoint: draw `browser → API → saved pipeline → response` and explain why the model is loaded once per process.
