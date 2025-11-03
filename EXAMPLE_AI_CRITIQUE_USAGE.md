# 🤖 How to Use AI Critique API in Notebooks

This guide shows you how to automatically get ChatGPT critiques directly from your notebook cells.

---

## 🔧 Setup (One-Time)

### 1. Get OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy it (you'll need it below)

### 2. Set API Key as Environment Variable

**Option A: Using .env file (RECOMMENDED for local):**
```bash
# The .env file already exists in the project root with your API key
# Just install python-dotenv:
pip install python-dotenv

# The ai_critique_helper.py will automatically load from .env
# No manual export needed!
```

**Option B: In your terminal (temporary - for current session):**
```bash
export OPENAI_API_KEY="sk-your-key-here"
```

**Option C: In Colab (at start of notebook):**
```python
import os
os.environ['OPENAI_API_KEY'] = 'sk-your-key-here'
```

**Option D: Permanently in shell config:**
```bash
# Add to ~/.zshrc or ~/.bashrc
echo 'export OPENAI_API_KEY="sk-your-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### 3. Install Required Packages

```python
!pip install openai python-dotenv
```

---

## 📓 Usage in Notebook

### **Cell 1: Import the Helper**

```python
# At the top of your notebook
from ai_critique_helper import AICritiqueHelper

# Initialize (do this once)
ai = AICritiqueHelper(model="gpt-4")  # or "gpt-3.5-turbo" for faster/cheaper
```

---

### **Cell 2-5: Your Phase 1 Code (Business Understanding)**

```python
# Your actual CRISP-DM Phase 1 code
project_charter = {
    'stakeholders': ['VP Customer Success', 'Retention Analytics Lead'],
    'business_objectives': ['Quantify churn risk', 'Prioritize outreach campaigns'],
    'constraints': ['Data refresh monthly', 'Model must be explainable'],
    'success_criteria': 'Recall >= 0.80',
    'milestones': {
        'kickoff': 'Define outcomes and KPIs',
        'baseline_model': 'First iteration with classical ML',
        'deployment_candidate': 'Pipeline validated in UAT'
    }
}

print("Project Charter:")
print(project_charter)
```

---

### **Cell 6: Get AI Critique (Automatic!)**

```python
# Capture the code you just wrote
code = """
project_charter = {
    'stakeholders': ['VP Customer Success', 'Retention Analytics Lead'],
    'business_objectives': ['Quantify churn risk', 'Prioritize outreach campaigns'],
    'constraints': ['Data refresh monthly', 'Model must be explainable'],
    'success_criteria': 'Recall >= 0.80',
    'milestones': {
        'kickoff': 'Define outcomes and KPIs',
        'baseline_model': 'First iteration with classical ML',
        'deployment_candidate': 'Pipeline validated in UAT'
    }
}
"""

# Capture the output
output = str(project_charter)

# 🤖 GET CRITIQUE FROM CHATGPT (API CALL)
critique_round1 = ai.critique_phase(
    methodology="CRISP-DM",
    phase_name="Business Understanding",
    code=code,
    output=output,
    save_to_file=True  # Automatically saves to critiques/ folder
)
```

**What happens:**
1. ✅ Sends code + output to ChatGPT API
2. ✅ ChatGPT acts as "world-renowned CRISP-DM expert"
3. ✅ Returns structured critique with:
   - What you did well
   - Critical issues
   - 5-10 specific improvements
   - Best practices
   - Ready to proceed? Yes/No
4. ✅ Displays beautifully formatted in notebook
5. ✅ Saves to `critiques/business_understanding/critique_TIMESTAMP.md`

---

### **Cell 7: Read the Critique & Make Improvements**

```python
# Read the critique above and improve your code
# Example: Add missing stakeholders, define LTV, add risk assessment

# IMPROVED VERSION
project_charter_v2 = {
    'stakeholders': [
        'VP Customer Success',
        'Retention Analytics Lead',
        'Data Engineering',
        'CFO',  # Added - cares about ROI
        'Legal'  # Added - regulatory compliance
    ],
    'business_objectives': [
        'Quantify churn risk',
        'Prioritize outreach campaigns',
        'Calculate customer LTV',  # Added
        'Measure campaign ROI'  # Added
    ],
    'constraints': [
        'Data refresh monthly',
        'Model must be explainable',
        'GDPR compliance required',  # Added
        'Max inference latency: 150ms'  # Added
    ],
    'success_criteria': {
        'recall': 0.80,
        'precision': 0.55,  # Added
        'ROI': '> 100%'  # Added
    },
    'milestones': {
        'kickoff': 'Define outcomes and KPIs',
        'data_audit': 'Validate data quality',  # Added
        'baseline_model': 'First iteration with classical ML',
        'deployment_candidate': 'Pipeline validated in UAT'
    },
    'risks': [  # Added entire section
        'Delayed billing feeds',
        'Call center capacity limits',
        'Customer privacy concerns'
    ]
}

print("Improved Project Charter:")
print(project_charter_v2)
```

---

### **Cell 8: Get Second-Pass Critique**

```python
# Capture improved code
improved_code = """
project_charter_v2 = {
    'stakeholders': [
        'VP Customer Success',
        'Retention Analytics Lead',
        'Data Engineering',
        'CFO',
        'Legal'
    ],
    ...
}
"""

improved_output = str(project_charter_v2)

