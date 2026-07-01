import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Data
# -----------------------------
matches = pd.read_csv("data/processed/matches_cleaned.csv")
deliveries = pd.read_csv("data/processed/deliveries_cleaned.csv")

# Create output folder
os.makedirs("outputs/figures", exist_ok=True)

plt.style.use("ggplot")

# -----------------------------
# 1. Matches per Season
# -----------------------------
season_matches = matches["season"].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(season_matches.index,
         season_matches.values,
         marker="o",
         linewidth=2)

plt.title("Matches Played per Season")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.tight_layout()
plt.savefig("outputs/figures/matches_per_season.png")
plt.close()

print("Saved -> matches_per_season.png")


# -----------------------------
# 2. Runs Scored Per Season
# -----------------------------

season_runs = deliveries.groupby("match_id")["total_runs"].sum().reset_index()

season_runs = season_runs.merge(
    matches[["id", "season"]],
    left_on="match_id",
    right_on="id"
)

season_runs = season_runs.groupby("season")["total_runs"].sum()

plt.figure(figsize=(10,5))

plt.bar(
    season_runs.index.astype(str),
    season_runs.values,
    color="royalblue"
)

plt.title("Total Runs Scored Per Season")
plt.xlabel("Season")
plt.ylabel("Runs")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/figures/runs_per_season.png")

plt.close()

print("Saved -> runs_per_season.png")


# -----------------------------
# 3. Toss Decision Analysis
# -----------------------------

plt.figure(figsize=(6,6))

matches["toss_decision"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.ylabel("")

plt.title("Toss Decision Distribution")

plt.tight_layout()

plt.savefig("outputs/figures/toss_decision.png")

plt.close()

print("Saved -> toss_decision.png")

# -----------------------------
# 4. Top Venues
# -----------------------------

venue_counts = matches["venue"].value_counts().head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=venue_counts.values,
    y=venue_counts.index,
    palette="viridis"
)

plt.title("Top 10 IPL Venues by Matches")

plt.xlabel("Matches")

plt.ylabel("Venue")

plt.tight_layout()

plt.savefig("outputs/figures/top_venues.png")

plt.close()

print("Saved -> top_venues.png")


# -----------------------------
# 5. Top Teams by Wins
# -----------------------------

team_wins = matches["winner"].value_counts().head(10)

plt.figure(figsize=(10,6))

sns.barplot(
    x=team_wins.values,
    y=team_wins.index,
    palette="rocket"
)

plt.title("Top 10 IPL Teams by Match Wins")

plt.xlabel("Wins")

plt.ylabel("Team")

plt.tight_layout()

plt.savefig("outputs/figures/top_teams.png")

plt.close()

print("Saved -> top_teams.png")

# -----------------------------
# 6. First Innings Score Distribution
# -----------------------------

first_innings = deliveries[deliveries["inning"] == 1]

first_scores = (
    first_innings.groupby("match_id")["total_runs"]
    .sum()
)

plt.figure(figsize=(10,5))

sns.histplot(
    first_scores,
    bins=25,
    kde=True,
    color="dodgerblue"
)

plt.title("Distribution of First Innings Scores")

plt.xlabel("Runs")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("outputs/figures/score_distribution.png")

plt.close()

print("Saved -> score_distribution.png")


# -----------------------------
# 7. Correlation Heatmap
# -----------------------------

numeric = deliveries[
    [
        "ball",
        "total_runs",
        "extra_runs",
        "batsman_runs"
    ]
]

plt.figure(figsize=(8,6))

sns.heatmap(
    numeric.corr(),
    annot=True,
    cmap="Blues",
    linewidths=0.5
)

plt.title("Feature Correlation Heatmap")

plt.tight_layout()

plt.savefig("outputs/figures/correlation_heatmap.png")

plt.close()

print("Saved -> correlation_heatmap.png")


# -----------------------------
# 8. Highest Team Scores
# -----------------------------

team_scores = (
    deliveries.groupby(
        [
            "match_id",
            "inning",
            "batting_team"
        ]
    )["total_runs"]
    .sum()
    .reset_index()
)

top_scores = team_scores.sort_values(
    "total_runs",
    ascending=False
).head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x="total_runs",
    y="batting_team",
    data=top_scores,
    palette="crest"
)

plt.title("Highest IPL Team Scores")

plt.xlabel("Runs")

plt.ylabel("Batting Team")

plt.tight_layout()

plt.savefig("outputs/figures/highest_team_scores.png")

plt.close()

print("Saved -> highest_team_scores.png")