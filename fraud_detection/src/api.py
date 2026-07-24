import joblib
import os
import numpy as np
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI(title="Fraud Detection API", version="1.0.0")
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "fraud_model.joblib")
model = None


class Transaction(BaseModel):
    amount: float
    hour: int
    distance_km: float
    prev_failures: int
    is_international: int


class Prediction(BaseModel):
    is_fraud: bool
    probability: float


@app.on_event("startup")
def load():
    global model
    try:
        model = joblib.load(model_path)
    except FileNotFoundError:
        model = None


@app.get("/health")
def health():
    return {"status": "healthy" if model else "unhealthy"}


@app.post("/predict", response_model=Prediction)
def predict(tx: Transaction):
    features = np.array([[tx.amount, tx.hour, tx.distance_km, tx.prev_failures, tx.is_international]])
    proba = model.predict_proba(features)[0, 1]
    return Prediction(is_fraud=bool(proba > 0.5), probability=round(proba, 4))
