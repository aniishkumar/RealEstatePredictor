from pydantic import BaseModel, Field, field_validator


class PropertyInput(BaseModel):
    """Features match the California Housing dataset's documented columns."""

    median_income: float = Field(..., gt=0, le=20, description="Median income in tens of thousands of USD")
    house_age: float = Field(..., ge=0, le=100)
    average_rooms: float = Field(..., gt=0, le=100)
    average_bedrooms: float = Field(..., gt=0, le=50)
    population: float = Field(..., ge=0, le=100000)
    average_occupancy: float = Field(..., gt=0, le=100)
    latitude: float = Field(..., ge=32, le=43)
    longitude: float = Field(..., ge=-125, le=-114)

    @field_validator("average_bedrooms")
    @classmethod
    def bedrooms_not_absurd(cls, value: float) -> float:
        if value <= 0:
            raise ValueError("average_bedrooms must be greater than zero")
        return value


class PredictionResponse(BaseModel):
    predicted_price: float = Field(..., description="Estimated median house value in USD")
    currency: str
    model_version: str
    model_name: str
    disclaimer: str
