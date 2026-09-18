# Interview question bank

Use this as a prompt sheet. For every answer, tie back to the named project file rather than reciting definitions.

## Beginner (20)

1. **What problem does this solve?** Estimate a California census-block median home value; not a certified appraisal. *Test:* scope. *Example:* `README.md` limitations. *Avoid:* promising exact listing prices.
2. **What is a feature?** An input variable such as `median_income`. *Test:* ML vocabulary. *Example:* `RAW_FEATURES`. *Avoid:* calling the target a feature.
3. **What is the target?** USD-converted `median_house_value`. *Test:* dataset understanding. *Example:* `ml/train.py`. *Avoid:* forgetting source units.
4. **Regression vs classification?** Regression returns continuous values; classification returns labels. *Test:* task framing. *Example:* price versus property type. *Avoid:* calling price a class.
5. **Why split data?** To estimate unseen-data behavior. *Test:* generalization. *Example:* 80/20 split. *Avoid:* training and scoring same rows.
6. **What is an API?** Contract for browser/server communication. *Test:* web basics. *Example:* `/predict`. *Avoid:* confusing it with UI.
7. **Why FastAPI?** Typed request validation and automatic docs. *Test:* framework choice. *Example:* `PropertyInput`. *Avoid:* claiming it trains models.
8. **Why POST?** Input is structured JSON that creates a prediction request. *Test:* HTTP. *Example:* POST `/predict`. *Avoid:* putting all fields in URL.
9. **What is JSON?** Text format sent between React and FastAPI. *Test:* integration. *Example:* `JSON.stringify`. *Avoid:* calling it a database.
10. **What is Pydantic?** Runtime parser/validator for API schemas. *Test:* safety. *Example:* bounds in `schemas.py`. *Avoid:* manual string checks only.
11. **What is a pipeline?** Ordered transformations plus model. *Test:* reproducibility. *Example:* `Pipeline` in train. *Avoid:* separate API preprocessing.
12. **What is joblib?** Python object serialization used for fitted pipeline. *Test:* deployment. *Example:* `joblib.dump`. *Avoid:* retraining per request.
13. **What is MAE?** Average absolute dollar error. *Test:* evaluation. *Example:* `evaluate`. *Avoid:* calling it percentage accuracy.
14. **What is RMSE?** Root mean squared error, emphasizing large misses. *Test:* evaluation. *Example:* metrics artifact. *Avoid:* saying it is always better than MAE.
15. **What is R²?** Improvement over mean-target baseline. *Test:* metric literacy. *Example:* held-out result. *Avoid:* “accuracy percent.”
16. **What is overfitting?** Learning training quirks rather than patterns. *Test:* generalization. *Example:* unconstrained tree. *Avoid:* judging it on train score alone.
17. **What is a React component?** Reusable UI function. *Test:* frontend. *Example:* `PropertyForm`. *Avoid:* mixing API logic everywhere.
18. **What is controlled input?** React state is the input value. *Test:* forms. *Example:* `values` state. *Avoid:* relying only on DOM.
19. **What is CORS?** Browser policy controlling cross-origin requests. *Test:* web security. *Example:* middleware. *Avoid:* allowing every origin in production.
20. **What happens when API is down?** Service catches error and displays safe message. *Test:* resilience. *Example:* `api.js`. *Avoid:* exposing exception traces.

## Intermediate (25)

