# Telco Churn — CRISP-DM Project

This project executes the full CRISP-DM lifecycle on the Kaggle Telco Customer Churn dataset.

## Structure
- `data/` — Instructions and storage for raw data downloads.
- `notebooks/` — Main notebook covering every CRISP-DM phase.
- `prompts/` — GPT-5 critique prompts and revision logs.
- `app/` — FastAPI microservice, artifacts, and Dockerfile.
- `medium_article.md` — Long-form narrative.
- `youtube_script.md` — 10-minute walkthrough script.

## Quick Start
1. Authenticate with Kaggle CLI (`kaggle datasets download blastchar/telco-customer-churn`).
2. Place `Telco-Customer-Churn.csv` under `data/raw/`.
3. Open `notebooks/crisp_dm_telco_churn.ipynb` in Colab or Jupyter. Run cells sequentially per phase.
4. Update critique logs in `prompts/` after each GPT-5/Claude review pass.

## Deployment
- Build Docker image: `docker build -t telco-churn-app app/`.
- Run locally: `docker run -p 8000:8000 telco-churn-app`.
- FastAPI endpoint: `POST /score` with payload fields documented in `app/README.md`.

## Monitoring Checklist
- Weekly drift report on key categorical features.
- Monthly fairness audit on senior citizen segment.
- Quarterly security review of dependencies.

Further details live in the notebook and Medium draft.
