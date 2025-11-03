# ⚡ Fast Workflow: Get AI Critiques in 5 Minutes Per Phase

**Goal**: Quickly get ChatGPT critiques for all phases with minimal effort.

---

## 🚀 Super Quick Setup (One-Time, 2 Minutes)

Your API key is already configured! Just verify:

```python
# Test in Python
python3 test_api_key.py
# Should show: ✅ API connection successful!
```

---

## 📝 The Fast Workflow (5 Minutes Per Phase)

### Step 1: Open Your Notebook

```bash
cd crisp_dm_telco_churn/notebooks
jupyter notebook crisp_dm_telco_churn.ipynb
```

### Step 2: Add This Cell ONCE at the Top

```python
# Import AI critique helper
from ai_critique_helper import AICritiqueHelper

# Initialize with fast model (cheaper + faster than GPT-4)
ai = AICritiqueHelper(model="gpt-3.5-turbo")

print("✅ AI Critique Helper Ready!")
```

### Step 3: After EACH Phase, Add This

```python
# === AI CRITIQUE CHECKPOINT ===

# 1. Capture your code as string
code = """
# Copy-paste your phase code here
project_charter = {
    'stakeholders': ['VP Customer Success'],
    'business_objectives': ['Reduce churn']
}
"""

# 2. Capture your output
output = str(project_charter)  # or whatever your output variable is

# 3. Get AI critique (auto-displays + saves)
critique = ai.critique_phase(
    methodology="CRISP-DM",  # or "KDD" or "SEMMA"
    phase_name="Business Understanding",  # change for each phase
    code=code,
    output=output
)

# 4. Read the critique above ☝️ and make improvements below ☟
```

### Step 4: After Making Improvements

```python
# === SHOW IMPROVEMENTS ===

# Your improved code
improved_code = """
project_charter = {
    'stakeholders': ['VP Customer Success', 'CFO', 'Legal'],  # Added based on critique
    'business_objectives': ['Reduce churn', 'Calculate ROI'],  # Added ROI
    'risks': ['Delayed billing feeds']  # Added risk assessment
}
"""

improved_output = str(project_charter_v2)

# Get second critique to show revision
critique2 = ai.second_pass_critique(
    methodology="CRISP-DM",
    phase_name="Business Understanding",
    initial_critique=critique,
    improved_code=improved_code,
    improved_output=improved_output
)

# ✅ Done! Both critiques auto-saved to critiques/ folder
```

---

## 📁 What Gets Saved Automatically

After running critiques, you'll have:

```
crisp_dm_telco_churn/
└── critiques/
    ├── business_understanding/
    │   ├── critique_20241102_143052.md  ← First critique
    │   └── critique_20241102_144523.md  ← After improvements
    ├── data_understanding/
    │   ├── critique_20241102_150112.md
    │   └── critique_20241102_151045.md
    └── ... (for each phase)
```

**Perfect for assignment submission - shows iterative improvement!**

---

## ⚡ Even FASTER: Copy-Paste Template

Just copy this template after each phase:

```python
# ========== AI CRITIQUE CHECKPOINT ==========
code = """
[PASTE YOUR CODE HERE]
"""
output = """[PASTE YOUR OUTPUT HERE]"""

# First critique
critique = ai.critique_phase("CRISP-DM", "Phase Name", code, output)

# [READ CRITIQUE, MAKE IMPROVEMENTS]

improved_code = """[PASTE IMPROVED CODE]"""
improved_output = """[PASTE NEW OUTPUT]"""

# Second critique (shows revision!)
critique2 = ai.second_pass_critique("CRISP-DM", "Phase Name", critique, improved_code, improved_output)
# ========== END CHECKPOINT ==========
```

**Time per phase: ~5 minutes** (2 min for first critique, 3 min to improve and get second critique)

---

## 💰 Cost

- **GPT-3.5-Turbo**: ~$0.002-0.005 per critique
- **For 18 phases × 2 critiques = 36 total**: ~$0.10-0.20 total
- **For GPT-4** (if you want better quality): ~$1-3 total

**Recommendation**: Use `gpt-3.5-turbo` for speed, it's good enough for critiques!

---

## 🎯 Which Phases to Critique?

### If Time is Tight (Minimum for Assignment):

**CRISP-DM**: Business Understanding, Modeling, Evaluation (3 phases)
**KDD**: Selection, Data Mining, Interpretation (3 phases)
**SEMMA**: Sample, Model, Assess (3 phases)

**Total: 9 phases × 2 critiques = 18 critiques = 45 minutes**

### If You Have Time (Complete):

**CRISP-DM**: All 6 phases = 30 minutes
**KDD**: All 5 phases = 25 minutes
**SEMMA**: All 5 phases = 25 minutes

**Total: 16 phases × 2 critiques = 32 critiques = 80 minutes**

---

## 🆘 Troubleshooting

**"API key not found" error:**
```bash
python3 test_api_key.py  # Verify setup
```

**Want to see saved critiques:**
```bash
ls critiques/business_understanding/
cat critiques/business_understanding/critique_*.md
```

**Too expensive? Switch to GPT-3.5:**
```python
ai = AICritiqueHelper(model="gpt-3.5-turbo")  # Much cheaper!
```

---

## 📊 Alternative: Use Browser ChatGPT (Even Faster!)

**If you prefer the ChatGPT web interface:**

1. Open https://chat.openai.com
2. Copy the expert prompt from `prompts/business_understanding.md`
3. Paste your code and output
4. Get critique
5. Make improvements
6. Paste improved code
7. Get second critique
8. **Share the conversation** (ChatGPT has "share" button)
9. Add link to your notebook

**Pros:**
- ✅ Familiar interface
- ✅ No code needed
- ✅ Can save conversations

**Cons:**
- ❌ Manual copy-paste
- ❌ Not integrated in notebook

**Both approaches satisfy the assignment!**

---

## ✅ Final Checklist

- [ ] Test API key: `python3 test_api_key.py`
- [ ] Open notebook: `jupyter notebook`
- [ ] Add AI helper initialization cell
- [ ] After each phase: Run critique
- [ ] Make improvements
- [ ] Run second critique
- [ ] Verify critiques saved in `critiques/` folders
- [ ] Commit to GitHub

**That's it! Fast, simple, and satisfies the assignment requirement for "multiple revisions through AI critique."**

---

## 📚 Full Documentation

- **This guide** - Fast workflow (you are here!)
- [QUICK_API_START.md](QUICK_API_START.md) - More detailed guide
- [EXAMPLE_AI_CRITIQUE_USAGE.md](EXAMPLE_AI_CRITIQUE_USAGE.md) - Complete reference

---

**Time to complete all 3 methodologies: ~90 minutes**

**Ready? Open a notebook and start with Business Understanding!** 🚀
