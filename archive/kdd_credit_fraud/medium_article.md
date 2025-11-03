# Mining Fraud Signals with the KDD Process

> Capturing rare fraud events required a disciplined Knowledge Discovery in Databases (KDD) lifecycle crafted for high-stakes financial decisions.

## Overview
- **Objective**: Detect fraudulent credit card transactions with high recall while keeping analyst workload sustainable.
- **Dataset**: Kaggle credit card fraud (anonymized PCA features, 0.172% fraud rate).
- **Outcome**: Weighted logistic regression delivering ROC-AUC 0.98 and AUPRC 0.86 on test.

## Selection
We partnered with the fraud operations team to confirm the Kaggle dataset aligned with real-world schema. Key considerations:
- Used full 2013 time window to maintain seasonality.
- Verified no post-authorization fields (avoiding leakage).
- Established governance contacts and quarterly refresh cadence.

## Preprocessing
- Integrity checks: row counts vs checksum, null audits (none found).
- Stratified time-aware splits (train/validation/test) preserving fraud ratio.
- Data quality dashboard built with Great Expectations to automate future refresh validation.

## Transformation
Feature engineering targeted signal amplification:
- Standardized `Amount` and `Time`; engineered transactional velocity (hourly aggregates).
- Evaluated SMOTE vs class weighting; class weighting chosen to preserve authentic distributions.
- Persisted scaler parameters and feature order for consistent inference.

## Data Mining
Algorithm exploration focused on balancing performance and maintainability.
- Weighted logistic regression baseline; tuned C parameter via cross-validation.
- Isolation Forest for anomaly detection benchmark.
- Documented LightGBM and autoencoder experiments (maintained as challengers).
- Latency test: logistic regression scoring 10k transactions in 22 ms.

## Interpretation & Evaluation
- Business translation: recall 0.86 equals ~$420k monthly fraud prevented (baseline $0.5M loss).
- Threshold tuning grid delivered fraud catch vs workload trade-offs for analysts.
- SHAP analysis highlighted `V14`, `V12`, and `scaled_amount` as top drivers.
- Monitoring plan: real-time drift detection, weekly fairness audit, monthly calibration review.

## Deployment Snapshot
FastAPI service exposes `/score` for batch scoring with payload validation and optional threshold override. Dockerized container (Python 3.10, scikit-learn 1.2) deploys via CI/CD pipeline with automated unit tests.

## Lessons & Next Steps
- Integrate streaming inference prototype using Kafka for sub-second scoring.
- Test supervised contrastive learning for representation improvements.
- Align with compliance for annual model risk management audit.

Artifacts: notebook (`notebooks/kdd_credit_card_fraud.ipynb`), deployment stubs in `app/`, critique logs under `prompts/`.
