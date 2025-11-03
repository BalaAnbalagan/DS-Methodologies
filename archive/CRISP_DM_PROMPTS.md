# CRISP-DM ChatGPT Prompts (Copy-Paste Ready)

Quick reference for getting AI critiques at each phase.

---

## Expert Persona (Use Once at Start)

```
You are a world-renowned CRISP-DM methodology expert who has:
- Led 50+ enterprise data science projects following CRISP-DM
- Written award-winning books: "Mastering CRISP-DM" and "Business-Driven Data Science"
- Trained over 10,000 data scientists at Fortune 500 companies

You provide detailed, actionable critiques focused on methodological rigor and business value.
```

---

## Phase 1: Business Understanding

**After running your business understanding code, copy this:**

```
Review my Business Understanding phase for telco churn prediction.

CONTEXT:
- Methodology: CRISP-DM
- Project: Telco Customer Churn Prediction
- Goal: Reduce churn through predictive retention campaigns

MY WORK:
[Paste your project_charter code and output here]

CRITIQUE QUESTIONS:
1. Have I clearly defined the business problem and objectives?
2. Are my success criteria (Recall ≥ 0.80) appropriate for this business case?
3. What stakeholders or constraints am I missing?
4. What business questions should I be asking about churn economics?
5. How can I better align technical metrics with business value?

Please provide 5-10 actionable improvements to strengthen this phase.
```

---

## Phase 2: Data Understanding

**After running EDA, copy this:**

```
Review my Data Understanding phase for telco churn prediction.

CONTEXT:
- Dataset: 7,043 customers, 21 features
- Class distribution: [paste your churn rate here]
- Top correlated features: [paste correlation results]

MY ANALYSIS:
[Paste key findings: churn rate, top correlations, distribution insights]

CRITIQUE QUESTIONS:
1. Have I thoroughly explored all important aspects of the data?
2. Are there any critical patterns or anomalies I might have missed?
3. What additional EDA visualizations would strengthen my understanding?
4. How should I interpret the class imbalance for modeling?
5. What business insights can I extract from these correlations?
6. Are there potential data quality issues I should investigate?

Provide 5-10 actionable improvements for this phase.
```

---

## Phase 3: Data Preparation

**After preprocessing, copy this:**

```
Review my Data Preparation phase for telco churn prediction.

CONTEXT:
- Missing data: TotalCharges had [X] missing values, filled with median
- Encoding: One-Hot Encoding for categorical features
- Scaling: StandardScaler for numeric features
- Split: 70% train / 15% validation / 15% test (stratified)

MY CODE:
[Paste your preprocessing pipeline code]

RESULTS:
- Train shape: [paste shape]
- Valid shape: [paste shape]
- Test shape: [paste shape]

CRITIQUE QUESTIONS:
1. Is median imputation appropriate for TotalCharges, or should I use a different strategy?
2. Should I handle outliers before or after splitting?
3. Are there any feature engineering opportunities I'm missing?
4. Is my train/validation/test split ratio optimal?
5. Should I consider different encodings (e.g., target encoding, ordinal)?
6. Are there any data leakage risks in my pipeline?
7. What preprocessing steps might improve model performance?

Provide 5-10 actionable improvements.
```

---

## Phase 4: Modeling

**After training models, copy this:**

```
Review my Modeling phase for telco churn prediction.

CONTEXT:
- Problem: Binary classification (churn prediction)
- Class imbalance: [paste ratio]
- Models trained: Logistic Regression, Random Forest, XGBoost, LightGBM

MY RESULTS:
[Paste model comparison table with Accuracy, Precision, Recall, F1, ROC-AUC]

Champion Model: [paste champion model name and metrics]

CRITIQUE QUESTIONS:
1. Is my model selection appropriate for this business problem?
2. How well am I handling class imbalance?
3. Should I tune hyperparameters differently?
4. Are there other algorithms I should consider?
5. Is my model comparison methodology sound?
6. How can I better interpret the SHAP values for business stakeholders?
7. Are there ensemble or stacking opportunities?
8. What's the trade-off between model complexity and interpretability?

Provide 5-10 actionable improvements.
```

---

## Phase 5: Evaluation

**After test evaluation, copy this:**

```
Review my Evaluation phase for telco churn prediction.

CONTEXT:
- Success Criteria: Recall ≥ 0.80
- Business Goal: Maximize retention while minimizing wasted campaign spend

TEST SET RESULTS:
[Paste classification report]

Confusion Matrix:
- True Positives: [paste TP]
- True Negatives: [paste TN]
- False Positives: [paste FP]
- False Negatives: [paste FN]

BUSINESS IMPACT:
[Paste: customers targeted, saved, revenue saved, campaign costs, net benefit, ROI]

CRITIQUE QUESTIONS:
1. Did I meet the business success criteria (Recall ≥ 0.80)?
2. How should I interpret the precision-recall trade-off for this use case?
3. Are there better evaluation metrics I should consider?
4. Is my cost-benefit analysis realistic and comprehensive?
5. What threshold tuning might improve business outcomes?
6. How can I better communicate results to non-technical stakeholders?
7. What additional validation should I perform (e.g., cross-validation)?
8. Are there fairness or bias concerns I should investigate?

Provide 5-10 actionable improvements.
```

---

## Phase 6: Deployment

**After creating deployment artifacts, copy this:**

```
Review my Deployment phase for telco churn prediction.

CONTEXT:
- Champion Model: [paste model name]
- Deployment: FastAPI microservice
- Artifacts: Model pipeline (joblib), feature metadata, model card

MY DEPLOYMENT PLAN:
Model Card:
[Paste your model_card dictionary]

Sample API Payload:
[Paste sample_payload]

CRITIQUE QUESTIONS:
1. Is my model serialization approach production-ready?
2. What's missing from my model card?
3. Are my ethical considerations comprehensive?
4. What monitoring should I implement post-deployment?
5. How should I handle model versioning and updates?
6. What testing strategy should I use for the API?
7. Are there scalability concerns I should address?
8. What documentation would help future maintainers?
9. How should I plan for model retraining and drift detection?

Provide 5-10 actionable improvements for production deployment.
```

---

## Quick Workflow

1. **Run phase code in notebook**
2. **Copy relevant prompt above**
3. **Paste your actual results** where indicated
4. **Paste into ChatGPT**
5. **Get critique**
6. **Apply improvements**
7. **Repeat for next phase**

---

## Save Your Critiques

Create a file for each phase:
- `critiques/business_understanding.txt`
- `critiques/data_understanding.txt`
- `critiques/data_preparation.txt`
- `critiques/modeling.txt`
- `critiques/evaluation.txt`
- `critiques/deployment.txt`

Paste ChatGPT's responses there for your assignment submission.
