import joblib
import pandas as pd

model = joblib.load("models/churn_model.pkl")

def predict_churn(input_data):
    data = pd.DataFrame([input_data])
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return {
        "prediction": int(prediction),
        "churn_probability": round(float(probability), 4)
    }