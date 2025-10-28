# 🎥 Video Talk Track: CRISP-DM Telco Customer Churn Prediction

**Duration**: 8-12 minutes
**Target Audience**: Data science students, practitioners learning CRISP-DM
**Skill Level**: Intermediate

---

## 📋 Pre-Recording Checklist

- [ ] Open notebook in Jupyter/Colab
- [ ] Have dataset loaded (7,043 customers)
- [ ] Clear all outputs and restart kernel for fresh run
- [ ] Have project charter visible
- [ ] Prepare to show visualizations

---

## 🎬 Video Structure

### INTRO (0:00 - 1:00)

**[Show title slide: "CRISP-DM: Predicting Telco Customer Churn"]**

**Talk Track:**
> "Welcome! Today we're walking through a complete CRISP-DM implementation for predicting customer churn at a telecommunications company. CRISP-DM stands for Cross-Industry Standard Process for Data Mining, and it's one of the most widely used frameworks in industry.
>
> Here's what makes this project special: We're not just building a model. We're following a business-driven process that starts with understanding stakeholder needs and ends with a deployable solution that actually makes money.
>
> By the end of this video, you'll see how CRISP-DM's six phases work together to deliver a production-ready churn prediction system."

**[Show notebook title cell]**

---

### PHASE 1: BUSINESS UNDERSTANDING (1:00 - 2:30)

**[Show project charter code cell]**

**Talk Track:**
> "Phase 1 is Business Understanding, and this is where CRISP-DM really shines. Before we touch any data, we're meeting with stakeholders to understand what they actually need.
>
> **[Point to stakeholders]** Our stakeholders include the VP of Customer Success, the Retention Analytics Lead, and Data Engineering. Each has different concerns.
>
> **[Point to business objectives]** The business wants two things: Quantify churn risk and prioritize retention campaigns. This isn't about building the most accurate model - it's about solving a business problem.
>
> **[Point to success criteria]** We've agreed that our model needs at least 80% recall. Why recall? Because in retention campaigns, it's more expensive to miss a churner than to accidentally target someone who wasn't going to leave. We'd rather have some false positives than miss true churners.
>
> **[Point to constraints]** The model must be explainable - stakeholders need to understand WHY someone is predicted to churn. And we need monthly data refreshes since customer behavior changes."

**[Run project charter cell]**

**🤖 AI Learning Checkpoint:**
> "This is a great place to pause. Take this project charter to ChatGPT or Claude and ask: 'Am I missing any stakeholders? Are my success criteria aligned with the business objective? What about regulatory or ethical considerations?' The AI will push your thinking further."

---

### PHASE 2: DATA UNDERSTANDING (2:30 - 4:30)

**[Run data loading cell]**

**Talk Track:**
> "Phase 2: Data Understanding. Now we can finally look at the data.
>
> **[Show shape output]** We have 7,043 customers with 21 features. This is a manageable dataset - small enough to iterate quickly but large enough to build production models.
>
> **[Run churn distribution cell]** Here's the key insight: **73% of customers stay, 27% churn.** That's a 2.8-to-1 imbalance. Not extreme, but enough that we'll need to handle it in modeling.
>
> **[Show class distribution visualization]** This pie chart makes it visual - about 1 in 4 customers are churning. That's actually quite high for a telco company."

**[Run correlation analysis]**

**Talk Track:**
> "Let's find what predicts churn. **[Point to correlation output]** The top 3 features correlated with churn are:
> 1. Tenure - how long they've been a customer (0.352 correlation)
> 2. Total Charges (0.199)
> 3. Monthly Charges (0.193)
>
> These make business sense! Newer customers with higher charges are more likely to leave - probably because they haven't built loyalty yet and they're paying premium prices.
>
> **[Run EDA visualizations]** Look at these patterns:
> - **Tenure vs Churn**: New customers (0-10 months) churn way more
> - **Contract Type**: Month-to-month contracts have massive churn compared to annual contracts
> - **Monthly Charges**: Churners tend to have higher monthly bills
> - **Internet Service**: Fiber optic customers churn more - maybe competitor prices?"

