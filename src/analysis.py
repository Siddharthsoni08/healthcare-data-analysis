import pandas as pd

# Load dataset
df = pd.read_csv("../data/healthcare.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Shape
print("\nShape of dataset:")
print(df.shape)

# Info
print("\nDataset info:")
print(df.info())

# Describe
print("\nStatistical summary:")
print(df.describe())