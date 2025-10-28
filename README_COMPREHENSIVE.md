# 🎓 Data Science Methodologies Portfolio

> **A comprehensive demonstration of three classic data science methodologies (CRISP-DM, KDD, SEMMA) applied to real-world Kaggle datasets with production-ready implementations.**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?logo=Jupyter)](https://jupyter.org/try)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Methodology Comparison](#methodology-comparison)
- [Projects](#projects)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Deliverables](#deliverables)
- [Critique Process](#critique-process)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This portfolio demonstrates mastery of three foundational data science methodologies through complete, production-ready implementations:

### **1. CRISP-DM** — Telco Customer Churn Prediction
- **Business Focus**: Reduce customer churn through predictive retention campaigns
- **Dataset**: [Telco Customer Churn (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Phases**: Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment
- **Models**: Logistic Regression, Random Forest, XGBoost, LightGBM
- **Key Feature**: Cost-benefit analysis with business ROI calculations

### **2. KDD** — Credit Card Fraud Detection
- **Business Focus**: Real-time anomaly detection for fraudulent transactions
- **Dataset**: [Credit Card Fraud Detection (Kaggle)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Phases**: Selection → Preprocessing → Transformation → Data Mining → Interpretation/Evaluation
- **Models**: Logistic Regression, Isolation Forest, Random Forest, XGBoost, Local Outlier Factor
- **Key Feature**: Cost-sensitive threshold optimization for extreme class imbalance (579:1)

### **3. SEMMA** — Bank Marketing Campaign Optimization
- **Business Focus**: Optimize term deposit campaign targeting
- **Dataset**: [Bank Marketing Dataset (Kaggle)](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset)
- **Phases**: Sample → Explore → Modify → Model → Assess
- **Models**: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost
- **Key Feature**: Feature engineering and campaign ROI analysis

---

## 🔍 Methodology Comparison

| Aspect | CRISP-DM | KDD | SEMMA |
|--------|----------|-----|-------|
| **Origin** | Industry consortium (1996) | Academic (Fayyad et al., 1996) | SAS Institute (1998) |
| **Focus** | Business-driven, iterative | Research-oriented, data-centric | Tool-agnostic, modeling focus |
| **Phases** | 6 phases (cyclic) | 5 phases (linear) | 5 phases (iterative) |
| **Best For** | Enterprise deployments | Knowledge discovery | Rapid prototyping |
| **Starting Point** | Business understanding | Data selection | Data sampling |
| **Our Implementation** | Churn prediction | Fraud detection | Marketing optimization |

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.9 or higher
- Jupyter Notebook or JupyterLab
- Kaggle account (for dataset download)
- Git
- Docker (optional, for deployment)

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/DS-Methodologies.git
cd DS-Methodologies
```

### Step 2: Create Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n ds-methodologies python=3.9
conda activate ds-methodologies
```

### Step 3: Install Dependencies

```bash
# Install all dependencies for notebooks
pip install -r requirements.txt

# Or install per-project deployment dependencies
cd crisp_dm_telco_churn/app
pip install -r requirements.txt
```

### Step 4: Setup Kaggle API

```bash
# Install Kaggle CLI
pip install kaggle

# Place your kaggle.json in ~/.kaggle/
mkdir -p ~/.kaggle
cp ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

### Step 5: Download Datasets

```bash
# Telco Churn
cd crisp_dm_telco_churn/data/raw
kaggle datasets download -d blastchar/telco-customer-churn
unzip telco-customer-churn.zip

# Credit Card Fraud
cd ../../kdd_credit_fraud/data/raw
kaggle datasets download -d mlg-ulb/creditcardfraud
unzip creditcardfraud.zip

# Bank Marketing
cd ../../semma_bank_marketing/data/raw
kaggle datasets download -d janiobachmann/bank-marketing-dataset
unzip bank-marketing-dataset.zip
```

---

## 📖 Usage Guide

### Running Notebooks

#### Option 1: Local Jupyter

```bash
jupyter notebook
# Navigate to project/notebooks/ and open the .ipynb file
```

#### Option 2: Google Colab

1. Upload the notebook to Google Drive
2. Open with Google Colab
3. Upload dataset to Colab session or mount Drive
4. Install dependencies:
   ```python
   !pip install -r requirements.txt
   ```

### Executing Critique Process

Each phase has a dedicated critique prompt file in `prompts/`:

```bash
# Example: Critique the Business Understanding phase
cat crisp_dm_telco_churn/prompts/business_understanding.md
```

**Two-Pass Critique Workflow**:

1. **Pass 1**: Complete the phase in the notebook
2. Use the critique prompt with GPT-4/Claude
3. Document feedback in the prompt file under "Pass 1"
4. Apply revisions to notebook
5. **Pass 2**: Re-submit for final review
6. Document final feedback and revisions

### Deployment

#### Local FastAPI Development

```bash
cd crisp_dm_telco_churn/app
python main.py
# API available at http://localhost:8000
# Docs at http://localhost:8000/docs
```

#### Docker Deployment

```bash
cd crisp_dm_telco_churn/app
docker build -t telco-churn-api .
docker run -p 8000:8000 telco-churn-api
```

---

## 🎭 Critique Process

### Critique Persona

```markdown
You are a world-renowned authority on [CRISP-DM/KDD/SEMMA].
You have authored multiple award-winning books and mentor
Fortune 500 data teams. Critique my [phase] section with
10–15 actionable improvements, focusing on methodological
rigor, completeness, and clarity.
```

### Evaluation Criteria

- ✅ **Completeness**: All methodology phases thoroughly implemented
- ✅ **Technical Accuracy**: Correct application of algorithms and metrics
- ✅ **Reproducibility**: Clear documentation and runnable code
- ✅ **Depth of Reflection**: Meaningful critique integration
- ✅ **Code Quality**: Clean, documented, production-ready code
- ✅ **Visual Clarity**: Informative, well-designed charts and tables
- ✅ **Professionalism**: Polished deliverables ready for presentation

---

## 📦 Deliverables

Each project includes:

1. **Jupyter Notebook** - Complete methodology walkthrough
2. **Medium Article** - Publication-ready narrative
3. **YouTube Script** - 8-12 minute video outline
4. **Critique Prompts** - Two-pass review logs
5. **FastAPI Service** - Production API
6. **Docker Configuration** - Containerized deployment
7. **Model Card** - Comprehensive model documentation

---

## 🙏 Acknowledgments

- **Datasets**: Kaggle community
- **Methodologies**: CRISP-DM consortium, Fayyad et al., SAS Institute
- **Tools**: Scikit-learn, XGBoost, LightGBM, SHAP, FastAPI communities

---

**⭐ If you find this portfolio helpful, please consider giving it a star!**

Happy Mining! 🎓📊🚀
