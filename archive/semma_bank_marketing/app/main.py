"""FastAPI scaffold for SEMMA bank marketing model."""
from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException
from joblib import load
from pydantic import BaseModel, Field

APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR / "artifacts" / "bank_marketing_semma.joblib"

app = FastAPI(title="Bank Marketing SEMMA API", version="0.1.0")


def load_pipeline():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Missing bank_marketing_semma.joblib. Train and export the pipeline first.")
    return load(MODEL_PATH)


class MarketingPayload(BaseModel):
    age: int = Field(..., ge=18, le=99)
    job: str
    marital: str
    education: str
    default: str
    housing: str
    loan: str
    contact: str
    month: str
    day_of_week: str
    duration: int = Field(..., ge=0)
    campaign: int = Field(..., ge=1)
    pdays: int = Field(..., ge=-1)
    previous: int = Field(..., ge=0)
    poutcome: str
    emp_var_rate: float = Field(..., description="Economic indicator from dataset (emp.var.rate)")
    cons_price_idx: float = Field(..., description="Consumer price index")
    cons_conf_idx: float = Field(..., description="Consumer confidence index")
    euribor3m: float = Field(..., ge=0)
    nr_employed: float = Field(..., ge=0)
    days_since_last_contact: int = Field(..., ge=0)
    call_duration_bucket: str


class MarketingPrediction(BaseModel):
    subscription_probability: float
    recommendation: str


@app.post("/score", response_model=MarketingPrediction)
def score(payload: MarketingPayload):
    try:
        pipeline = load_pipeline()
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    df = pd.DataFrame([payload.dict()])
    proba = pipeline.predict_proba(df)[0, 1]
    recommendation = "prioritize" if proba >= 0.6 else "nurture" if proba >= 0.4 else "defer"
    return MarketingPrediction(subscription_probability=float(proba), recommendation=recommendation)


@app.get("/healthz")
def healthcheck():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
