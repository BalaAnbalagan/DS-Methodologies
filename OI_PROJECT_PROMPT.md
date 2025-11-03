# Open Interpreter Project Generation Prompt

Copy and paste this entire prompt into Open Interpreter after activating it.

---

## System Role

You are GPT-5 running inside Open-Interpreter on Bala's local Mac.
You can execute Python locally, install packages, read/write files, and generate reports.

## Goal

Automatically create and complete **three full end-to-end data-mining projects** using the three classic methodologies:
1️⃣ CRISP-DM
2️⃣ SEMMA
3️⃣ KDD

Each project must:
- Use a **different Kaggle or PapersWithCode dataset**
- Follow **all phases** of its methodology completely
- Produce executable code, detailed explanations, self-critiques, and Medium-ready markdowns

## Folder Structure (Already Created)

```
DS-Methodologies/
├── CRISP_DM/
│   ├── dataset/
│   ├── results/
│   ├── crisp_dm_notebook.ipynb (YOU CREATE THIS)
│   ├── report.md (YOU CREATE THIS)
│   └── medium_draft.md (YOU CREATE THIS)
├── SEMMA/
│   ├── dataset/
│   ├── results/
│   ├── semma_notebook.ipynb (YOU CREATE THIS)
│   ├── report.md (YOU CREATE THIS)
│   └── medium_draft.md (YOU CREATE THIS)
└── KDD/
    ├── dataset/
    ├── results/
    ├── kdd_notebook.ipynb (YOU CREATE THIS)
    ├── report.md (YOU CREATE THIS)
    └── medium_draft.md (YOU CREATE THIS)
```

## Datasets to Use

### CRISP-DM → Retail / Sales Forecasting
- **Dataset**: M5 Walmart Sales Forecasting
- **Kaggle**: `m5-forecasting-accuracy`
- **Problem**: Time series sales prediction
- **Download**: `kaggle datasets download -d m5-forecasting-accuracy -p CRISP_DM/dataset --unzip`

### SEMMA → Student Performance
- **Dataset**: UCI Student Performance
- **Kaggle**: `uciml/student-alcohol-consumption`
- **Problem**: Student grade prediction
- **Download**: `kaggle datasets download -d uciml/student-alcohol-consumption -p SEMMA/dataset --unzip`

### KDD → Credit Card Fraud Detection
- **Dataset**: Credit Card Fraud
- **Kaggle**: `mlg-ulb/creditcardfraud`
- **Problem**: Anomaly/fraud detection
- **Download**: `kaggle datasets download -d mlg-ulb/creditcardfraud -p KDD/dataset --unzip`

## Project Generation Loop

For **each methodology** (CRISP-DM, SEMMA, KDD):

### Step 1: Download Dataset
```python
import subprocess
# Use appropriate kaggle download command above
subprocess.run(["kaggle", "datasets", "download", ...])
```

### Step 2: Generate Jupyter Notebook

Create `<methodology>_notebook.ipynb` with:

#### A. Methodology-Specific Phases

**CRISP-DM (6 phases):**
1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

**SEMMA (5 phases):**
1. Sample
2. Explore
3. Modify
4. Model
5. Assess

**KDD (5 phases):**
1. Selection
2. Preprocessing
3. Transformation
4. Data Mining
5. Interpretation & Evaluation

#### B. For Each Phase:

1. **Add Markdown Header**
   ```markdown
   ## Phase N: [Phase Name]

   [Brief description of what this phase does]
   ```

2. **Add Code Cells**
   - Load data
   - Perform analysis
   - Create visualizations
   - Save figures to `results/`
   - Print key metrics

3. **Execute Code & Capture Outputs**
   - Actually RUN the code
   - Capture print outputs
   - Save visualizations

4. **Add Expert Critique Section**
   ```markdown
   ### 🔍 Expert Review & Recommendations

   You are a world-renowned data-mining authority who has authored multiple
   award-winning books and mentor Fortune 500 data teams. Critique this
   [Phase Name] phase with 10–15 actionable improvements, focusing on
   methodological rigor, completeness, and clarity.

   **Critique:**

   [Use OpenAI API to generate critique - see code below]
   ```

5. **Generate AI Critique Using OpenAI API**
   ```python
   import openai
   from dotenv import load_dotenv
   load_dotenv()

   def get_critique(phase_name, code, output):
       response = openai.chat.completions.create(
           model="gpt-4",
           messages=[
               {"role": "system", "content": "You are a world-renowned data mining methodology expert."},
               {"role": "user", "content": f'''Review this {phase_name} phase:

               CODE:
               {code}

               OUTPUT:
               {output}

               Provide 10-15 actionable improvements focusing on methodological rigor.'''}
           ]
       )
       return response.choices[0].message.content

   critique = get_critique(phase_name, code_str, output_str)
   # Add critique to notebook as markdown cell
   ```

### Step 3: Generate Report (report.md)

Create a comprehensive phase-by-phase report with:

```markdown
# [Methodology] Project Report: [Dataset Name]

## Executive Summary
[1-2 paragraphs on project goals and outcomes]

## Methodology Overview
[Why this methodology? What are its strengths?]

## Phase-by-Phase Analysis

### Phase 1: [Name]
**Implementation:**
- [What was done]
- [Key code snippets]

**Results:**
- [Metrics, findings]
- [Visualizations]

**Expert Critique:**
- [Top 3-5 recommendations from AI]

[Repeat for all phases]

## Key Findings
1. ...
2. ...
3. ...

## Conclusion & Recommendations
[Business value, next steps]
```

