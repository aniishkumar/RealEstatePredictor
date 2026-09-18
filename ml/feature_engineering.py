from sklearn.base import BaseEstimator, TransformerMixin


class HousingFeatures(BaseEstimator, TransformerMixin):
    """Create ratios without using the target, so inference can repeat the work safely."""

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        result = X.copy()
        result["bedroom_room_ratio"] = result["average_bedrooms"] / result["average_rooms"].clip(lower=0.1)
        result["people_per_room"] = result["average_occupancy"] / result["average_rooms"].clip(lower=0.1)
        return result
