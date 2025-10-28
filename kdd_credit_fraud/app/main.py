"""FastAPI service scaffold for credit card fraud detection."""
from pathlib import Path
from typing import Dict

import pandas as pd
from fastapi import FastAPI, HTTPException
from joblib import load
from pydantic import BaseModel, Field, validator

APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR / "artifacts" / "credit_fraud_model.joblib"
FEATURE_PATH = APP_DIR / "artifacts" / "feature_order.joblib"

app = FastAPI(title="Credit Card Fraud Scoring API", version="0.1.0")


def load_model_and_features():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Missing credit_fraud_model.joblib artifact. Train and export before serving.")
    if not FEATURE_PATH.exists():
        raise FileNotFoundError("Missing feature_order.joblib artifact. Export feature order with the model.")
    model = load(MODEL_PATH)
    feature_order = load(FEATURE_PATH)
    return model, feature_order


class TransactionPayload(BaseModel):
    features: Dict[str, float] = Field(..., description="Mapping of feature name to numeric value")

    @validator("features")
    def validate_non_empty(cls, value: Dict[str, float]):
        if not value:
            raise ValueError("Expected at least one feature value")
        return value


class FraudPrediction(BaseModel):
    fraud_probability: float
    risk_band: str


@app.post("/score", response_model=FraudPrediction)
def score_transaction(payload: TransactionPayload):
    try:
        model, feature_order = load_model_and_features()
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    missing = [feat for feat in feature_order if feat not in payload.features]
    if missing:
        raise HTTPException(status_code=400, detail={"missing_features": missing})

    df = pd.DataFrame([[payload.features[feat] for feat in feature_order]], columns=feature_order)
    proba = model.predict_proba(df)[0, 1]
    band = "critical" if proba >= 0.8 else "high" if proba >= 0.5 else "medium" if proba >= 0.2 else "low"
    return FraudPrediction(fraud_probability=float(proba), risk_band=band)


@app.get("/healthz")
def healthcheck():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
