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

print("\nDuplicate rows:")
print(df.duplicated().sum())

# Convert names to proper format
df["Name"] = df["Name"].str.title()


df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])


df["Stay Duration"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days


df = df[df["Billing Amount"] > 0]


print("\nCleaned Data Info:")
print(df.info())