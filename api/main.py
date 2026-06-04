from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.abspath("."))

from src.predict import predict_churn

app = FastAPI(
    title="Customer Churn Prediction API",
    description="End-to-End MLOps API for predicting customer churn",
    version="1.0"
)

class CustomerData(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running"
    }

@app.post("/predict")
def predict(data: CustomerData):
    result = predict_churn(data.dict())
    return result