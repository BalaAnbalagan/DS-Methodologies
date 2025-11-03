# Telco Churn FastAPI Service

## Setup
1. Ensure `artifacts/telco_churn_pipeline.joblib` exists (exported from notebook).
2. Install dependencies: `pip install -r requirements.txt`.
3. Run service: `uvicorn main:app --host 0.0.0.0 --port 8000`.

## Endpoints
- `GET /healthz` — Liveness probe.
- `POST /score` — Accepts a single payload of customer attributes and returns churn probability and risk tier.

## Sample Payload
```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "No",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 80.65,
  "TotalCharges": 1020.5
}
```

## Docker
- Build: `docker build -t telco-churn-app .`
- Run: `docker run -p 8000:8000 telco-churn-app`

Remember to document monitoring and rollback procedures in the project README.
