# Interview cheat sheet

| Topic | Concise answer |
|---|---|
| Architecture | React controlled form → FastAPI/Pydantic → cached joblib pipeline → JSON response. |
| Dataset | 20,640 California Housing census-block rows; aggregate, California-only, not appraisals. |
| Features | 8 raw numeric fields plus two target-safe ratios. |
| Preprocessing | Train-fitted median imputation and scaling in a saved `ColumnTransformer` pipeline. |
| Models | Linear baseline, Random Forest bagging, Histogram Gradient Boosting. |
| Metrics | MAE average dollar miss; RMSE weights large misses; R² vs mean baseline—not accuracy. |
| Leakage | Never learn transforms or choices from held-out test data; never derive feature from target. |
| Pipeline | Guarantees training and inference transformations match. |
| Joblib | Persists fitted transformations and estimator; API loads once, never retrains per request. |
| FastAPI/Pydantic | Typed REST endpoints and boundary validation; invalid fields receive 422. |
| POST/JSON | Browser sends structured feature body; API returns typed prediction object. |
| React state | Inputs, busy, error, and result are state; inputs are controlled. |
| Testing | Health, model loading, valid response contract, invalid request. |
| Scale | Stateless replicas behind load balancer; versioned artifacts, monitoring and rate limits. |
| Monitoring | latency/errors, input drift, delayed ground-truth error, model version. |
