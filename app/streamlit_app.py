import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction MLOps Platform")
st.write("Enter customer details to predict churn probability.")

st.sidebar.header("Customer Information")

gender = st.sidebar.selectbox("Gender", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
SeniorCitizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
Partner = st.sidebar.selectbox("Partner", [0, 1])
Dependents = st.sidebar.selectbox("Dependents", [0, 1])
tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
PhoneService = st.sidebar.selectbox("Phone Service", [0, 1])
MultipleLines = st.sidebar.selectbox("Multiple Lines", [0, 1])
InternetService = st.sidebar.selectbox("Internet Service", [0, 1, 2])
OnlineSecurity = st.sidebar.selectbox("Online Security", [0, 1, 2])
OnlineBackup = st.sidebar.selectbox("Online Backup", [0, 1, 2])
DeviceProtection = st.sidebar.selectbox("Device Protection", [0, 1, 2])
TechSupport = st.sidebar.selectbox("Tech Support", [0, 1, 2])
StreamingTV = st.sidebar.selectbox("Streaming TV", [0, 1, 2])
StreamingMovies = st.sidebar.selectbox("Streaming Movies", [0, 1, 2])
Contract = st.sidebar.selectbox("Contract", [0, 1, 2])
PaperlessBilling = st.sidebar.selectbox("Paperless Billing", [0, 1])
PaymentMethod = st.sidebar.selectbox("Payment Method", [0, 1, 2, 3])
MonthlyCharges = st.sidebar.number_input("Monthly Charges", min_value=0.0, value=70.35)
TotalCharges = st.sidebar.number_input("Total Charges", min_value=0.0, value=845.50)

input_data = {
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}

if st.button("Predict Churn"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=input_data
    )

    if response.status_code == 200:
        result = response.json()

        probability = result["churn_probability"]
        prediction = result["prediction"]

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Churn Probability", f"{probability * 100:.2f}%")

        with col2:
            if prediction == 1:
                st.error("High Risk: Customer may churn")
            else:
                st.success("Low Risk: Customer likely to stay")

        st.subheader("Input Data")
        st.json(input_data)
    else:
        st.error("API is not running. Start FastAPI first.")