### Step 4: Generate Medium Article (medium_draft.md)

Create publication-ready article:

```markdown
# Mastering [Methodology]: A Complete Guide to [Problem Type]

*A comprehensive walkthrough of [methodology] applied to real-world data*

---

## Introduction

[Hook: Why this methodology matters]
[Dataset introduction]
[What readers will learn]

## The [Methodology] Framework

[Explain methodology with storytelling]
[Why it's used in industry]

## Implementation Journey

### Phase 1: [Name]
[Story-style explanation]
[Key insights]
[Visualization]

[Repeat for all phases]

## Key Takeaways

1. [Business insight]
2. [Technical insight]
3. [Methodological insight]

## What's Next?

[Call to action]
[Links to project]

---

*Generated: [Date]*
#DataScience #MachineLearning #[Methodology] #DataMining
```

## Requirements for Each Notebook

### Minimum Content Standards:

1. **Imports & Setup** (1 cell)
2. **Each Phase** (3-5 cells minimum):
   - Markdown explanation
   - Code implementation
   - Output/visualization
   - AI critique
3. **Comprehensive EDA** with 5+ visualizations
4. **Multiple Models** (at least 3 algorithms)
5. **Model Comparison** table
6. **Business Impact** analysis
7. **Deployment** artifacts (save model, create model card)

### Code Quality:

- Clean, commented code
- Professional visualizations (seaborn/matplotlib)
- Proper train/test splits
- Cross-validation where appropriate
- Error handling
- Performance metrics clearly displayed

## Final Deliverables

After generating all 3 projects:

### 1. Root README.md

```markdown
# DS Methodologies Portfolio

Three complete data mining projects demonstrating industry-standard methodologies.

## Projects

### 1. CRISP-DM: Walmart Sales Forecasting
- **Dataset**: M5 Forecasting
- **Accuracy**: [X]%
- **Key Insight**: [...]
- [Medium Article](#)

### 2. SEMMA: Student Performance Prediction
- **Dataset**: UCI Student Performance
- **Accuracy**: [X]%
- **Key Insight**: [...]
- [Medium Article](#)

### 3. KDD: Credit Card Fraud Detection
- **Dataset**: Credit Card Fraud
- **AUC**: [X]
- **Key Insight**: [...]
- [Medium Article](#)

## Methodology Comparison

[See COMPARISON_TABLE.md]

## Usage

Each project folder contains:
- `*_notebook.ipynb` - Complete implementation
- `report.md` - Detailed analysis
- `medium_draft.md` - Publication-ready article

## Installation

\`\`\`bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter openai python-dotenv
\`\`\`
```

### 2. COMPARISON_TABLE.md

Create a comparison table:

```markdown
# Methodology Comparison

| Aspect | CRISP-DM | SEMMA | KDD |
|--------|----------|-------|-----|
| **Focus** | Business-driven | Model-centric | Knowledge discovery |
| **Phases** | 6 | 5 | 5 |
| **Iterations** | Cyclical | Linear | Iterative |
| **Best For** | Business problems | Statistical modeling | Exploratory analysis |
| **Accuracy** | [X]% | [Y]% | [Z]% |
| **Training Time** | [X]min | [Y]min | [Z]min |
| **Interpretability** | High | Medium | High |
| **Deployment Ready** | ✅ | ✅ | ⚠️ Research-focused |

## Key Insights

### CRISP-DM
- Strengths: [...]
- Weaknesses: [...]
- Best use case: [...]

### SEMMA
- Strengths: [...]
- Weaknesses: [...]
- Best use case: [...]

### KDD
- Strengths: [...]
- Weaknesses: [...]
- Best use case: [...]

## Conclusion

[Which methodology for which scenarios?]
```

## Style Guidelines

- Write clearly and educationally
- Use Bala's friendly Tamil-influenced English tone
- Include emoji sparingly (✅ ❌ 📊 🎯 only)
- Add IEEE-style peer review paragraphs after each methodology
- Professional but approachable
- Focus on both technical excellence and business value

## Execution Instructions

1. **Run this entire prompt in Open Interpreter**
2. **Let it execute autonomously** - it should:
   - Download all 3 datasets
   - Generate all 3 notebooks (with AI critiques)
   - Generate all 6 documentation files (3 reports + 3 Medium articles)
   - Generate README.md and COMPARISON_TABLE.md
3. **Verify outputs** - check that all files exist and have content
4. **Polish if needed** - manual review and edits

## Expected Timeline

- Dataset downloads: 5-10 minutes
- CRISP-DM generation: 20-30 minutes
- SEMMA generation: 20-30 minutes
- KDD generation: 20-30 minutes
- Documentation: 10-15 minutes
- **Total: 75-115 minutes autonomous execution**

---

## Begin Execution

Start by saying:

> "I will now generate three complete data mining projects using CRISP-DM, SEMMA, and KDD methodologies. This will take approximately 90 minutes. Let me start with CRISP-DM..."

Then proceed autonomously through all steps.

**✅ When complete, print: "All projects ready for publish in Medium and GitHub."**
