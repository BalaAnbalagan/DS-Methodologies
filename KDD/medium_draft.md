# KDD Process: Unsupervised Fraud Detection with Isolation Forest

*When labels are scarce or untrustworthy, let the data reveal anomalies—and learn from the limitations*

## Abstract

The Knowledge Discovery in Databases (KDD) process represents one of the earliest formalized data mining methodologies, emphasizing knowledge extraction through Selection, Preprocessing, Transformation, Data Mining, and Interpretation. In this article, we apply KDD's unsupervised approach to credit card fraud detection using Isolation Forest—achieving 29.12% precision and 16.87% recall. While these metrics pale compared to supervised methods, they reveal crucial insights about when unsupervised anomaly detection shines and when it struggles.

## Introduction: The KDD Philosophy

Unlike CRISP-DM's business-centric approach or SEMMA's rapid prototyping focus, KDD emphasizes **knowledge discovery as a scientific process**. Born in the academic research community, KDD treats data mining as hypothesis generation and testing.

**The Five KDD Phases:**

1. **Selection**: Choose relevant data subsets
2. **Preprocessing**: Clean and handle missing values
3. **Transformation**: Engineer features and reduce dimensionality
4. **Data Mining**: Apply algorithms to extract patterns
5. **Interpretation/Evaluation**: Validate discoveries and generate insights

For fraud detection, we leverage KDD's strength in **unsupervised learning**—detecting anomalies without relying on labeled fraud examples.

## Why Unsupervised Anomaly Detection?

Supervised models (like our CRISP-DM random forest achieving 96.5% precision) require labeled training data. But what if:

- Labels are unavailable (new fraud patterns emerging)
- Labels are unreliable (only caught frauds are labeled; successful frauds go undetected)
- Fraud evolves faster than labeling processes
- You want to discover unknown fraud types, not just detect known patterns

Unsupervised anomaly detection addresses these scenarios by learning "normal" behavior and flagging deviations—no labels required during training.

## Selection & Preprocessing: All Data, No Labels

**Dataset Selection:**
- Total transactions: 284,807
- Features: 30 (V1-V28 from PCA, plus Time and Amount)
- Class labels: Available but **intentionally unused during training**

Unlike SEMMA's strategic sampling (49K transactions) or CRISP-DM's train/test split, KDD's unsupervised approach uses **all 284,807 transactions** to learn the broadest possible definition of "normal."

