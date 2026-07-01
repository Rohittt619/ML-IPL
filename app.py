import streamlit as st
import pandas as pd
import joblib

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="IPL Score Predictor",
    page_icon="🏏",
    layout="wide"
)

# ---------------------------
# Load Model
# ---------------------------
model = joblib.load("models/best_model.pkl")

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("🏏 IPL Score Predictor")

st.sidebar.markdown("---")

st.sidebar.info("""
### Machine Learning Project

Predict the final first innings score of an IPL match.

### Algorithms Used
- Linear Regression
- Decision Tree
- Random Forest

### Tech Stack
- Python
- Pandas
- Scikit-Learn
- Streamlit
""")

st.sidebar.markdown("---")
st.sidebar.success("👨‍💻 Developed by Rohit Rathod")

# ---------------------------
# Title
# ---------------------------
st.markdown("""
# 🏏 IPL First Innings Score Predictor

### Predict the Final First Innings Score using Machine Learning

---
""")

# ---------------------------
# Teams
# ---------------------------
teams = [
    "Mumbai Indians",
    "Chennai Super Kings",
    "Royal Challengers Bangalore",
    "Kolkata Knight Riders",
    "Delhi Daredevils",
    "Kings XI Punjab",
    "Rajasthan Royals",
    "Sunrisers Hyderabad",
    "Deccan Chargers",
    "Pune Warriors",
    "Rising Pune Supergiant",
    "Gujarat Lions"
]

# ---------------------------
# Team Selection
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox(
        "🏏 Batting Team",
        teams
    )

with col2:
    bowling_team = st.selectbox(
        "🎯 Bowling Team",
        teams
    )

# ---------------------------
# Match Inputs
# ---------------------------
left, right = st.columns(2)

with left:

    current_score = st.number_input(
        "Current Score",
        min_value=0,
        value=100
    )

    current_wickets = st.slider(
        "Current Wickets",
        0,
        10,
        2
    )

with right:

    overs = st.slider(
        "Overs Completed",
        5.0,
        20.0,
        10.0,
        0.1
    )

    runs_last_5 = st.number_input(
        "Runs in Last 5 Overs",
        min_value=0,
        value=45
    )

wickets_last_5 = st.slider(
    "Wickets in Last 5 Overs",
    0,
    5,
    1
)

# ---------------------------
# Calculate Run Rate
# ---------------------------
current_run_rate = current_score / overs

# ---------------------------
# Predict Button
# ---------------------------
predict = st.button(
    "🚀 Predict Score",
    use_container_width=True
)

if predict:

    if batting_team == bowling_team:
        st.error("❌ Batting Team and Bowling Team cannot be the same.")
        st.stop()

    sample = pd.DataFrame({

        "batting_team": [batting_team],
        "bowling_team": [bowling_team],
        "current_score": [current_score],
        "current_wickets": [current_wickets],
        "overs": [overs],
        "current_run_rate": [current_run_rate],
        "runs_last_5": [runs_last_5],
        "wickets_last_5": [wickets_last_5]

    })

    prediction = int(model.predict(sample)[0])

    low = prediction - 5
    high = prediction + 5

    if prediction >= 190:
        pitch = "🟢 High Scoring Pitch"
        message = "Excellent batting conditions. Expect a very high-scoring game."

    elif prediction >= 170:
        pitch = "🟡 Balanced Pitch"
        message = "A competitive total. Both teams have a fair chance."

    else:
        pitch = "🔴 Bowling Friendly Pitch"
        message = "Bowlers are likely to dominate this match."

    st.markdown("---")

    st.markdown(
        f"""
        <div style="
        background-color:#1E293B;
        padding:30px;
        border-radius:15px;
        text-align:center;
        ">

        <h2 style="color:white;">
        🏏 Predicted First Innings Score
        </h2>

        <h1 style="
        color:#00FF99;
        font-size:60px;
        ">
        {low} - {high}
        </h1>

        <h3 style="color:white;">
        {pitch}
        </h3>

        <p style="
        color:#D1D5DB;
        font-size:18px;
        ">
        {message}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

st.caption(
    "Made with ❤️ using Python • Scikit-Learn • Streamlit | © Rohit Rathod"
)