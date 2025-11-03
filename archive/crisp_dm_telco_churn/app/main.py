"""FastAPI microservice scaffold for the Telco churn model."""
from pathlib import Path
from typing import List

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from joblib import load

APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR / "artifacts" / "telco_churn_pipeline.joblib"

app = FastAPI(title="Telco Churn Scoring API", version="0.1.0")


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model artifact missing. Run the notebook to train and export the pipeline "
            "to app/artifacts/telco_churn_pipeline.joblib."
        )
    return load(MODEL_PATH)


class ChurnFeatures(BaseModel):
    gender: str = Field(..., description="Customer gender")
    SeniorCitizen: int = Field(..., ge=0, le=1)
    Partner: str
    Dependents: str
    tenure: float = Field(..., ge=0)
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float = Field(..., ge=0)
    TotalCharges: float = Field(..., ge=0)


class ChurnPrediction(BaseModel):
    churn_probability: float
    churn_risk: str


@app.post("/score", response_model=ChurnPrediction)
def score_churn(payload: ChurnFeatures):
    try:
        model = load_model()
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    df = pd.DataFrame([payload.dict()])
    proba = model.predict_proba(df)[0, 1]
    risk = "high" if proba >= 0.6 else "medium" if proba >= 0.4 else "low"
    return ChurnPrediction(churn_probability=float(proba), churn_risk=risk)


@app.get("/healthz")
def healthcheck():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
