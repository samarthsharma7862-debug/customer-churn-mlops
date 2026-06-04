# Customer Churn Prediction MLOps Platform

## Overview

An End-to-End MLOps platform for predicting customer churn using Machine Learning and modern deployment practices.

## Features

- Customer Churn Prediction using XGBoost
- Data Preprocessing Pipeline
- MLflow Experiment Tracking
- FastAPI REST API
- Streamlit Interactive Dashboard
- Docker Containerization
- GitHub Version Control
- Production-Ready MLOps Workflow

## Tech Stack

- Python
- XGBoost
- Pandas
- Scikit-Learn
- MLflow
- FastAPI
- Streamlit
- Docker
- Git

## Project Structure

```text
customer-churn-mlops/
ÃÄÄ api/
ÃÄÄ app/
ÃÄÄ data/
ÃÄÄ src/
ÃÄÄ Dockerfile
ÃÄÄ docker-compose.yml
ÃÄÄ requirements.txt
ÀÄÄ README.md
```

## Running Locally

```bash
pip install -r requirements.txt
python src/train_model.py
uvicorn api.main:app --reload
streamlit run app/streamlit_app.py
```

## Docker Deployment

```bash
docker build -t churn-mlops .
docker run -p 8501:8501 churn-mlops
```

## API Endpoint

POST /predict

Example Response:

```json
{
  "prediction": 0,
  "churn_probability": 0.4939
}
```

## Author

Samarth Sharma
