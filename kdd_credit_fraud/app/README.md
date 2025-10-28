# Credit Card Fraud FastAPI Service

## Prerequisites
- `artifacts/credit_fraud_model.joblib` and `artifacts/feature_order.joblib` exported from the notebook.

## Local Run
```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Score Endpoint
`POST /score`
```json
{
  "features": {
    "V1": -1.3598071337,
    "V2": -0.0727811733,
    "V3": 2.5363467383,
    "V4": 1.3781552243,
    "V5": -0.3383207699,
    "scaled_amount": 0.245,
    "scaled_time": 0.512,
    "hour": 12
    // include remaining PCA features from feature_order.joblib
  }
}
```

Response includes fraud probability and risk band (low/medium/high/critical).

## Docker
- Build: `docker build -t fraud-kdd-app .`
- Run: `docker run -p 8000:8000 fraud-kdd-app`

Instrument monitoring hooks (e.g., Prometheus, OpenTelemetry) before deploying to production.
