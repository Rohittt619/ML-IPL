import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error

# -------------------------
# Load dataset
# -------------------------

df = pd.read_csv("data/processed/ipl_ml_dataset.csv")
print(df.shape)

# Use only data after 5 overs
df = df[df["overs"] >= 5]

print(df.shape)

# -------------------------
# Keep useful columns
# -------------------------

df = df[[
    "batting_team",
    "bowling_team",
    "current_score",
    "current_wickets",
    "overs",
    "current_run_rate",
    "runs_last_5",
    "wickets_last_5",
    "final_score"
]]

# -------------------------
# Features & Target
# -------------------------

X = df.drop("final_score", axis=1)
y = df["final_score"]

# -------------------------
# Categorical Columns
# -------------------------

categorical = [
    "batting_team",
    "bowling_team"
]

numeric = [
    "current_score",
    "current_wickets",
    "overs",
    "current_run_rate",
    "runs_last_5",
    "wickets_last_5"
]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
        ("num", "passthrough", numeric)
    ]
)

# -------------------------
# Train-Test Split
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(
       n_estimators=20,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)
}

best_model = None
best_mae = float("inf")

print("="*50)

for name, model in models.items():

    pipe = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    pipe.fit(X_train, y_train)

    pred = pipe.predict(X_test)

    mae = mean_absolute_error(y_test, pred)
    rmse = mean_squared_error(y_test, pred) ** 0.5

    print(f"{name}")
    print(f"MAE : {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print("-"*50)

    if mae < best_mae:
        best_mae = mae
        best_model = pipe

joblib.dump(best_model, "models/best_model.pkl")

print("Best model saved!")