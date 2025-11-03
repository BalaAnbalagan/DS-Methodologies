# Bank Marketing — SEMMA Project

SEMMA workflow for optimizing term-deposit marketing campaigns using Kaggle's bank marketing dataset.

## Structure
- `data/` — Data acquisition instructions and storage.
- `notebooks/` — Core SEMMA notebook.
- `prompts/` — Critique prompts with revision logs.
- `app/` — FastAPI deployment scaffold.
- `medium_article.md` — Storytelling draft for publication.
- `youtube_script.md` — 8-minute video script.

## Procedure
1. Download `bank-additional-full.csv` into `data/raw/`.
2. Open `notebooks/semma_bank_marketing.ipynb` (Colab recommended).
3. Follow SEMMA phases sequentially, capturing visuals for content pieces.
4. Apply GPT-5/Claude critique twice per phase and log outcomes.

## Deployment Snapshot
- FastAPI service exposes `/score` with asynchronous batch support.
- Docker image ready for containerized deployment; adapt to SAS/IBM if needed.
- Placeholder artifact `app/artifacts/bank_marketing_semma.joblib` saved by notebook.

## Operational Notes
- Monitor lift scores weekly during campaigns.
- Refresh macroeconomic features monthly.
- Coordinate with compliance on consent and opt-out policies.
