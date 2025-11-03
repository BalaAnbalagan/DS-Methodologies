# YouTube Script — KDD Credit Card Fraud (9 minutes)

## Hook (0:00–0:25)
- "Every minute, thousands of card transactions stream in. How do you catch the fraudulent ones without drowning analysts?"
- Flash highlight: ROC-AUC 0.98 with manageable workload.

## Agenda (0:25–0:45)
- Introduce KDD phases and high-level flow.
- Mention Kaggle dataset and anonymized features.

## Selection (0:45–1:45)
- Discuss data sourcing, leakage checks, and governance contacts.
- Show traceability table linking features to business goals.

## Preprocessing (1:45–2:45)
- Walk through integrity dashboard (checksums, missingness).
- Explain stratified time-aware splitting strategy.

## Transformation (2:45–4:00)
- Demo creation of scaled amount/time and velocity features.
- Compare SMOTE vs class weighting experiments; share critique-inspired improvements.

## Data Mining (4:00–6:15)
- Present experiment matrix: logistic regression, isolation forest, lightGBM, autoencoder.
- Highlight performance metrics and latency benchmarks.
- Mention MLflow tracking and critique tips on fairness.

## Interpretation & Evaluation (6:15–7:45)
- Translate precision/recall into fraud dollars saved.
- Show threshold tuning grid and SHAP beeswarm chart.
- Outline monitoring KPIs and compliance considerations.

## Deployment Snapshot (7:45–8:30)
- Demonstrate FastAPI scoring request and Docker packaging.
- Mention drift monitoring backlog and stream-processing roadmap.

## Closing (8:30–9:00)
- Recap key takeaways and invite feedback on next anomaly detection techniques.
- Point audience to Medium article and GitHub repo.
