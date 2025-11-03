# Credit Card Fraud — KDD Project

End-to-end Knowledge Discovery in Databases (KDD) workflow for highly imbalanced transaction data.

## Structure
- `data/` — Download instructions for Kaggle credit card fraud dataset.
- `notebooks/` — KDD notebook detailing each phase.
- `prompts/` — GPT-5 critique prompts and revision notes.
- `app/` — FastAPI deployment assets.
- `medium_article.md` — Storytelling draft.
- `youtube_script.md` — 9-minute video outline.

## Runbook
1. Download `creditcard.csv` into `data/raw/`.
2. Launch `notebooks/kdd_credit_card_fraud.ipynb` in Colab or local Jupyter.
3. Execute cells by KDD phase, capturing visuals for Medium article.
4. After each phase, run two-pass critique and log outcomes in `prompts/`.

## Deployment Notes
- Dockerfile builds slim Python runtime with scikit-learn and FastAPI.
- `/score` endpoint returns fraud probability and risk tier.
- Includes placeholder for model artifact (`app/artifacts/credit_fraud_model.joblib`).

## Operations Checklist
- Daily monitoring for drift (population stability index).
- Weekly threshold tuning with fraud operations.
- Quarterly compliance review for model risk governance.
