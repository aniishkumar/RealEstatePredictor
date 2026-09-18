# Dataset
`ml/train.py` downloads scikit-learn's California Housing data (20,640 rows) and writes the exact training copy to `data/processed/california_housing.csv`. Features are census-block aggregates: income, age, room/bedroom averages, population, occupancy, latitude and longitude. Target `MedHouseVal` becomes USD by multiplying its documented $100k units by 100,000. EDA checks types, nulls, duplicates and distributions in `notebooks/exploration.ipynb`.

**Risk:** a census-block aggregate is not an individual listing. Do not claim broad real-time appraisal accuracy.
