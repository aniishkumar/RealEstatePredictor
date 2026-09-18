# Preprocessing
`ml/preprocess.py` builds a `Pipeline`: feature creation, then `ColumnTransformer`, then a numerical sub-pipeline with median imputation and `StandardScaler`. The transformer routes selected columns to the appropriate treatment. Median is less sensitive than mean to skew/outliers. Scaling puts values on comparable ranges, helping linear regression; tree splits generally do not need scaling, but retaining one consistent pipeline makes experiments and serving safer.

Most important: `fit` happens on training rows only. Saving it with the estimator makes inference transformations identical and avoids leakage or hand-coded drift.
