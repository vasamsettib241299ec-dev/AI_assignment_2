from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

MODEL_FILE = Path("student_grade_model.joblib")

st.set_page_config(page_title="Student Grade Predictor", page_icon="📘")
st.title("Student Final-Grade Predictor")
st.write("Enter a student's details to estimate the final grade (G3) out of 20.")
st.caption("This educational demo uses the UCI Student Performance dataset. Predictions are estimates, not guarantees.")

if not MODEL_FILE.exists():
    st.error("Saved model not found. Run Part_D_Machine_Learning.ipynb through Problem 14 first.")
    st.stop()

try:
    saved = joblib.load(MODEL_FILE)
    with st.form("prediction_form"):
        studytime = st.selectbox("Weekly study time", options=[1, 2, 3, 4], format_func=lambda x: {
            1: "1 — less than 2 hours", 2: "2 — 2 to 5 hours",
            3: "3 — 5 to 10 hours", 4: "4 — more than 10 hours"
        }[x])
        failures = st.number_input("Past class failures", min_value=0, max_value=10, value=0, step=1)
        absences = st.number_input("Number of absences", min_value=0, max_value=100, value=2, step=1)
        G1 = st.number_input("First-period grade (G1)", min_value=0.0, max_value=20.0, value=12.0, step=0.5)
        G2 = st.number_input("Second-period grade (G2)", min_value=0.0, max_value=20.0, value=14.0, step=0.5)
        submitted = st.form_submit_button("Predict final grade")

    if submitted:
        values = pd.DataFrame([{
            "studytime": studytime, "failures": failures,
            "absences": absences, "G1": G1, "G2": G2
        }])[saved["features"]]
        prediction = float(saved["model"].predict(values)[0])
        prediction = max(0.0, min(20.0, prediction))
        st.metric("Estimated final grade (G3)", f"{prediction:.2f} / 20")
        if prediction >= 10:
            st.success("The estimate is in the passing range (10 or above).")
        else:
            st.warning("The estimate is below 10. This is only a model estimate.")
except (OSError, ValueError, KeyError) as error:
    st.error(f"Could not load or use the saved model: {error}")

with st.expander("Limitations"):
    st.write("The model is trained on a limited public dataset and uses only five input features. Real outcomes depend on many factors. The result should not be used for decisions about an actual student's future.")
