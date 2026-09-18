# EDA
EDA is a pre-model audit: shape, data types, missingness, duplicates, summary statistics, target histogram, and income/price scatter plot. The notebook uses the processed file so analysis matches training. A histogram identifies skew and target caps; scatter shows association, not causation. Check potential leakage by ensuring only input columns, never `median_house_value`, enter `X`.

Interview: “I use EDA to discover data quality and distribution issues before choosing transformations—not to generate decorative charts.”