**[Show correlation heatmap]**

**Talk Track:**
> "This heatmap shows all correlations at once. The darker reds show strong positive correlations. Notice tenure has a negative correlation with churn (darker blue) - long-time customers rarely leave."

**🤖 AI Learning Checkpoint:**
> "Pause here. Copy your EDA findings to an AI and ask: 'What patterns am I missing? Should I investigate feature interactions? Are there business insights I should extract from these correlations?' This deepens your analysis."

---

### PHASE 3: DATA PREPARATION (4:30 - 6:00)

**[Run missing values check]**

**Talk Track:**
> "Phase 3: Data Preparation. This is the unglamorous but critical phase.
>
> **[Point to missing values]** We found 11 missing values in TotalCharges. Not many, but we need to handle them. We'll impute with the median - a safe choice that doesn't distort the distribution.
>
> **[Show feature types]** We have 15 categorical features and 4 numeric. The categorical ones need encoding."

**[Run preprocessing pipeline]**

**Talk Track:**
> "Here's our preprocessing pipeline - and this is a best practice you should always follow:
>
> **[Point to ColumnTransformer]**
> - Categorical features: Impute → One-Hot Encode
> - Numeric features: Impute → Standardize with StandardScaler
>
> Why pipelines? Two reasons:
> 1. **Prevents data leakage** - we fit on train, transform on test
> 2. **Makes deployment easy** - we save one object that does all preprocessing
>
> **[Run train/valid/test split]** We split into 70% train (4,930 customers), 15% validation (1,056), and 15% test (1,057). We use stratified splitting to preserve the 73-27 churn ratio in all sets."

**🤖 AI Learning Checkpoint:**
> "Ask AI: 'Is median imputation appropriate for TotalCharges? Should I handle outliers? What other preprocessing steps would improve model performance?' The AI might suggest feature engineering like binning tenure or creating interaction features."

---

### PHASE 4: MODELING (6:00 - 8:00)

**[Run model training cells]**

**Talk Track:**
> "Phase 4: Modeling. This is where we try multiple algorithms and pick the best.
>
> We're training four models:
> 1. **Logistic Regression** - interpretable baseline
> 2. **Random Forest** - ensemble, handles non-linearity
> 3. **XGBoost** - gradient boosting, often wins competitions
> 4. **LightGBM** - faster gradient boosting
>
> Notice we're using `class_weight='balanced'` and `scale_pos_weight` - this tells the algorithms 'hey, churners are rare, pay more attention to them.'"

**[Show model comparison table]**

**Talk Track:**
> "Results are in! **[Point to comparison]**
>
> | Model | ROC-AUC | Recall | Precision | F1-Score |
> |-------|---------|--------|-----------|----------|
> | **Logistic Regression** | **0.8447** | 0.8143 | 0.5055 | 0.6238 |
> | LightGBM | 0.8359 | 0.7321 | 0.5216 | 0.6092 |
> | XGBoost | 0.8246 | 0.7500 | 0.5316 | 0.6222 |
> | Random Forest | 0.8147 | 0.5000 | 0.5983 | 0.5447 |
>
> Surprise! **Logistic Regression wins** with 0.8447 ROC-AUC and 81% recall. Sometimes the simplest model is the best - and it has a huge advantage: we can explain it to stakeholders."

**[Show ROC curves]**

**Talk Track:**
> "These ROC curves compare all models. The closer to the top-left corner, the better. Logistic Regression (blue) edges out the others, especially in the region that matters for our business."

**🤖 AI Learning Checkpoint:**
> "Pause and ask AI: 'Why might Logistic Regression beat ensemble methods here? Should I tune hyperparameters? What about stacking or blending models?' The AI will teach you about the bias-variance tradeoff and when simple beats complex."

---

