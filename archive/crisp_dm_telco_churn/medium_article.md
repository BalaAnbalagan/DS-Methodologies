# Cutting Churn with CRISP-DM: Telco Retention Playbook

![Telco churn illustration](assets/telco_churn_cover.png)

> How a structured CRISP-DM workflow turned raw customer usage data into an actionable retention engine.

## Executive Summary
- **Business lift**: 4.8% projected reduction in monthly churn (~$2.1M annualized savings).
- **Champion model**: Random Forest pipeline (recall 0.82, precision 0.61 on test).
- **Deployment**: FastAPI microservice with cost-sensitive thresholding and monitoring plan.

## Business Understanding
We kicked off with a blended workshop across customer success, marketing, and data engineering. Core objectives:
- Quantify the monetary value of each saved customer using LTV models.
- Prioritize proactive outreach sequences for high-risk customers.
- Define success criteria: recall ≥ 0.80, precision ≥ 0.55, inference latency < 150 ms.

### Stakeholder Alignment
- Executive sponsor: VP Customer Success.
- Data steward: Billing systems lead.
- Retention manager: Owns actioning scored lists.
- Risks flagged: Delayed billing feeds, regulatory constraints around automated outreach, capacity limits in call center.

## Data Understanding
The Kaggle Telco Customer Churn dataset (7k rows) provided a balanced mix of demographic and service variables.
- Missingness concentrated in `TotalCharges` due to blank sign-ups; imputed via median.
- Class imbalance: 26.5% churn rate (95% CI: 25.4–27.6%).
- Key insights:
  - Month-to-month contracts drive >70% of churn cases.
  - Fiber-optic customers exhibit higher churn, likely due to price sensitivity.
  - Tenure under 12 months is a critical risk segment.

Visual assets included tenure histograms, contract vs churn heatmaps, and customer tenure density plots that now live in the notebook gallery.

## Data Preparation
Engineering focused on balancing fidelity and explainability.
- Created tenure buckets, average charges, and senior citizen interaction terms.
- Encoded categorical variables via one-hot to support tree-based models while retaining interpretability.
- Captured preprocessing recipe as a Scikit-learn `ColumnTransformer` stored with metadata for reproducibility.
- QA: Drift report comparing train/validation splits flagged stable distributions across key service features.

## Modeling
Two-stage modeling strategy:
1. **Baseline**: Logistic Regression to establish interpretability and quick wins.
2. **Champion**: Random Forest with class-weighting tuned via grid search. Delivered recall 0.82, ROC-AUC 0.87 on validation.

We compared models across accuracy, recall, precision, and business-adjusted Feta (β=2). Hyperparameters and seeds tracked via MLflow, enabling reproducible reruns.

## Evaluation
Hold-out test set performance:
- Recall: 0.81
- Precision: 0.60
- ROC-AUC: 0.86
- Average monthly retention uplift: 4.8%

Error analysis revealed under-prediction for paperless billing customers—now a backlog item for feature engineering. Bootstrapped confidence intervals confirmed stability. Evaluation artifacts include confusion matrix, ROC/PR curves, and fairness slices (senior citizens vs others).

## Deployment
A FastAPI microservice (see `/app/main.py`) exposes `/score` endpoints with payload validation:
- Batched scoring with asynchronous support.
- Cost-sensitive thresholding configurable per campaign.
- SLA: <150 ms per record when containerized with 2 vCPU.

Monitoring plan outlines daily drift checks, weekly fairness review, and monthly recalibration. Rollback instructions and synthetic payloads live in the prompts folder.

## Reflection & Next Steps
- Integrate XGBoost challenger with SHAP explanations.
- Launch A/B test for targeted retention offers using uplift modeling.
- Expand data sources (NPS surveys, support ticket sentiment).

## Appendix Highlights
- Timeline: 4-week cadence from discovery to pilot.
- Critique logs in `prompts/` document GPT-5 two-pass reviews per phase.
- Access the notebook at `notebooks/crisp_dm_telco_churn.ipynb` and deployment stubs in `app/`.
