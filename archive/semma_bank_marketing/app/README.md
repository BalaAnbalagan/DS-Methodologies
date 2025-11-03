# Bank Marketing FastAPI Service

## Preparation
- Ensure `artifacts/bank_marketing_semma.joblib` is exported from the notebook.

## Local Launch
```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Endpoints
- `GET /healthz` — Service heartbeat.
- `POST /score` — Accepts a single customer payload and returns subscription probability plus recommendation.

## Example Payload
```json
{
  "age": 42,
  "job": "admin.",
  "marital": "married",
  "education": "university.degree",
  "default": "no",
  "housing": "yes",
  "loan": "no",
  "contact": "cellular",
  "month": "may",
  "day_of_week": "thu",
  "duration": 210,
  "campaign": 3,
  "pdays": 999,
  "previous": 1,
  "poutcome": "success",
  "emp_var_rate": 1.1,
  "cons_price_idx": 93.994,
  "cons_conf_idx": -36.4,
  "euribor3m": 4.857,
  "nr_employed": 5191.0,
  "days_since_last_contact": 27,
  "call_duration_bucket": "180-240"
}
```

## Docker Usage
- Build: `docker build -t semma-bank-app .`
- Run: `docker run -p 8000:8000 semma-bank-app`

Augment with monitoring/logging middleware before production deployment.
