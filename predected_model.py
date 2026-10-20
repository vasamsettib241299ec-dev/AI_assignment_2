from pathlib import Path
import joblib
import pandas as pd

MODEL_FILE = Path("student_grade_model.joblib")

def predict_final_grade(studytime, failures, absences, G1, G2):
    if not MODEL_FILE.exists():
        raise FileNotFoundError(
            "Model not found. Run Part_D_Machine_Learning.ipynb through Problem 14 first."
        )
    saved = joblib.load(MODEL_FILE)
    values = {
        "studytime": studytime,
        "failures": failures,
        "absences": absences,
        "G1": G1,
        "G2": G2
    }
    input_data = pd.DataFrame([values])[saved["features"]]
    prediction = float(saved["model"].predict(input_data)[0])
    return max(0.0, min(20.0, prediction))

if __name__ == "__main__":
    print("Student final-grade prediction (G3, from 0 to 20)")
    try:
        studytime = int(input("Study time (1–4): "))
        failures = int(input("Past class failures (0 or more): "))
        absences = int(input("Number of absences (0 or more): "))
        G1 = float(input("First-period grade G1 (0–20): "))
        G2 = float(input("Second-period grade G2 (0–20): "))
        if studytime not in range(1, 5):
            raise ValueError("Study time must be between 1 and 4.")
        if failures < 0 or absences < 0:
            raise ValueError("Failures and absences cannot be negative.")
        if not 0 <= G1 <= 20 or not 0 <= G2 <= 20:
            raise ValueError("G1 and G2 must be between 0 and 20.")
        result = predict_final_grade(studytime, failures, absences, G1, G2)
        print(f"Predicted final grade: {result:.2f} / 20")
        print("This is an estimate from a small public dataset, not an official grade.")
    except ValueError as error:
        print("Invalid input:", error)
    except FileNotFoundError as error:
        print(error)