### PHASE 5: EVALUATION (8:00 - 10:00)

**[Run test set evaluation]**

**Talk Track:**
> "Phase 5: Evaluation. Now we test on data the model has NEVER seen.
>
> **[Show test metrics]**
> - ROC-AUC: 0.8145 (good discrimination)
> - Accuracy: 78.33% (decent)
> - Precision: 62.75% (6 in 10 predictions are right)
> - Recall: 45.55% (we catch 45% of churners)
> - F1-Score: 0.5278 (balanced metric)
>
> **Wait - our recall is only 45.55%!** We wanted 80%. What happened?
>
> We're using the default 0.5 threshold. Let's talk about business impact first, then we can tune the threshold."

**[Show confusion matrix]**

**Talk Track:**
> "The confusion matrix tells the story:
> - **True Negatives: 700** - correctly said they won't churn
> - **False Positives: 76** - we said churn, but they stayed
> - **False Negatives: 153** - **THESE ARE EXPENSIVE** - we missed them and they left
> - **True Positives: 128** - correctly caught churners"

**[Show business impact analysis]**

**Talk Track:**
> "Here's why data science is about business, not just models. Let's calculate ROI:
>
> **Assumptions:**
> - Average customer lifetime value: $1,200
> - Retention campaign cost: $100 per customer
> - Campaign success rate: 35% (industry standard)
>
> **Calculation:**
> - We target 204 customers (TP + FP)
> - We save about 45 customers (128 TP × 35% success rate)
> - **Revenue saved: $53,760** (45 customers × $1,200)
> - **Campaign costs: $20,400** (204 × $100)
> - **Net benefit: $33,360**
> - **ROI: 163.5%!**
>
> Even with 45% recall, we're making money! If we tune the threshold to get 80% recall, we'll target more people (more costs) but save more customers (more revenue). That's an exercise for the stakeholders to optimize."

**[Show success criteria check]**

**Talk Track:**
> "We did NOT meet our 80% recall criteria with the default threshold. In production, we'd tune this threshold based on business costs. But we proved the concept - this model generates positive ROI."

**🤖 AI Learning Checkpoint:**
> "Ask AI: 'How should I tune the threshold to hit 80% recall? What's the optimal precision-recall tradeoff for retention campaigns? Should I worry about model calibration?' The AI will teach you threshold optimization and business-driven modeling."

---

### PHASE 6: DEPLOYMENT (10:00 - 11:30)

**[Show model serialization]**

**Talk Track:**
> "Phase 6: Deployment. We're not done until the model is in production.
>
> **[Point to joblib dump]** We serialize the entire pipeline - preprocessing + model - into one .joblib file. This means anyone can load it and make predictions without rewriting preprocessing code.
>
> **[Show artifacts directory]** Our deployment artifacts:
> - `telco_churn_pipeline.joblib` - the trained pipeline
> - `feature_metadata.json` - feature names and types
> - `model_card.json` - documentation of everything
>
> **[Show FastAPI example]** In the `/app` folder, there's a FastAPI service ready to score customers in real-time. You POST customer features, you GET back churn probability and risk level (high/medium/low).
>
> **[Mention Docker]** There's also a Dockerfile - you can deploy this entire service to cloud with one command."

**[Show model card snippet]**

**Talk Track:**
> "The model card documents everything stakeholders need to know:
> - **Performance**: 81.45% ROC-AUC on test
> - **Limitations**: 'Model trained on 2013 data, requires monthly retraining'
> - **Ethical considerations**: 'Ensure fair treatment across demographics, avoid discriminatory targeting'
> - **Usage**: 'Batch scoring for monthly retention campaigns'
>
> This is professional ML engineering. Models without documentation cause problems in production."

---

### CONCLUSION & NEXT STEPS (11:30 - 12:00)

