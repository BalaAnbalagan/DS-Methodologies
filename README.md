# 🎓 Learn Data Science Methodologies with AI

> **Master CRISP-DM, KDD, and SEMMA through hands-on implementations with AI-assisted learning**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com)

---

## 🎯 What You'll Learn

This repository teaches you **three foundational data science methodologies** through complete, runnable projects:

✅ **Learn by doing** - Run real projects on Kaggle datasets
✅ **AI-powered learning** - Use ChatGPT/Claude to critique and improve your work
✅ **Video-tutorial ready** - Perfect structure for creating teaching content
✅ **Clear explanations** - Accessible for learners at all levels

**Perfect for**: Students, educators, aspiring data scientists, content creators

---

## 🚀 Start Learning (No Setup Required!)

**Click any badge to open the notebook in Google Colab:**

### 1️⃣ CRISP-DM: Predicting Customer Churn
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BalaAnbalagan/DS-Methodologies/blob/main/crisp_dm_telco_churn/notebooks/crisp_dm_telco_churn.ipynb)

**Learn**: Business-driven ML, cost-benefit analysis, SHAP explainability, production deployment
**Dataset**: [7K telecom customers](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
**Question**: *Which customers will leave?*

📂 [View Project Folder](crisp_dm_telco_churn/) | 📄 [Medium Article](crisp_dm_telco_churn/medium_article.md) | 🎥 [YouTube Script](crisp_dm_telco_churn/youtube_script.md)

---

### 2️⃣ KDD: Detecting Credit Card Fraud
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BalaAnbalagan/DS-Methodologies/blob/main/kdd_credit_fraud/notebooks/kdd_credit_card_fraud.ipynb)

**Learn**: Anomaly detection, handling 579:1 imbalance, cost-sensitive ML, real-time systems
**Dataset**: [284K transactions, 492 frauds](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
**Question**: *How to catch fraud in real-time?*

📂 [View Project Folder](kdd_credit_fraud/) | 📄 [Medium Article](kdd_credit_fraud/medium_article.md) | 🎥 [YouTube Script](kdd_credit_fraud/youtube_script.md)

---

### 3️⃣ SEMMA: Optimizing Marketing Campaigns
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BalaAnbalagan/DS-Methodologies/blob/main/semma_bank_marketing/notebooks/semma_bank_marketing.ipynb)

**Learn**: Feature engineering, rapid prototyping, campaign ROI, batch scoring
**Dataset**: [41K bank contacts](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset)
**Question**: *Who should we target next?*

📂 [View Project Folder](semma_bank_marketing/) | 📄 [Medium Article](semma_bank_marketing/medium_article.md) | 🎥 [YouTube Script](semma_bank_marketing/youtube_script.md)

---

## 🤖 The AI-Assisted Learning Method

### How It Works:

```
1. Run Notebook → 2. Understand Results → 3. Ask AI to Critique
          ↑                                           ↓
5. Deepen Understanding ← 4. Apply Improvements ←────┘
```

### Example Workflow:

**Step 1**: Open notebook in Colab, run a phase (e.g., "Data Preparation")

**Step 2**: Use our critique prompts with ChatGPT/Claude:
```
You are a world-renowned data science expert.
Critique my Data Preparation phase with 10-15 improvements.
Focus on: correctness, depth, business value, clarity.

[Paste your notebook section here]
```

**Step 3**: AI suggests improvements like:
- "Add feature correlation analysis before modeling"
- "Consider outlier detection for MonthlyCharges"
- "Document your imputation strategy for missing values"

**Step 4**: Apply changes, see better results, understand WHY

**All critique prompts included** in each project's `prompts/` folder!

---

## 📹 Perfect for Video Tutorials

Each project includes:

✅ **Pre-written YouTube scripts** (8-12 min with timestamps)
✅ **30+ professional visualizations** (ready to record)
✅ **Clear learning structure** (Goal → Code → Output → Insight)
✅ **Real-world business problems** (engaging narratives)

**Use these to**:
- Create your own data science tutorials
- Teach students step-by-step
- Build a YouTube/TikTok channel
- Explain concepts to colleagues

---

## 💻 Local Setup (Optional)

**Prefer running locally?**

```bash
# Clone repository
git clone https://github.com/BalaAnbalagan/DS-Methodologies.git
cd DS-Methodologies

# Install dependencies
pip install -r requirements.txt

# Download datasets (need Kaggle API)
# See detailed instructions in QUICK_START.md

# Launch Jupyter
jupyter notebook
```

📖 **Full setup guide**: [QUICK_START.md](QUICK_START.md)

---

## 📂 What's Inside Each Project

```
📁 crisp_dm_telco_churn/
├── 📓 notebooks/
│   └── crisp_dm_telco_churn.ipynb    ← 🚀 Open in Colab!
├── 🤖 prompts/                        ← AI critique templates
│   ├── business_understanding.md
│   ├── data_understanding.md
│   ├── data_preparation.md
│   ├── modeling.md
│   ├── evaluation.md
│   └── deployment.md
├── 🚀 app/                            ← FastAPI deployment
├── 📄 medium_article.md               ← Ready to publish
└── 🎥 youtube_script.md               ← Video walkthrough
```

*Same structure for KDD and SEMMA projects!*

---

## 🎓 Learning Outcomes

After completing these projects, you'll understand:

**Technical Skills**:
- Structuring end-to-end DS projects
- 15 ML algorithms (LogReg, RF, XGBoost, LightGBM, IsolationForest...)
- Handling real challenges (missing data, class imbalance, feature engineering)
- Model explainability with SHAP
- Production deployment with FastAPI + Docker

**Methodological Knowledge**:
- When to use CRISP-DM vs KDD vs SEMMA
- How each phase connects
- Business-driven vs research-driven approaches

**AI Collaboration**:
- How to use ChatGPT/Claude effectively
- Asking the right critique questions
- Iterative improvement cycles
- Learning faster with AI assistance

---

## 🌟 Why This Approach Works

**Traditional Learning**:
Read docs → Try to apply → Get stuck → Google errors → Repeat

**AI-Assisted Learning**:
Run code → Understand results → Ask AI expert questions → Apply improvements → Master concepts

**Result**: Learn faster, deeper, with personalized guidance

---

## 📖 Additional Resources

- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Detailed project breakdown
- **[QUICK_START.md](QUICK_START.md)** - 15-minute setup guide
- **[README_COMPREHENSIVE.md](README_COMPREHENSIVE.md)** - Full documentation

---

## 🤝 Contribute

Help improve this learning resource:
- 🐛 Report errors
- 💡 Suggest improvements
- 🎥 Share video tutorials you create
- 🌍 Translate to other languages

**Open an issue**: https://github.com/BalaAnbalagan/DS-Methodologies/issues

---

## ⭐ Star This Repo

If this helped you learn, give it a ⭐! It helps others discover this resource.

---

## 📜 License

MIT License - Free for education, portfolios, teaching, commercial use

---

## 🚀 Ready to Learn?

**Pick a project above and click "Open in Colab"** to start your data science journey!

**Questions?** Check the critique prompts - they teach you how to ask AI the right questions.

---

*Made with ❤️ for the data science learning community*
*Created with Claude Code to democratize DS education*

**Happy Learning!** 🎓📊🚀
