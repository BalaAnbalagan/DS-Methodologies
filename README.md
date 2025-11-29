# Data Science Methodologies Portfolio

**Three complete credit card fraud detection projects demonstrating CRISP-DM, SEMMA, and KDD methodologies with executed Jupyter notebooks, comprehensive Medium articles, and detailed expert critiques.**

## Video Presentation

[![Data Science Methodologies Portfolio](https://img.youtube.com/vi/af_ZoFPcYUk/0.jpg)](https://youtu.be/af_ZoFPcYUk)

[Watch the full presentation on YouTube](https://youtu.be/af_ZoFPcYUk)

## Overview

This portfolio showcases three fundamental data mining methodologies applied to the same problem domain—credit card fraud detection—allowing direct comparison of approaches, trade-offs, and results. Each project includes:

- **Executed Jupyter Notebooks** with full outputs, metrics, and visualizations
- **Publication-Ready Medium Articles** (8-12KB each) with detailed analysis
- **Expert Critiques** embedded throughout notebooks
- **Real Metrics** from 284,807 credit card transactions (492 frauds, 0.17% rate)

## Performance Comparison

| Methodology | Approach | Precision | Recall | F1 Score | ROC AUC | Best For |
|------------|----------|-----------|--------|----------|---------|----------|
| **CRISP-DM** | Supervised (Random Forest) | **96.52%** | 75.00% | 84.41% | 92.46% | Production deployment, business alignment |
| **SEMMA** | Supervised (Random Forest) | 93.85% | **82.43%** | **87.77%** | **97.79%** | Rapid prototyping, iterative refinement |
| **KDD** | Unsupervised (Isolation Forest) | 29.12% | 16.87% | 21.36% | N/A | Exploratory analysis, no labels available |

## Projects

### 1. CRISP-DM: Business-Driven Fraud Detection

**Methodology Focus**: Cross-Industry Standard Process for Data Mining emphasizes business understanding, deployment planning, and iterative refinement through six phases.

**Implementation**:
- Full dataset (284,807 transactions)
- Two models: Logistic Regression (baseline) + Random Forest (advanced)
- Hour-based feature engineering for temporal patterns
- Business cost-benefit analysis

**Key Results**:
- Random Forest: **96.52% precision, 75% recall, 84.41% F1**
- Logistic Regression: 84.76% precision, 60.14% recall, 70.36% F1
- **96.5% precision** = only 4 false positives per 111 detected frauds
- Estimated value: **$11,475 saved** on test set alone

**Files**:
- Notebook: [`CRISP_DM/crisp_dm_walmart_sales.ipynb`](CRISP_DM/crisp_dm_walmart_sales.ipynb) (77KB with outputs)
- Medium Article: [📝 Published on Medium](https://medium.com/@balamuralikrishnan.anbalagan/battling-credit-card-fraud-with-crisp-dm-a-data-driven-approach-28f492e3646f)
- Technical Report: [`CRISP_DM/report.md`](CRISP_DM/report.md)

**When to Use CRISP-DM**:
- ✅ Production deployment required
- ✅ Stakeholder alignment critical
- ✅ Business ROI must be quantified
- ✅ Deployment monitoring and maintenance planned

---

### 2. SEMMA: Rapid Exploration and Modeling

**Methodology Focus**: Sample, Explore, Modify, Model, Assess—SAS Institute's framework for rapid prototyping and iterative experimentation.

**Implementation**:
- Strategic sampling (49,492 transactions: 49K legitimate + all 492 frauds)
- Exploratory visualizations (amount distribution, correlation heatmap)
- Z-score standardization
- Random Forest with 100 estimators

**Key Results**:
- **97.79% ROC AUC** - highest class separation across all methodologies
- **93.85% precision, 82.43% recall, 87.77% F1** - best F1 score
- 6x computational speedup via sampling
- ~$11,475 net value on test set

**Files**:
- Notebook: [`SEMMA/semma_student_performance.ipynb`](SEMMA/semma_student_performance.ipynb) (86KB with outputs)
- Medium Article: [📝 Published on Medium](https://medium.com/@balamuralikrishnan.anbalagan/semma-methodology-in-action-rapid-fraud-detection-prototyping-7d2ca8277048)
- Technical Report: [`SEMMA/report.md`](SEMMA/report.md)

**When to Use SEMMA**:
- ✅ Rapid proof-of-concept needed
- ✅ Iterative experimentation preferred
- ✅ Business context already understood
- ✅ Technical exploration drives value

---

### 3. KDD: Unsupervised Anomaly Detection

**Methodology Focus**: Knowledge Discovery in Databases emphasizes scientific rigor and unsupervised learning for scenarios where labels are scarce or unreliable.

**Implementation**:
- Full dataset (all 284,807 transactions)
- **No labels used during training** (unsupervised approach)
- Isolation Forest with contamination=0.001
- Post-hoc evaluation against true fraud labels

**Key Results**:
- **29.12% precision, 16.87% recall** - demonstrates unsupervised limitations
- Caught 83 of 492 frauds (17%) without any labeled training data
- 202 false positives (71% false alert rate)
- **Key Insight**: Unsupervised methods sacrifice performance for generality

**Files**:
- Notebook: [`KDD/kdd_credit_fraud.ipynb`](KDD/kdd_credit_fraud.ipynb) (4.4KB with outputs)
- Medium Article: [📝 Published on Medium](https://medium.com/@balamuralikrishnan.anbalagan/kdd-process-unsupervised-fraud-detection-with-isolation-forest-815953becce1)
- Technical Report: [`KDD/report.md`](KDD/report.md)

**When to Use KDD**:
- ✅ No labeled data available (new fraud patterns)
- ✅ Labels potentially contaminated/unreliable
- ✅ Exploratory research phase
- ✅ Bootstrapping labeled dataset from scratch
- ❌ Production deployment (use supervised methods)

---

## Methodology Comparison

| Aspect | CRISP-DM | SEMMA | KDD |
|--------|----------|-------|-----|
| **Focus** | Business value | Technical experimentation | Knowledge discovery |
| **Phases** | 6 (Business → Deployment) | 5 (Sample → Assess) | 5 (Selection → Interpretation) |
| **Iteration** | Explicit loops | Core philosophy | Less emphasized |
| **Supervision** | Supervised | Supervised | Unsupervised |
| **Deployment** | Central concern | Not emphasized | Not emphasized |
| **Strengths** | Comprehensive, production-ready | Fast, iterative | No labels required |
| **Weaknesses** | Time-consuming | Limited business context | Lower performance |
| **Best Dataset Size** | Any | Small-Medium | Large |
| **Evaluation Metrics** | Business + Technical | Technical | Exploratory |

## Dataset Information

**Credit Card Fraud Detection Dataset**
- Source: [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Transactions: 284,807 (European cardholders, September 2013)
- Features: 30 (V1-V28 from PCA + Time + Amount)
- Fraud Rate: 0.17% (492 fraud cases)
- Class Imbalance: 579:1 (legitimate : fraud)
- Size: 144MB

**Challenge**: Extreme class imbalance makes accuracy meaningless—precision, recall, F1, and ROC AUC are critical metrics.

## Key Findings

### 1. Supervised vs. Unsupervised Trade-off
- Supervised methods (CRISP-DM, SEMMA) achieve 93-96% precision
- Unsupervised methods (KDD) achieve 29% precision
- **Gap**: ~67 percentage points in precision
- **Use Case**: Unsupervised shines when labels unavailable, not when labels exist

### 2. Sampling Impact
- SEMMA's 6x sampling speedup had minimal performance cost
- **97.79% ROC AUC** (sampled) vs. 92.46% (full data)
- Strategic fraud retention (all 492 cases) was key

### 3. Model Selection
- Random Forest outperformed Logistic Regression across all metrics
- Ensemble methods handle nonlinear V1-V28 interactions better
- **Precision improvement**: 84.76% (LR) → 96.52% (RF)

### 4. Business Value
- Both supervised approaches deliver ~$11,500 net value on small test set
- Scaled to millions of transactions: **millions in annual savings**
- False positive rate matters: CRISP-DM's 4 FPs vs. SEMMA's 9 FPs

### 5. Methodology Maturity
- **Production**: CRISP-DM (deployment planning built-in)
- **Prototyping**: SEMMA (fastest time-to-insight)
- **Research**: KDD (exploratory, hypothesis-driven)

## Getting Started

### Prerequisites
```bash
Python 3.9+
pandas, numpy, scikit-learn, matplotlib, seaborn
jupyter notebook
```

### Installation
```bash
git clone https://github.com/BalaAnbalagan/DS-Methodologies.git
cd DS-Methodologies
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running Notebooks

**Option 1: Local Jupyter**
```bash
# CRISP-DM
cd CRISP_DM
jupyter notebook crisp_dm_walmart_sales.ipynb

# SEMMA
cd ../SEMMA
jupyter notebook semma_student_performance.ipynb

# KDD
cd ../KDD
jupyter notebook kdd_credit_fraud.ipynb
```

**Option 2: Google Colab** (No installation required!)

Open directly in Colab:
- [CRISP-DM Notebook](https://colab.research.google.com/github/BalaAnbalagan/DS-Methodologies/blob/main/CRISP_DM/crisp_dm_walmart_sales.ipynb)
- [SEMMA Notebook](https://colab.research.google.com/github/BalaAnbalagan/DS-Methodologies/blob/main/SEMMA/semma_student_performance.ipynb)
- [KDD Notebook](https://colab.research.google.com/github/BalaAnbalagan/DS-Methodologies/blob/main/KDD/kdd_credit_fraud.ipynb)

**Note for Colab users**: You'll need to upload the dataset to your Colab session or mount Google Drive.

### Dataset Setup
The 144MB `creditcard.csv` dataset is **not included in GitHub** (exceeds 100MB limit). Download it:

1. **Download**: Get from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) (requires free account)
2. **For Local Jupyter**: Place in `{CRISP_DM,SEMMA,KDD}/dataset/creditcard.csv`
3. **For Google Colab**:
   - Upload to Colab session: Use Colab's file upload
   - Or mount Google Drive and update paths in notebooks

## Project Structure
```
DS-Methodologies/
├── CRISP_DM/
│   ├── crisp_dm_walmart_sales.ipynb (77KB, executed)
│   ├── medium_draft.md (8.3KB, publication-ready)
│   ├── report.md (technical summary)
│   └── dataset/
│       └── creditcard.csv (144MB)
├── SEMMA/
│   ├── semma_student_performance.ipynb (86KB, executed)
│   ├── medium_draft.md (10KB, publication-ready)
│   ├── report.md
│   └── dataset/
│       └── creditcard.csv
├── KDD/
│   ├── kdd_credit_fraud.ipynb (4.4KB, executed)
│   ├── medium_draft.md (12KB, publication-ready)
│   ├── report.md
│   └── dataset/
│       └── creditcard.csv
├── README.md (this file)
└── requirements.txt
```

## Medium Article Highlights

Each Medium article (8-12KB) includes:
- **Methodology explanation** with phase-by-phase breakdown
- **Actual metrics** from executed notebooks
- **Confusion matrices** and performance analysis
- **Business cost-benefit calculations**
- **Expert critiques** identifying strengths/weaknesses
- **Comparison tables** across methodologies
- **Future improvements** and iteration recommendations
- **When-to-use guidance** for practitioners

Perfect for:
- Data science portfolios
- Medium.com publication
- Technical blog posts
- Methodology education

## Future Enhancements

### Model Improvements
- **Deep Learning**: Autoencoders for unsupervised feature learning
- **XGBoost/LightGBM**: Gradient boosting for better precision/recall
- **SMOTE**: Synthetic minority oversampling
- **Cost-Sensitive Learning**: Optimize for business costs, not statistical metrics

### Feature Engineering
- Temporal patterns (hour-of-day, day-of-week)
- Velocity features (transaction frequency)
- Amount binning and transformations
- Merchant category data (if available)

### Deployment
- Real-time scoring API (FastAPI)
- Model monitoring dashboards
- A/B testing framework
- Drift detection

## License

MIT License - See LICENSE file for details.

## References

1. Credit Card Fraud Detection Dataset: [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
2. CRISP-DM 1.0: Chapman et al. (2000). "CRISP-DM 1.0 Step-by-step data mining guide"
3. SEMMA: SAS Institute. "SEMMA Data Mining Methodology"
4. KDD: Fayyad, Piatetsky-Shapiro, Smyth (1996). "From Data Mining to Knowledge Discovery in Databases"
5. Isolation Forest: Liu, Ting, Zhou (2008). "Isolation Forest"

## Contact

Questions or feedback? Open an issue or reach out at **bala.anbalagan@sjsu.edu**

---

**Note**: All three projects use the same credit card fraud dataset to enable direct methodology comparison. In practice, CRISP-DM, SEMMA, and KDD would each shine on different problem types—this portfolio demonstrates their approaches, trade-offs, and when to use each.