**Talk Track:**
> "Let's recap what we accomplished with CRISP-DM:
>
> **Phase 1 - Business Understanding**: Aligned with stakeholders on 80% recall goal
> **Phase 2 - Data Understanding**: Found tenure, charges, contract type predict churn
> **Phase 3 - Data Preparation**: Built clean preprocessing pipeline
> **Phase 4 - Modeling**: Logistic Regression beat fancy algorithms (0.8447 ROC-AUC)
> **Phase 5 - Evaluation**: Generated $33,360 net benefit (163% ROI)
> **Phase 6 - Deployment**: Production-ready FastAPI service with model card
>
> **What makes CRISP-DM different?**
> - **Business-first**: We started with stakeholders, not data
> - **Iterative**: We can loop back to any phase
> - **Practical**: We focused on deployment from day one
> - **Explainable**: We chose an interpretable model stakeholders can trust
>
> **Your next steps:**
> 1. Clone this repo and run the notebook
> 2. At each 🤖 checkpoint, use AI to critique your work
> 3. Compare with KDD and SEMMA methodologies (also in this repo)
> 4. Try threshold tuning to hit 80% recall
> 5. Add SHAP explanations for model interpretability
>
> **Resources:**
> - Full notebook: [GitHub link]
> - Medium article: [Detailed writeup with all visualizations]
> - AI learning guide: HOW_TO_LEARN_WITH_AI.md
>
> Thanks for watching! If you found this helpful, check out the KDD fraud detection and SEMMA marketing optimization videos. Subscribe for more methodology deep dives!"

---

## 🎬 Recording Tips

### Visual Aids to Show
1. **Business Understanding**: Project charter dictionary printed nicely
2. **Data Understanding**: Churn distribution pie chart, correlation heatmap
3. **Data Preparation**: Pipeline diagram (draw this!)
4. **Modeling**: Model comparison bar chart, ROC curves
5. **Evaluation**: Confusion matrix heatmap, business impact bar chart
6. **Deployment**: Model card JSON, FastAPI code

### Pacing Tips
- **Speak slowly** at checkpoints - viewers should pause
- **Repeat key numbers**: "45% recall - that's less than our 80% goal"
- **Use analogies**: "Threshold tuning is like adjusting a thermostat"
- **Point to visuals**: Don't just talk about charts, point at specific areas

### Common Student Questions to Address
1. *"Why did Logistic Regression beat XGBoost?"* - Sometimes data is linearly separable, and simpler is better
2. *"How do I choose between accuracy, precision, and recall?"* - It depends on business costs
3. *"Do I always need 80% recall?"* - No! It's problem-specific. For fraud, you might want 95%+
4. *"Can I use this in Colab?"* - Yes! There are setup cells for Colab in the notebook

### Engagement Hooks
- **Start**: "Have you ever wondered how Netflix knows you're about to cancel?"
- **Middle**: "Here's where most data scientists mess up - they skip the business understanding"
- **End**: "The best model is the one that gets deployed - not the one with the highest accuracy"

---

## 📊 Key Metrics to Emphasize

| Metric | Value | Why It Matters |
|--------|-------|----------------|
| ROC-AUC | 0.8145 | Good discrimination between churners and non-churners |
| Recall | 45.55% | We catch less than half of churners - needs threshold tuning |
| Precision | 62.75% | Of customers we target, 63% are actual churners |
| Net Benefit | $33,360 | **THE NUMBER THAT MATTERS** - we make money! |
| ROI | 163.5% | For every $1 spent on campaigns, we get $2.64 back |

---

## 🎯 Learning Objectives (State These)

After watching, viewers will be able to:
1. ✅ Explain all 6 CRISP-DM phases with real examples
2. ✅ Justify model selection with business metrics, not just accuracy
3. ✅ Calculate ROI for a retention campaign
4. ✅ Build an end-to-end pipeline from business problem to deployment
5. ✅ Use AI to critique and improve each phase

---

*Generated based on actual notebook execution results*
*CRISP-DM Test Results: ROC-AUC 0.8145 | Net Benefit $33,360 | Ready for deployment*
