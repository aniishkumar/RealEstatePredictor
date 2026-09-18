# Feature engineering
`HousingFeatures` creates `bedroom_room_ratio` and `people_per_room`. Ratios express density/household composition that raw averages may obscure. It is a scikit-learn transformer with `fit` and `transform`, so the same calculation occurs in training and API prediction. It uses no target; deriving price-per-room from price would be leakage.
