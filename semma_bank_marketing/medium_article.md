# SEMMA in Action: Bank Marketing Response Optimization

> Applying the SAS-inspired SEMMA framework to transform marketing call logs into a precision targeting engine.

## Campaign Snapshot
- **Goal**: Increase term-deposit subscriptions while limiting call center load.
- **Dataset**: Kaggle bank marketing (45k Portuguese banking campaigns).
- **Champion Model**: Logistic regression with balanced weights (ROC-AUC 0.82, lift@10% = 3.1x).

## Sample
- Extracted 30% stratified sample for rapid prototyping while preserving response distribution (11.7% yes).
- Documented sampling error (±1.5%) and quarterly refresh plan.
- Maintained assumption log for socio-economic segments.

## Explore
- Response rate analyzed across age, job, education, previous campaigns.
- Heatmaps and uplift charts revealed high potential among retirees and students with short campaign duration.
- Cohort analysis by previous outcome informed retargeting strategy.

## Modify
- Engineered contact cadence features (days since last contact, call duration bucket).
- Added macroeconomic indicators (unemployment rate, CPI) via public API to capture seasonality.
- Created reproducible transformation recipe stored alongside model artifacts for deployment.

## Model
- Baseline logistic regression for interpretability; AutoGluon challenger explored gradient boosting and catboost variants.
- Calibrated probabilities using isotonic regression, improving marketing threshold decisions.
- Logged runtime and resource usage to ensure feasibility on SAS/IBM tooling if replicated.

## Assess
- Confusion matrix and lift curve translated into incremental revenue projections for marketing leads.
- Established action thresholds (green ≥0.6, amber 0.4–0.6, red <0.4 probability).
- Drafted monitoring dashboard requirements to track campaign performance, drift, and consent compliance.

## Deployment Roadmap
- FastAPI microservice exposes segment-aware scoring endpoint with asynchronous batch support.
- Docker container orchestrated for both on-prem and cloud deployments.
- Backlog includes SAS ODA replication and IBM SPSS comparison for academic completeness.

Artifacts: notebook (`notebooks/semma_bank_marketing.ipynb`), FastAPI assets in `app/`, critique logs under `prompts/`.
