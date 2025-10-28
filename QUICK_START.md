# ⚡ Quick Start Guide

Get up and running with your DS Methodologies Portfolio in 15 minutes!

---

## 📥 Step 1: Install Dependencies (5 minutes)

```bash
# Navigate to project root
cd /Users/banbalagan/Projects/DS-Methodologies

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

---

## 📦 Step 2: Download Datasets (5 minutes)

### Option A: Using Kaggle API (Recommended)

```bash
# Install Kaggle CLI
pip install kaggle

# Setup Kaggle credentials
# 1. Go to https://www.kaggle.com/account
# 2. Scroll to "API" section and click "Create New API Token"
# 3. Download kaggle.json
# 4. Move it to ~/.kaggle/

mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Download datasets
cd crisp_dm_telco_churn/data/raw
kaggle datasets download -d blastchar/telco-customer-churn
unzip telco-customer-churn.zip && rm telco-customer-churn.zip

cd ../../kdd_credit_fraud/data/raw
kaggle datasets download -d mlg-ulb/creditcardfraud
unzip creditcardfraud.zip && rm creditcardfraud.zip

cd ../../semma_bank_marketing/data/raw
kaggle datasets download -d janiobachmann/bank-marketing-dataset
unzip bank-marketing-dataset.zip && rm bank-marketing-dataset.zip

cd ../../..
```

### Option B: Manual Download

1. **Telco Churn**: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
   - Save as: `crisp_dm_telco_churn/data/raw/Telco-Customer-Churn.csv`

2. **Credit Fraud**: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
   - Save as: `kdd_credit_fraud/data/raw/creditcard.csv`

3. **Bank Marketing**: https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset
   - Save as: `semma_bank_marketing/data/raw/bank-additional-full.csv`

---

## 🚀 Step 3: Run Your First Notebook (5 minutes)

```bash
# Start Jupyter
jupyter notebook

# Open one of these notebooks:
# 1. crisp_dm_telco_churn/notebooks/crisp_dm_telco_churn.ipynb
# 2. kdd_credit_fraud/notebooks/kdd_credit_card_fraud.ipynb
# 3. semma_bank_marketing/notebooks/semma_bank_marketing.ipynb

# Run all cells (Kernel → Restart & Run All)
```

### What to Expect:

**CRISP-DM (Telco Churn)** - ~3-5 minutes runtime
- ✅ EDA with correlation heatmaps
- ✅ 4 models trained (LogReg, RF, XGBoost, LightGBM)
- ✅ SHAP explanations
- ✅ Business ROI analysis
- ✅ Model saved to `app/artifacts/`

**KDD (Credit Fraud)** - ~2-4 minutes runtime
- ✅ Extreme imbalance handling
- ✅ 6 anomaly detection models
- ✅ Cost-sensitive threshold optimization
- ✅ Temporal analysis
- ✅ Model saved to `app/artifacts/`

**SEMMA (Bank Marketing)** - ~3-5 minutes runtime
- ✅ Strategic sampling
- ✅ Feature engineering
- ✅ 5 model comparison
- ✅ Campaign efficiency metrics
- ✅ Model saved to `app/artifacts/`

---

## 🎯 Quick Test: Deploy an API

```bash
# After running CRISP-DM notebook (generates model artifacts)
cd crisp_dm_telco_churn/app

# Install deployment dependencies
pip install -r requirements.txt

# Start the API
python main.py
```

### Test the API:

Open browser: http://localhost:8000/docs

Or use curl:
```bash
curl -X POST "http://localhost:8000/score" \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 80.65,
    "TotalCharges": 1020.5
  }'
```

**Expected Response:**
```json
{
  "churn_probability": 0.6234,
  "churn_risk": "high"
}
```

---

## 📝 Quick Checklist

After following this guide, you should have:

- [ ] Virtual environment created and activated
- [ ] All Python dependencies installed
- [ ] Three datasets downloaded to correct locations
- [ ] At least one notebook executed successfully
- [ ] Model artifacts generated in `app/artifacts/`
- [ ] FastAPI service tested and working

---

## 🐛 Common Issues

### ❌ ModuleNotFoundError
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt
```

### ❌ FileNotFoundError: Dataset not found
```bash
# Solution: Verify file paths
ls crisp_dm_telco_churn/data/raw/
# Should show: Telco-Customer-Churn.csv
```

### ❌ Kernel dies while training
```bash
# Solution: Reduce model complexity or use sample data
# Edit notebook: train_sample = train.sample(frac=0.1)
```

### ❌ Port 8000 already in use
```bash
# Solution: Use different port
uvicorn main:app --port 8001
```

---

## 🎓 What's Next?

1. **Execute Critique Process**
   - Review `prompts/` files in each project
   - Use GPT-4/Claude for expert feedback
   - Document improvements

2. **Complete All Three Projects**
   - Run all notebooks
   - Compare methodologies
   - Generate all artifacts

3. **Polish Deliverables**
   - Update Medium articles with charts
   - Record YouTube walkthroughs
   - Create presentation slides

4. **Deploy to Cloud** (Optional)
   - Heroku: Easy deployment
   - AWS: Lambda + API Gateway
   - Google Cloud: Cloud Run

---

## 📚 Key Files to Review

- **README_COMPREHENSIVE.md** - Full documentation
- **PROJECT_SUMMARY.md** - What's been built
- **QUICK_START.md** - This file
- **requirements.txt** - All dependencies

---

## 🎉 You're Ready!

You now have a complete data science portfolio demonstrating:
- ✅ Three industry-standard methodologies
- ✅ Real-world datasets and problems
- ✅ Production-quality code
- ✅ Deployment-ready APIs

**Time to shine in your assignment! 🌟**

---

*Need help? Review the comprehensive documentation in README_COMPREHENSIVE.md*
