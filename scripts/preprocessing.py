import pandas as pd
import numpy as np
import os

# -----------------------------
# Load datasets
# -----------------------------
matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

print("=" * 60)
print("MATCHES DATASET")
print("=" * 60)
print(matches.head())

print("\nShape:", matches.shape)

print("\nMissing Values")
print(matches.isnull().sum())

print("\n" + "=" * 60)
print("DELIVERIES DATASET")
print("=" * 60)
print(deliveries.head())

print("\nShape:", deliveries.shape)

print("\nMissing Values")
print(deliveries.isnull().sum())

# -----------------------------
# Remove duplicate rows
# -----------------------------
matches.drop_duplicates(inplace=True)
deliveries.drop_duplicates(inplace=True)

# -----------------------------
# Fill missing values
# -----------------------------
matches.fillna("Unknown", inplace=True)

# -----------------------------
# Create output folder
# -----------------------------
os.makedirs("data/processed", exist_ok=True)

# -----------------------------
# Save cleaned datasets
# -----------------------------
matches.to_csv("data/processed/matches_cleaned.csv", index=False)
deliveries.to_csv("data/processed/deliveries_cleaned.csv", index=False)

print("\n✅ Cleaned datasets saved successfully!")