1. **Why median imputation?** More robust to skew/outliers than mean. *Test:* preprocessing. *Example:* `SimpleImputer`. *Avoid:* claiming source has nulls without inspection.
2. **Why scale?** It helps coefficient-based models compare feature magnitudes. *Test:* model mechanics. *Example:* `StandardScaler`. *Avoid:* saying trees require it.
3. **What does ColumnTransformer do?** Applies named transforms to named columns. *Test:* data routing. *Example:* numeric branch. *Avoid:* losing schema order.
4. **Why fit transforms on train only?** Test information would leak. *Test:* leakage. *Example:* pipeline fit. *Avoid:* `fit_transform` all rows.
5. **Why one pipeline?** Same learned transforms in inference. *Test:* serving consistency. *Example:* serialized artifact. *Avoid:* duplicate transformations.
6. **Why feature ratios?** They express composition/density using raw inputs. *Test:* feature engineering. *Example:* `HousingFeatures`. *Avoid:* target-derived ratios.
7. **Linear regression limits?** It may miss nonlinear interactions. *Test:* model choice. *Example:* candidate baseline. *Avoid:* calling it useless.
8. **How does a tree predict?** It follows splits to a leaf and returns a learned leaf value. *Test:* ML fundamentals. *Example:* RF base estimator. *Avoid:* saying it uses coefficients.
9. **How does random forest reduce variance?** Average decorrelated bootstrap trees. *Test:* ensemble. *Example:* `RandomForestRegressor`. *Avoid:* confusing bagging and boosting.
10. **How does gradient boosting work?** Sequential trees correct residual error. *Test:* ensembles. *Example:* `HistGradientBoostingRegressor`. *Avoid:* claiming parallel independent trees.
11. **What does learning rate do?** Shrinks each boosting step; tradeoff with iterations. *Test:* tuning. *Example:* `0.06`. *Avoid:* treating it as data sampling.
12. **Why not XGBoost?** Histogram Gradient Boosting is strong and avoids a non-core dependency. *Test:* tradeoff. *Example:* candidates. *Avoid:* pretending XGBoost ran.
13. **How choose final model?** Lowest held-out MAE, tie RMSE. *Test:* rigor. *Example:* `min(results…)`. *Avoid:* cherry-picking R².
14. **What is cross-validation?** Repeated splits to stabilize validation estimates. *Test:* evaluation. *Example:* next tuning step. *Avoid:* using test repeatedly.
15. **Validation vs test?** Validation tunes; test is final unbiased check. *Test:* experimental design. *Example:* current simple holdout. *Avoid:* tuning to test.
16. **Why fixed seed?** Reproducible split/model randomness. *Test:* reproducibility. *Example:* 42. *Avoid:* calling it accuracy improvement.
17. **Why load once?** Reduces latency and avoids repeated disk I/O. *Test:* performance. *Example:* `@lru_cache`. *Avoid:* shared mutable request data.
18. **Why DataFrame at inference?** Pipeline expects named columns. *Test:* schema. *Example:* `predictor.py`. *Avoid:* positional arrays.
19. **How model versioned?** Metadata version is saved with artifact. *Test:* operations. *Example:* JSON metadata. *Avoid:* duplicate hard-coded version.
20. **What does 422 mean?** Valid HTTP request but invalid schema content. *Test:* errors. *Example:* negative income. *Avoid:* returning 500.
21. **What does 503 mean here?** Model service cannot serve because artifact missing. *Test:* readiness. *Example:* `/health`. *Avoid:* confusing client validation.
22. **Why frontend env URL?** Different dev/prod endpoints without code edit. *Test:* deployment. *Example:* `VITE_API_URL`. *Avoid:* hard-coded production URL.
23. **How timeout handled?** AbortController ends slow request after 10s. *Test:* browser reliability. *Example:* `api.js`. *Avoid:* infinite spinner.
24. **How accessible errors?** Associated IDs and `role=alert`. *Test:* accessibility. *Example:* form. *Avoid:* color-only errors.
25. **Why no fancy dashboard?** A valuation workspace prioritizes auditability/readability. *Test:* product judgment. *Example:* CSS. *Avoid:* fake metrics.

## Advanced (25)

