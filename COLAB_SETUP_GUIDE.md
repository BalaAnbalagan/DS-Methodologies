# 🚀 Google Colab Setup Guide

> **Run these notebooks in Colab with zero local setup**

This guide shows you how to run the DS Methodologies notebooks in Google Colab, including dataset loading options.

---

## ⚡ Quick Start (2 minutes)

### Step 1: Open Notebook in Colab

Click any "Open in Colab" badge from the README:

- [CRISP-DM Notebook](https://colab.research.google.com/github/BalaAnbalagan/DS-Methodologies/blob/main/crisp_dm_telco_churn/notebooks/crisp_dm_telco_churn.ipynb)
- [KDD Notebook](https://colab.research.google.com/github/BalaAnbalagan/DS-Methodologies/blob/main/kdd_credit_fraud/notebooks/kdd_credit_card_fraud.ipynb)
- [SEMMA Notebook](https://colab.research.google.com/github/BalaAnbalagan/DS-Methodologies/blob/main/semma_bank_marketing/notebooks/semma_bank_marketing.ipynb)

### Step 2: Run the Setup Cell

Each notebook has a **"Colab Setup"** cell at the top. Just run it!

```python
# This cell handles everything automatically
```

### Step 3: Load Dataset

Choose your preferred method (all 3 options are in the notebook):
- **Option A**: Upload CSV from your computer (easiest)
- **Option B**: Download from Kaggle API
- **Option C**: Load from Google Drive

### Step 4: Run the Rest!

Execute cells in order. That's it!

---

## 📂 Dataset Loading Options

### Option A: Direct Upload (Easiest for First Time)

**Steps:**
1. Download dataset from Kaggle to your computer:
   - [Telco Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (12 MB)
   - [Credit Fraud](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) (150 MB)
   - [Bank Marketing](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset) (5 MB)

2. Run this cell in Colab:
```python
from google.colab import files
import pandas as pd

# Upload file from your computer
uploaded = files.upload()

# Get filename (usually only one file)
filename = list(uploaded.keys())[0]
data = pd.read_csv(filename)
print(f"✅ Loaded {len(data):,} rows from {filename}")
```

3. Continue with the notebook!

**Pros:** Simple, no API keys needed
**Cons:** Need to re-upload if session expires

---

### Option B: Kaggle API (Best for Repeated Use)

**One-Time Setup:**

1. **Get Kaggle API Token:**
   - Go to https://www.kaggle.com/account
   - Scroll to "API" section
   - Click "Create New API Token"
   - This downloads `kaggle.json`

2. **Upload to Colab:**
```python
from google.colab import files

# Upload your kaggle.json
files.upload()  # Select kaggle.json from your computer

# Setup Kaggle credentials
!mkdir -p ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
print("✅ Kaggle API configured!")
```

3. **Download Dataset:**

**For CRISP-DM (Telco Churn):**
```python
!kaggle datasets download -d blastchar/telco-customer-churn
!unzip -q telco-customer-churn.zip
import pandas as pd
data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(f"✅ Loaded {len(data):,} customers")
```

**For KDD (Credit Fraud):**
```python
!kaggle datasets download -d mlg-ulb/creditcardfraud
!unzip -q creditcardfraud.zip
import pandas as pd
data = pd.read_csv('creditcard.csv')
print(f"✅ Loaded {len(data):,} transactions")
```

**For SEMMA (Bank Marketing):**
```python
!kaggle datasets download -d janiobachmann/bank-marketing-dataset
!unzip -q bank-marketing-dataset.zip
import pandas as pd
data = pd.read_csv('bank-additional-full.csv', sep=';')
print(f"✅ Loaded {len(data):,} contacts")
```

**Pros:** Automated, reproducible, one-click after setup
**Cons:** Requires Kaggle account and API token

---

### Option C: Google Drive (Best for Long Sessions)

**One-Time Setup:**

1. **Upload Dataset to Google Drive:**
   - Create folder: `My Drive/DS-Methodologies/data/`
   - Upload CSV files there

2. **Mount Drive in Colab:**
```python
from google.colab import drive
drive.mount('/content/drive')
```

3. **Load Dataset:**
```python
import pandas as pd

# Update path to match your Drive structure
data_path = '/content/drive/My Drive/DS-Methodologies/data/Telco-Customer-Churn.csv'
data = pd.read_csv(data_path)
print(f"✅ Loaded {len(data):,} rows from Drive")
```

**Pros:** Persists across sessions, no re-upload needed
**Cons:** Requires Drive organization

---

## 🔧 Installing Required Packages

### Automatic Installation (Handled by Notebooks)

Each notebook checks if you're in Colab and auto-installs:

```python
import sys
if 'google.colab' in sys.modules:
    print("📦 Installing Colab-specific packages...")
    !pip install -q xgboost lightgbm shap
    print("✅ Installation complete!")
```

### Manual Installation (If Needed)

```python
!pip install pandas numpy matplotlib seaborn scikit-learn
!pip install xgboost lightgbm
!pip install shap  # For model explainability
```

---

## 🗂️ Handling File Paths in Colab

### Local vs Colab Path Differences

**Local Jupyter:**
```python
data = pd.read_csv('../data/raw/dataset.csv')  # Relative path
```

**Google Colab:**
```python
# Files are in /content/ directory
data = pd.read_csv('/content/dataset.csv')  # Absolute path
```

### Auto-Detection (Built into Notebooks)

```python
import sys
from pathlib import Path

if 'google.colab' in sys.modules:
    # Running in Colab
    data_path = '/content/Telco-Customer-Churn.csv'
else:
    # Running locally
    data_path = Path('../data/raw/Telco-Customer-Churn.csv')

data = pd.read_csv(data_path)
```

---

## 💾 Saving Outputs from Colab

### Save Trained Models

```python
from google.colab import files
from joblib import dump

# Save model
dump(model, 'my_model.joblib')

# Download to your computer
files.download('my_model.joblib')
```

### Save to Google Drive

```python
# Mount Drive (if not already)
from google.colab import drive
drive.mount('/content/drive')

# Save model
from joblib import dump
dump(model, '/content/drive/My Drive/DS-Methodologies/models/my_model.joblib')
print("✅ Model saved to Google Drive!")
```

### Save Visualizations

```python
import matplotlib.pyplot as plt

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(data)
plt.title('My Analysis')

# Save to file
plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')

# Download
from google.colab import files
files.download('my_plot.png')
```

---

## ⚡ Colab Pro Tips

### 1. **Use GPU for Faster Training (Optional)**

```python
# Enable GPU: Runtime → Change runtime type → GPU

# Check GPU availability
import torch
if torch.cuda.is_available():
    print("✅ GPU is available!")
    print(f"GPU: {torch.cuda.get_device_name(0)}")
else:
    print("ℹ️  Using CPU (GPU not needed for these projects)")
```

**Note:** GPU isn't necessary for these projects, but speeds up XGBoost/LightGBM slightly.

### 2. **Keep Session Alive**

Colab disconnects after ~90 minutes of inactivity. To prevent:

1. **Browser Console Trick:**
```javascript
// Paste in browser console (F12):
function KeepClicking(){
  console.log("Keeping alive...");
  document.querySelector("colab-connect-button").click();
}
setInterval(KeepClicking, 60000);
```

2. **Or just save frequently:**
```python
# Download notebook often: File → Download → Download .ipynb
```

### 3. **Manage Memory**

If you run out of memory:

```python
# Clear variables
del large_dataframe
import gc
gc.collect()

# Check memory usage
!free -h

# Restart runtime if needed: Runtime → Restart runtime
```

### 4. **Version Control**

```python
# Save to GitHub from Colab
# File → Save a copy in GitHub

# Or download and commit locally
# File → Download → Download .ipynb
```

---

## 🐛 Common Issues & Solutions

### Issue 1: "FileNotFoundError"

**Problem:** Dataset not found
**Solution:**
```python
# Check current directory
!pwd
!ls -la

# List uploaded files
!ls /content/

# Verify path
import os
print("Files:", os.listdir('/content/'))
```

### Issue 2: "ModuleNotFoundError: No module named 'xgboost'"

**Problem:** Package not installed
**Solution:**
```python
!pip install xgboost lightgbm shap
```

### Issue 3: "Session Crashed" / Out of Memory

**Problem:** Dataset too large or memory leak
**Solution:**
```python
# Use data sampling for exploration
data_sample = data.sample(frac=0.1, random_state=42)

# Or upgrade to Colab Pro for more RAM
# https://colab.research.google.com/signup
```

### Issue 4: "Drive Mount Failed"

**Problem:** Permission issues
**Solution:**
```python
# Re-mount and authenticate
from google.colab import drive
drive.flush_and_unmount()
drive.mount('/content/drive', force_remount=True)
```

### Issue 5: Slow Downloads from Kaggle

**Problem:** Large dataset + slow connection
**Solution:**
```python
# Download locally, then upload to Colab
# Or use Google Drive method for persistence
```

---

## 📊 Colab vs Local Development

| Feature | Colab | Local Jupyter |
|---------|-------|---------------|
| **Setup** | ✅ None (browser-based) | ❌ Need Python, packages |
| **GPU Access** | ✅ Free GPU available | ❌ Need own hardware |
| **Session** | ⚠️  Disconnects after 90 min | ✅ Persistent |
| **Storage** | ⚠️  15 GB (Drive) | ✅ Your disk space |
| **Internet** | ❌ Required | ✅ Optional |
| **Speed** | ⚠️  Depends on connection | ✅ Local |
| **Cost** | ✅ Free (Pro: $10/mo) | ✅ Free (after setup) |

**Recommendation:**
- **Start with Colab** (zero setup, great for learning)
- **Switch to local** when you need longer sessions or offline work

---

## 🎓 Workflow Recommendations

### For First-Time Learners:

1. ✅ Use Colab with **Option A: Direct Upload**
2. ✅ Focus on learning, not setup
3. ✅ Download notebook + save work frequently

### For Repeated Use:

1. ✅ Set up Kaggle API (Option B)
2. ✅ Save models to Google Drive
3. ✅ Keep `kaggle.json` in Drive for easy re-upload

### For Serious Projects:

1. ✅ Consider Colab Pro ($10/mo) for:
   - Longer sessions (24h vs 12h)
   - More RAM (25GB vs 12GB)
   - Faster GPUs
2. ✅ Or switch to local development

---

## 📖 Additional Colab Resources

### Official Docs:
- **Colab Overview**: https://colab.research.google.com/notebooks/intro.ipynb
- **Colab FAQ**: https://research.google.com/colaboratory/faq.html

### Keyboard Shortcuts:
- **Run cell**: `Ctrl+Enter` (Windows) / `Cmd+Enter` (Mac)
- **Run cell & move**: `Shift+Enter`
- **Add cell below**: `Ctrl+M B` / `Cmd+M B`
- **Comment code**: `Ctrl+/` / `Cmd+/`

### Useful Colab Features:
- **Table of Contents**: Click folder icon (left sidebar)
- **Find & Replace**: `Ctrl+H` / `Cmd+H`
- **Code Snippets**: Click `<>` icon (left sidebar)
- **Variable Inspector**: Click `{}` icon (right sidebar)

---

## ✅ Checklist Before Starting

- [ ] Notebook opened in Colab
- [ ] Runtime type set (CPU is fine)
- [ ] Dataset loaded (one of 3 methods)
- [ ] Required packages installed
- [ ] First cell executed successfully
- [ ] Ready to learn! 🚀

---

## 🎉 You're Ready!

Open a notebook, load the dataset, and start learning!

**Questions?**
- Check [HOW_TO_LEARN_WITH_AI.md](HOW_TO_LEARN_WITH_AI.md) for learning tips
- Open an issue on GitHub
- Ask in the 🤖 Learning Checkpoints within notebooks

---

**Happy Coding!** 🚀📊🎓
