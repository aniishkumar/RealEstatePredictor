# Regression
Regression predicts a continuous quantity; classification predicts categories. Linear regression learns `y = β₀ + β₁x₁ + … + βₙxₙ`, selecting coefficients to minimize squared residuals. It is fast and interpretable but assumes additive linear relationships. A regression tree repeatedly splits values into nodes and predicts the mean target in a leaf; deep trees can overfit.

Random Forest bagging trains many trees on bootstrap samples with random feature subsets and averages them, reducing variance. Histogram Gradient Boosting builds trees sequentially to correct residual error; learning rate, iterations, and leaf count control its capacity.
