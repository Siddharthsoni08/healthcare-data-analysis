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


# Remove duplicates
df = df.drop_duplicates()

print("\nAfter removing duplicates:", df.shape)

# Convert names to proper format
df["Name"] = df["Name"].str.title()


df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])


df["Stay Duration"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days


df = df[df["Billing Amount"] > 0]


print("\nCleaned Data Info:")
print(df.info())


import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# -------------------------------
# 1. Gender Distribution
# -------------------------------
print("\nGender Count:")
print(df["Gender"].value_counts())


# -------------------------------
# 2. Disease Distribution
# -------------------------------
print("\nMedical Condition Count:")
print(df["Medical Condition"].value_counts())


# -------------------------------
# 3. Admission Type Distribution
# -------------------------------
print("\nAdmission Type Count:")
print(df["Admission Type"].value_counts())


# -------------------------------
# GRAPHS
# -------------------------------

# Gender Plot
sns.countplot(x="Gender", data=df)
plt.title("Gender Distribution")
plt.savefig("../images/gender_distribution.png")
plt.show()


# Disease Plot
sns.countplot(y="Medical Condition", data=df)
plt.title("Disease Distribution")
plt.savefig("../images/disease_distribution.png")
plt.show()


# Admission Type Plot
sns.countplot(x="Admission Type", data=df)
plt.title("Admission Type Distribution")
plt.savefig("../images/admission_type.png")
plt.show()


# Age Distribution
sns.histplot(df["Age"], bins=20)
plt.title("Age Distribution")
plt.savefig("../images/age_distribution.png")
plt.show()

# Age vs Disease
plt.figure(figsize=(10,6))
sns.boxplot(x="Medical Condition", y="Age", data=df)
plt.title("Age vs Disease")
plt.xticks(rotation=45)
plt.savefig("../images/age_vs_disease.png")
plt.show()


plt.figure(figsize=(8,6))
sns.scatterplot(x="Stay Duration", y="Billing Amount", data=df)
plt.title("Cost vs Stay Duration")
plt.savefig("../images/cost_vs_stay.png")
plt.show()


high_risk = df[(df["Age"] > 60) & (df["Stay Duration"] > 10)]

print("\nHigh Risk Patients Count:")
print(high_risk.shape[0])


costly_disease = df.groupby("Medical Condition")["Billing Amount"].mean().sort_values(ascending=False)

print("\nTop Costly Diseases:")
print(costly_disease)


