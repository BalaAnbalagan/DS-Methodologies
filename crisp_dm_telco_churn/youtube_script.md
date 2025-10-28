# YouTube Script — CRISP-DM Telco Churn (10 minutes)

## Hook (0:00–0:30)
- "Churn is eating 5% of telco revenue every month. Let me show you how CRISP-DM turns that around."
- Quick teaser of the retention uplift chart.

## Intro & Agenda (0:30–1:00)
- Introduce yourself as the data science lead.
- Outline CRISP-DM phases and mention real dataset from Kaggle.

## Business Understanding (1:00–2:00)
- Present stakeholder slide: VP Success, Retention Lead, Data Engineering.
- Explain KPIs (recall ≥ 0.80, SLA < 150 ms).
- Show before/after churn revenue impact.

## Data Understanding (2:00–3:30)
- Walk through dataset overview, churn rate, and missingness heatmap.
- Highlight key visuals (tenure histogram, contract vs churn).
- Mention critique insights that led to improved storytelling.

## Data Preparation (3:30–4:30)
- Demo preprocessing pipeline snippet in notebook.
- Describe feature engineering (tenure buckets, interaction terms).
- Discuss drift checks and reproducible pipeline packaging.

## Modeling (4:30–6:30)
- Compare logistic regression baseline vs random forest champion.
- Show metric table and calibration plot.
- Explain fairness slices and model cards per critique feedback.

## Evaluation (6:30–7:30)
- Present confusion matrix and ROC/PR curves.
- Translate results into retention lifts and ROI.
- Flag remaining risks from critique log (paperless billing underprediction).

## Deployment (7:30–8:30)
- Live demo of FastAPI `/score` request using synthetic payload.
- Outline monitoring cadence, rollback strategy, and SLA commitments.

## Wrap-up & Next Steps (8:30–9:30)
- Summarize top three learnings.
- Promote upcoming uplift modeling experiment.
- Invite viewers to download notebook and prompts via GitHub repo.

## Call to Action (9:30–10:00)
- "Like, subscribe, and drop a comment if you want a deep dive on the monitoring dashboard!"
- Encourage following Medium article for full narrative.
