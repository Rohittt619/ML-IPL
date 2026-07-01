import joblib
import pandas as pd

model = joblib.load("models/best_model.pkl")

sample = pd.DataFrame({

    "batting_team":["Mumbai Indians"],

    "bowling_team":["Chennai Super Kings"],

    "current_score":[120],

    "current_wickets":[3],

    "overs":[15],

    "current_run_rate":[8.0],

    "runs_last_5":[48],

    "wickets_last_5":[1]

})

prediction = model.predict(sample)

print("="*40)
print(f"Predicted First Innings Score : {prediction[0]:.0f}")
print("="*40)