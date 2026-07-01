# 🏏 IPL First Innings Score Prediction

> Predicting the final first innings score of an IPL match using Machine Learning — given live match conditions.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

## 📌 Problem Statement
Given batting team, bowling team, venue, current score, overs played, and wickets fallen — predict the final first innings total. Real-world use: live match score projections.

## 🛠️ Tech Stack
Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn · Jupyter Notebook

## 📊 Dataset
`IPL_First_Inning_Data.csv` — historical IPL match data (2008–2019)
Features: batting_team, bowling_team, venue, runs, wickets, overs, runs_last_5, wickets_last_5

## 🔍 Key Steps
1. **EDA** — score distributions, team-wise averages, venue impact analysis
2. **Feature engineering** — current run rate, wickets remaining, runs in last 5 overs
3. **Preprocessing** — OneHotEncoding for teams/venues, train-test split (80/20)
4. **Model training** — Linear Regression baseline → Random Forest for improvement
5. **Evaluation** — MAE and RMSE comparison across models

## 📈 Model Results
| Model | MAE | RMSE |
|---|---|---|
| Linear Regression | ~12 runs | ~16 runs |
| Random Forest | **~8 runs** | **~11 runs** |

Random Forest outperformed baseline by 33% on MAE.

## 🔑 Key Findings
- Venue significantly impacts scoring — DY Patil Stadium averages 20+ runs more than Chepauk
- Current run rate + wickets remaining are the two strongest predictors
- Teams batting first at home venues score ~15 runs higher on average

## 🚀 How to Run
```bash
git clone https://github.com/Rohittt619/ML-IPL
cd ML-IPL
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
jupyter notebook "IPL First Innings Score Prediction.ipynb"
```

## 📁 Files
| File | Description |
|---|---|
| `IPL First Innings Score Prediction.ipynb` | Main analysis notebook |
| `IPL_First_Inning_Data.csv` | Raw dataset |
| `requirements.txt` | Python dependencies |

## 👨‍💻 Author
**Rohit Rathod** · [LinkedIn](https://linkedin.com/in/rohit-rathod-19442a228) · [GitHub](https://github.com/Rohittt619)