1. **Bias-variance tradeoff?** Simpler models may underfit; flexible trees may overfit. *Test:* theory. *Example:* compare held-out errors. *Avoid:* claiming one is always best.
2. **How detect drift?** Monitor input distributions and delayed error by cohort. *Test:* MLOps. *Example:* deployment notes. *Avoid:* only uptime metrics.
3. **Prediction interval?** Range around estimate, requiring uncertainty method/calibration. *Test:* uncertainty. *Example:* future work. *Avoid:* presenting point price as certainty.
4. **Target capping effect?** It can make upper-value predictions unreliable. *Test:* dataset limits. *Example:* EDA histogram. *Avoid:* extrapolating above support.
5. **Spatial leakage?** Nearby records/splits may inflate performance. *Test:* domain rigor. *Example:* future geographic split. *Avoid:* claiming iid is guaranteed.
6. **Why row random split is limited?** Geography/time may differ in deployment. *Test:* validation design. *Example:* improve with grouped split. *Avoid:* rejecting all random splits.
7. **Feature importance caveat?** Importance is association under model/data, not causality. *Test:* interpretability. *Example:* add permutation importance later. *Avoid:* causal claims.
8. **Permutation importance?** Performance loss after shuffling a feature. *Test:* explainability. *Example:* future evaluation. *Avoid:* ignoring correlated features.
9. **How prevent schema drift?** Validate Pydantic fields and store raw schema metadata. *Test:* contracts. *Example:* `raw_features`. *Avoid:* accept arbitrary fields silently.
10. **Joblib security risk?** Never load untrusted pickle/joblib artifacts. *Test:* secure ML. *Example:* trusted model path. *Avoid:* user-uploaded artifact.
11. **Thread safety?** Pipeline prediction is read-only after load; avoid mutating shared object. *Test:* concurrency. *Example:* cached pipeline. *Avoid:* retraining in endpoint.
12. **Batching tradeoff?** Improves throughput but may add latency. *Test:* serving. *Example:* separate batch endpoint. *Avoid:* batch every interactive request.
13. **Horizontal scale?** Replicate stateless APIs behind balancer. *Test:* system design. *Example:* deployment doc. *Avoid:* shared local state.
14. **Model registry?** Artifact/version/metrics lineage store. *Test:* governance. *Example:* metadata is minimal prototype. *Avoid:* overwrite without provenance.
15. **Can scaling harm trees?** Usually unnecessary, but monotonic scaling preserves tree splits. *Test:* nuance. *Example:* common pipeline. *Avoid:* saying it changes tree logic materially.
16. **Why RMSE plus MAE?** Together distinguish ordinary vs large misses. *Test:* metric choice. *Example:* artifact. *Avoid:* one metric only.
17. **Data leakage example?** Filling imputer on full dataset before split. *Test:* integrity. *Example:* pipeline avoids. *Avoid:* only target leakage examples.
18. **Feature store needed?** Not here; schema is small/static. *Test:* proportional engineering. *Example:* direct input. *Avoid:* needless infrastructure.
19. **Authentication plan?** Gateway/OAuth/API keys, least privilege. *Test:* security. *Example:* not implemented demo. *Avoid:* store keys frontend.
20. **Rate limiting?** Limit per identity/IP at edge/API. *Test:* abuse prevention. *Example:* production future. *Avoid:* rate limit by trusting client header.
21. **Observability?** Correlation IDs, structured logs, latency/errors/model version. *Test:* operations. *Example:* logging hook. *Avoid:* log sensitive input indiscriminately.
22. **Rollback?** Deploy prior immutable artifact/version. *Test:* release safety. *Example:* metadata version. *Avoid:* retrain under pressure.
23. **Why async endpoint?** This CPU-bound prediction does not require async; use workers/replicas for scale. *Test:* FastAPI nuance. *Example:* sync endpoint. *Avoid:* “async makes CPU fast.”
24. **Caching predictions?** Only if identical requests frequent; protect privacy and include model version. *Test:* tradeoffs. *Example:* future. *Avoid:* stale values silently.
25. **How test model changes?** Re-run train, preserve data/version, compare held-out metrics and API contract. *Test:* CI. *Example:* tests. *Avoid:* replace artifact unreviewed.

## Project-specific (30), ML (30), FastAPI/backend (25), React/frontend (20), System design (20), Debugging (20)

