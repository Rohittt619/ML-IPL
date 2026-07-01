import pandas as pd

# -----------------------------
# Load datasets
# -----------------------------
matches = pd.read_csv("data/processed/matches_cleaned.csv")
deliveries = pd.read_csv("data/processed/deliveries_cleaned.csv")

# -----------------------------
# First innings only
# -----------------------------
df = deliveries[deliveries["inning"] == 1].copy()

# -----------------------------
# Wicket column
# -----------------------------
df["is_wicket"] = df["player_dismissed"].notna().astype(int)

# -----------------------------
# Current score
# -----------------------------
df["current_score"] = (
    df.groupby("match_id")["total_runs"]
      .cumsum()
)

# -----------------------------
# Current wickets
# -----------------------------
df["current_wickets"] = (
    df.groupby("match_id")["is_wicket"]
      .cumsum()
)

# -----------------------------
# Balls faced
# -----------------------------
df["balls"] = (
    df.groupby("match_id")
      .cumcount() + 1
)

# -----------------------------
# Overs completed
# -----------------------------
df["overs"] = df["balls"] / 6

# -----------------------------
# Current Run Rate
# -----------------------------
df["current_run_rate"] = (
    df["current_score"] / df["overs"]
)

# -----------------------------
# Runs in last 30 balls (5 overs)
# -----------------------------
df["runs_last_5"] = (
    df.groupby("match_id")["total_runs"]
      .rolling(30, min_periods=1)
      .sum()
      .reset_index(level=0, drop=True)
)

# -----------------------------
# Wickets in last 30 balls
# -----------------------------
df["wickets_last_5"] = (
    df.groupby("match_id")["is_wicket"]
      .rolling(30, min_periods=1)
      .sum()
      .reset_index(level=0, drop=True)
)

# -----------------------------
# Final score
# -----------------------------
final_score = (
    df.groupby("match_id")["total_runs"]
      .sum()
      .reset_index()
      .rename(columns={"total_runs":"final_score"})
)

df = df.merge(final_score,on="match_id")

# -----------------------------
# Save ML Dataset
# -----------------------------
df.to_csv(
    "data/processed/ipl_ml_dataset.csv",
    index=False
)

print("Dataset created successfully!")

print(df.head())