**Preprocessing:**
- No missing values to handle (clean dataset)
- Standardization: Z-score normalization ensures equal feature weighting
- No label-based stratification (we're unsupervised!)

**Key Decision**: We drop the Class column entirely during training, only using it later for evaluation. This mirrors real-world scenarios where new fraud types have no labels.

## Transformation: Feature Standardization

Feature engineering in unsupervised settings requires careful thought. Too much transformation risks removing the very anomalies we seek.

**Our Approach:**
```python
X_scaled = StandardScaler().fit_transform(X)
```

**Why minimal transformation?**
- PCA features (V1-V28) already capture nonlinear relationships
- Amount and Time preserve temporal and magnitude information
- Over-engineering (e.g., polynomial features) could mask anomalies
- Isolation Forest is robust to feature scales, but standardization improves interpretability

**Alternative Transformations Considered:**
- Dimensionality reduction (t-SNE, UMAP) for visualization
- Temporal binning of Time into hour-of-day
- Log-transformation of Amount

We opt for simplicity to establish a baseline, reserving advanced transformations for iteration cycles.

## Data Mining: Isolation Forest

**Algorithm Choice**: Isolation Forest

Isolation Forest works on a brilliant principle: **anomalies are easier to isolate than normal points**. By randomly partitioning feature space, outliers require fewer splits to isolate than dense normal points.

**Hyperparameters:**
- `n_estimators=100`: 100 isolation trees
- `contamination=0.001`: Expect 0.1% of data to be anomalies (conservative estimate; true fraud rate is 0.17%)
- `random_state=42`: Reproducibility

**Why these settings?**
- Contamination=0.001 is intentionally lower than true fraud rate (0.17%) to be conservative
- 100 trees balance ensemble diversity against computational cost
- Setting contamination too high would flag too many false positives

**Training Process:**
1. Build 100 random decision trees
2. Each tree randomly selects features and split values
3. Anomalies require fewer splits to isolate (short tree paths)
4. Aggregate anomaly scores across all trees
5. Flag 284 transactions (0.1% of 284,807) as anomalies

**Critical Insight**: The model never sees fraud labels during training. It learns purely from the distribution of V1-V28, Time, and Amount.

## Interpretation: The Reality Check

Now comes the moment of truth: how well do unsupervised anomalies correspond to actual fraud?

**Model Results:**

| Metric | Score |
|--------|-------|
| **Precision** | 29.12% |
| **Recall** | 16.87% |
| **F1 Score** | 21.36% |

**Confusion Matrix:**
- True Negatives: 284,113 (legitimate transactions correctly ignored)
- False Positives: 202 (legitimate transactions incorrectly flagged)
- False Negatives: 409 (frauds missed—**83% of all frauds!**)
- True Positives: 83 (frauds correctly detected—only **17% of frauds**)

### Interpreting These Results

At first glance, these metrics seem disappointing compared to supervised methods:
- CRISP-DM Random Forest: 96.52% precision, 75% recall
- SEMMA Random Forest: 93.85% precision, 82.43% recall
- KDD Isolation Forest: **29.12% precision, 16.87% recall**

**But context matters:**

**Precision 29.12%**: Of 285 flagged transactions, only 83 are actual fraud. This means fraud analysts would investigate 202 false positives—a 71% false alert rate. In production, this operational burden is often unacceptable.

**Recall 16.87%**: The model catches only 83 of 492 frauds (17%). This means **409 frauds slip through undetected**—a catastrophic miss rate for a fraud detection system.

**Why Such Poor Performance?**

1. **Contamination Mismatch**: We set contamination=0.001 (0.1%) but true fraud rate is 0.17%—guaranteeing we under-flag anomalies
2. **Frauds Aren't Always Outliers**: Some frauds mimic legitimate transactions in V1-V28 space
3. **No Supervision Signal**: The model has no feedback about what makes fraud different from legitimate transactions
4. **Class Imbalance**: With 579:1 imbalance, "normal" overwhelms the feature space

## Comparison: Supervised vs. Unsupervised

| Approach | Precision | Recall | F1 | ROC AUC | When to Use |
|----------|-----------|--------|----|----|-------------|
| **CRISP-DM (Supervised)** | 96.52% | 75.00% | 84.41% | 92.46% | Labels available, production deployment |
| **SEMMA (Supervised)** | 93.85% | 82.43% | 87.77% | 97.79% | Rapid prototyping with labels |
| **KDD (Unsupervised)** | 29.12% | 16.87% | 21.36% | N/A | No labels, exploratory analysis |

The performance gap is stark—but that doesn't make unsupervised methods worthless.

## When Unsupervised Methods Shine

Despite poor metrics, Isolation Forest excels in specific scenarios:

### 1. **Novelty Detection**
When entirely new fraud patterns emerge, supervised models trained on historical fraud fail. Unsupervised methods flag "anything unusual," catching zero-day fraud types.

### 2. **Label Contamination**
If labeled "non-fraud" actually contains undetected fraud, supervised models learn the wrong patterns. Unsupervised methods aren't biased by mislabeled data.

### 3. **Exploration Phase**
Before investing in labeling efforts, unsupervised methods identify which transactions to label first—focusing human effort on high-value anomalies.

### 4. **Hybrid Approaches**
Combine unsupervised anomaly scores as features for supervised models:
```python
X_enhanced = [V1, V2, ..., V28, Time, Amount, IsolationForest_Score]
```

This hybrid approach often outperforms either method alone.

## Improving Unsupervised Performance

Several strategies could boost KDD results:

### Hyperparameter Tuning
- Increase `contamination` to 0.0017 (match true fraud rate)
- Experiment with `max_samples` to control tree depth
- Try different random seeds and ensemble results

### Alternative Algorithms
- **One-Class SVM**: Learns a decision boundary around normal data
- **Autoencoders**: Neural networks that reconstruct normal patterns; anomalies have high reconstruction error
- **Local Outlier Factor (LOF)**: Density-based anomaly detection
- **DBSCAN Clustering**: Flag points that don't belong to any cluster

### Feature Engineering
- **Temporal Features**: Hour-of-day, day-of-week from Time
- **Amount Binning**: Categorical high/medium/low transaction values
- **Velocity Features**: Transaction frequency per time window (requires sequence data)

### Ensemble Methods
- Combine multiple unsupervised algorithms (Isolation Forest + LOF + Autoencoder)
- Use voting or averaging to improve robustness

## Expert Critique: KDD Methodology Lessons

**Strengths of KDD Process:**
- Emphasizes scientific rigor and knowledge discovery
- Well-suited for exploratory research
- Flexible framework accommodating various algorithms
- Strong focus on interpretation and validation

**Weaknesses for Production Fraud Detection:**
- Lacks business context and deployment planning (unlike CRISP-DM)
- No inherent iteration loops (unlike SEMMA)
- Unsupervised approach sacrifices performance for generality
- Limited guidance on evaluation metrics for anomaly detection

**Recommendation**: Use KDD for **research and exploration**, then transition to CRISP-DM for production deployment. The knowledge discovered through unsupervised analysis informs supervised model design.

## Conclusion: The Right Tool for the Right Job

Our KDD implementation achieved 29% precision and 17% recall—far below supervised methods—but this isn't a failure. It's an honest demonstration of unsupervised anomaly detection's trade-offs:

**What We Learned:**
1. Unsupervised methods can flag anomalies without labels
2. Performance lags supervised approaches when labels exist
3. Contamination parameter critically impacts precision/recall balance
4. Fraud often blends into "normal" feature space—not always outliers
5. Hybrid supervised+unsupervised approaches offer the best of both worlds

**When to Use KDD/Unsupervised Approaches:**
- ✅ New fraud patterns emerging (no historical labels)
- ✅ Exploring data before expensive labeling efforts
- ✅ Research and hypothesis generation
- ✅ Augmenting supervised models with anomaly features
- ❌ Production fraud detection with available labels (use supervised)
- ❌ High precision requirements (minimizing false alerts)

**Final Insight**: The 83 frauds correctly identified by Isolation Forest represent **early-stage discoveries**. In a real workflow, analysts would review these 83 cases, label the 285 flagged transactions, then train a supervised model on this labeled data—bootstrapping from unsupervised to supervised learning.

KDD's value lies not in matching supervised performance, but in **discovering the undiscovered**—a worthy goal when the alternative is complete ignorance.

## References

1. Credit Card Fraud Detection Dataset: [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
2. Fayyad, U., Piatetsky-Shapiro, G., & Smyth, P. (1996). "From Data Mining to Knowledge Discovery in Databases" - The seminal KDD paper
3. Liu, F. T., Ting, K. M., & Zhou, Z. H. (2008). "Isolation Forest" - Original Isolation Forest paper
4. Notebook implementation: [GitHub Repository](https://github.com/yourusername/DS-Methodologies)

---

*Full implementation with executed cells, confusion matrix analysis, and detailed code available in the accompanying Jupyter notebook.*