For these categories, practice the following project-grounded prompts. Answer each using the linked source, then state the tradeoff and a common mistake.

### Project-specific (30)
Why California Housing?; What are its 8 raw features?; Which two features are engineered?; Why convert target units?; Why USD UI?; Why California coordinate bounds?; Why `random_state=42`?; Why three candidate models?; What selection rule?; Where are metrics stored?; Where is version stored?; Why no hard-coded score?; What happens missing artifact?; What does health mean?; How API loads model?; Why cache?; How frontend sends data?; How errors render?; Why form values start as strings?; How numeric conversion works?; Why response model?; Why no feature-importance chart?; Why no deployment metrics?; Why disclaimer?; What notebook questions matter?; What target limitations?; Which files own concerns?; How reproduce run?; What exact test contract?; What would you demo?

### ML (30)
Define residual; explain least squares; explain intercept; explain coefficients; explain node/split/leaf; explain bootstrap; explain feature subsampling; bagging vs boosting; residual correction; learning rate; iterations; leaf nodes; underfit; overfit; regularization; train error; test error; holdout; CV; imputation; standardization; normalization; one-hot encoding; label encoding; feature leakage; target leakage; outlier; skew; correlation; causation.

### FastAPI/backend (25)
ASGI?; Uvicorn?; route?; GET vs POST?; request body?; response model?; Pydantic parsing?; 422?; 500?; 503?; CORS?; `lru_cache`?; DataFrame conversion?; exception logging?; safe error text?; model file path?; model startup strategy?; concurrent request behavior?; health check?; readiness vs liveness?; version endpoint?; config environment?; authentication plan?; rate limit plan?; HTTPS plan?

### React/frontend (20)
Component?; prop?; state?; controlled input?; `onChange`?; submit prevention?; `async/await`?; loading state?; error state?; conditional rendering?; fetch?; JSON parsing?; timeout?; environment variable?; form label?; focus style?; live region?; mobile layout?; why API service?; why no UI library?

### System design (20)
Current architecture?; statelessness?; load balancer?; replicas?; artifact store?; container?; health probes?; autoscaling?; logs?; metrics?; tracing?; queue use case?; caching?; CDN use case?; database need?; secrets manager?; CI/CD?; canary release?; rollback?; drift monitoring?

### Debugging/scenarios (20)
Model missing?; model corrupt?; 422 response?; 503 response?; CORS failure?; timeout?; wrong env URL?; frontend build fail?; mismatched schema?; NaN input?; artifact/model sklearn mismatch?; target units wrong?; training download fail?; bad coordinates?; memory high?; slow predictions?; different result after retraining?; tests skipped?; API docs mismatch?; UI result empty?

## Two-minute project defense

“I built EstateValue, a full-stack regression demo for California Housing data. I used eight documented census-block features and converted the source target from $100k units to USD. The training script creates a reproducible holdout split, applies target-safe ratio features and a scikit-learn preprocessing pipeline, then compares linear regression, random forest, and histogram gradient boosting with MAE, RMSE, and R². It saves the chosen complete pipeline with metadata. FastAPI validates raw JSON using Pydantic, loads the artifact once per process, predicts, and returns a typed response. A React controlled form calls that endpoint through one API service and handles loading, validation, network errors, and a clear disclaimer. I would emphasize that it is a California aggregate-data estimate, not a certified valuation.”

## 30-second version

“EstateValue is React plus FastAPI plus a serialized scikit-learn regression pipeline. It validates California Housing inputs, performs exactly the same preprocessing as training, and returns an estimated median value. I compared three models on a reproducible held-out split and store measured metrics, not claimed numbers.”

## Five-minute extension

After the two-minute explanation, walk through `ml/train.py`, `ml/preprocess.py`, `backend/schemas.py`, `backend/predictor.py`, `frontend/src/App.jsx`, and `tests/test_api.py`; explain a request lifecycle, model-selection metric tradeoff, limitations, then production scaling/monitoring plan.