# 🔄 GET SECOND-PASS CRITIQUE
critique_round2 = ai.second_pass_critique(
    methodology="CRISP-DM",
    phase_name="Business Understanding",
    initial_critique=critique_round1,
    improved_code=improved_code,
    improved_output=improved_output
)
```

**What happens:**
1. ✅ ChatGPT reviews your improvements
2. ✅ Checks if you addressed previous suggestions
3. ✅ Identifies what's still missing
4. ✅ Gives final score and recommendation
5. ✅ Says "Yes, ready to proceed" or "No, fix X first"

---

### **Cell 9-20: Continue with Phase 2**

Repeat the same pattern for Data Understanding, Data Preparation, etc.

---

## 📊 Example Output (What You'll See)

When you run `ai.critique_phase()`, you'll see in your notebook:

```
🤖 Requesting critique from gpt-4...
   Methodology: CRISP-DM
   Phase: Business Understanding
   Code length: 245 chars
   Output length: 189 chars
```

Then a beautifully formatted box appears:

---

### 🤖 AI Critique: Business Understanding

**✅ What You Did Well**

1. Clear stakeholder identification with two key roles
2. Specific, measurable success criteria (Recall >= 0.80)
3. Realistic constraints acknowledged (monthly refresh, explainability)
4. Milestone-based project planning

**⚠️ Critical Issues**

🟡 **Medium**: Missing CFO/Finance stakeholder - churn projects need ROI justification
🟡 **Medium**: No quantified business impact (e.g., "$X million annual loss from churn")
🟢 **Low**: Success criteria lacks precision threshold (only recall specified)

**💡 Specific Improvements**

1. **Add CFO to stakeholders** - They'll demand ROI projections and budget approval
2. **Quantify business impact** - Calculate: `churn_rate * customers * avg_LTV = annual_loss`
3. **Define customer LTV** - Needed to calculate retention campaign ROI
4. **Add precision to success criteria** - E.g., "Recall >= 0.80 AND Precision >= 0.55"
5. **Include regulatory stakeholder** - GDPR/privacy concerns for customer targeting
6. **Specify inference latency SLA** - E.g., "<150ms for real-time scoring"
7. **Add risk assessment** - What could block deployment? (data delays, capacity, legal)
8. **Define campaign economics** - Cost per contact, success rate assumptions
9. **Clarify "explainable"** - SHAP values? Feature importance? Executive dashboards?
10. **Add data audit milestone** - Validate data quality before modeling

**📚 Best Practices for Business Understanding**

1. Always start with "why" (business problem) before "what" (solution)
2. Translate technical metrics (recall) to business metrics ($ saved)
3. Get written sign-off from stakeholders on success criteria
4. Document assumptions that could invalidate the project

**✓ Ready to Proceed?**

**Not quite.** Address the CFO stakeholder, business impact quantification, and risk assessment before Phase 2. These are blockers for project approval.

Score: **6/10** - Good foundation but missing business justification

---

💾 Critique saved to: critiques/business_understanding/critique_20241102_143052.md

---

## 💰 Cost Estimate

Using OpenAI API:

- **GPT-4**: ~$0.03-0.10 per critique (2000-3000 tokens)
- **GPT-3.5-Turbo**: ~$0.002-0.005 per critique (much cheaper)

For all 16 checkpoints (6 + 5 + 5) with 2 passes each:
- **GPT-4**: ~$1-3 total
- **GPT-3.5-Turbo**: ~$0.10-0.20 total

💡 **Tip**: Use GPT-3.5-Turbo for drafts, GPT-4 for final critiques

---

## 📁 What Gets Saved

After running critiques, you'll have:

```
crisp_dm_telco_churn/
├── notebooks/
│   └── crisp_dm_telco_churn.ipynb (your notebook with API calls)
├── critiques/
│   ├── business_understanding/
│   │   ├── critique_20241102_143052.md (first pass)
│   │   └── critique_20241102_144523.md (second pass)
│   ├── data_understanding/
│   │   ├── critique_20241102_150112.md
│   │   └── critique_20241102_151045.md
│   └── ... (for each phase)
└── critiques/
    └── all_critiques.json (complete history)
```

Each `.md` file contains:
- Timestamp
- Code submitted
- Output/results
- Full AI critique

**Perfect for your assignment submission!**

---

## ✅ Benefits of This Approach

1. **Automated** - No copy-pasting to ChatGPT website
2. **Documented** - Every critique saved automatically
3. **Reproducible** - Clear audit trail of improvements
4. **Professional** - Beautiful formatting in notebooks
5. **Assignment-ready** - Shows iterative improvement process
6. **Version controlled** - All critiques in Git

---

## 🚀 Quick Start Commands

```bash
# 1. Install package
pip install openai

# 2. Set API key
export OPENAI_API_KEY="sk-your-key-here"

# 3. In your notebook
from ai_critique_helper import AICritiqueHelper
ai = AICritiqueHelper(model="gpt-4")

# 4. After each phase
critique = ai.critique_phase("CRISP-DM", "Business Understanding", code, output)

# 5. After improvements
critique2 = ai.second_pass_critique("CRISP-DM", "Business Understanding",
                                     critique, improved_code, improved_output)
```

---

## 🎯 Assignment Requirement Satisfied

This approach proves you:

✅ Used ChatGPT/GPT-5 for critique
✅ Did multiple revisions (two-pass process)
✅ Used "world renowned expert" persona
✅ Documented the iterative process
✅ Saved all artifacts
✅ Automated the workflow

**Perfect for demonstrating principled, step-by-step data science!**
