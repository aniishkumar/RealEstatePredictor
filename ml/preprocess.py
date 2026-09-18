from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from ml.feature_engineering import HousingFeatures

RAW_FEATURES = [
    "median_income", "house_age", "average_rooms", "average_bedrooms",
    "population", "average_occupancy", "latitude", "longitude",
]
ENGINEERED_FEATURES = RAW_FEATURES + ["bedroom_room_ratio", "people_per_room"]


def build_preprocessor() -> Pipeline:
    # Median imputation is robust to the skewed household-related fields in this dataset.
    numeric = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
    columns = ColumnTransformer([("numeric", numeric, ENGINEERED_FEATURES)], remainder="drop")
    return Pipeline([("features", HousingFeatures()), ("columns", columns)])
