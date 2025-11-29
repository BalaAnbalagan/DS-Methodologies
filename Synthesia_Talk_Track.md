# Synthesia Talk Track Script
## Data Science Methodologies Portfolio: CRISP-DM, SEMMA & KDD

**Total Duration**: ~5-7 minutes
**Speaker**: Professional, confident, educational tone

---

## SLIDE 1: Title Slide
**Duration**: ~20 seconds

> "Hello! I'm Bala Anbalagan from San Jose State University. Today, I'll walk you through my Data Science Methodologies Portfolio, where I compare three fundamental approaches to data mining: CRISP-DM, SEMMA, and KDD. I applied all three methodologies to the same problem—credit card fraud detection—to demonstrate their unique strengths and trade-offs. Let's dive in."

---

## SLIDE 2: Problem Overview / Dataset
**Duration**: ~40 seconds

> "Our challenge is credit card fraud detection using a real-world dataset from Kaggle. The dataset contains nearly 285,000 European credit card transactions from September 2013.

> Here's the critical challenge: only 492 transactions are fraudulent—that's just 0.17% of the data. This creates a massive 579-to-1 class imbalance, which means traditional accuracy metrics become meaningless. A model that simply predicts 'not fraud' for everything would be 99.83% accurate—but catch zero frauds.

> This extreme imbalance makes fraud detection a perfect case study for comparing different data mining methodologies."

---

## SLIDE 3: Methodology Comparison Overview
**Duration**: ~45 seconds

> "Let me introduce the three methodologies I compared.

> First, CRISP-DM—the Cross-Industry Standard Process for Data Mining. It's a business-focused approach with six phases, emphasizing deployment planning and stakeholder alignment. Think of it as the gold standard for production systems.

> Second, SEMMA—developed by SAS Institute. It focuses on rapid prototyping through five phases: Sample, Explore, Modify, Model, and Assess. It's perfect for quick experimentation and iterative refinement.

> Third, KDD—Knowledge Discovery in Databases. Born in academia, KDD emphasizes scientific rigor and is particularly suited for unsupervised learning when labeled data isn't available.

> Each methodology has its sweet spot, and I'll show you exactly what that means in practice."

---

## SLIDE 4: CRISP-DM Approach
**Duration**: ~50 seconds

> "Let's start with CRISP-DM. I followed all six phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment planning.

> For the business objective, I aimed to flag fraudulent transactions while minimizing false positives that frustrate legitimate customers.

> In data preparation, I engineered an 'Hour' feature from timestamps to capture daily transaction patterns, and standardized all features using z-score normalization.

> I trained two models: Logistic Regression as a baseline, and Random Forest to capture nonlinear patterns in the anonymized PCA features.

> The Random Forest achieved outstanding results: 96.52% precision and 75% recall, with an F1 score of 84.41%. This means when the model flags a transaction as fraud, it's correct 96.5% of the time—with only 4 false positives out of 111 detected frauds."

---

## SLIDE 5: SEMMA Approach
**Duration**: ~50 seconds

> "Now let's look at SEMMA's rapid prototyping approach.

> In the Sample phase, I made a strategic decision: instead of using all 285,000 transactions, I sampled 49,000 legitimate transactions but kept ALL 492 fraud cases. This gave me a 6x computational speedup while preserving the fraud signal.

> During Exploration, correlation heatmaps revealed weak linear relationships—a clear signal that ensemble methods would outperform linear models.

> After standardization in the Modify phase, I trained a Random Forest with 100 trees.

> The results were exceptional: 97.79% ROC AUC—the highest across all three methodologies—with 93.85% precision and 82.43% recall.

> SEMMA's iterative philosophy helped me identify specific improvements for the next iteration, like SMOTE resampling and feature engineering."

---

## SLIDE 6: KDD Approach (Unsupervised)
**Duration**: ~55 seconds

> "Here's where things get interesting. For KDD, I took a completely different approach: unsupervised anomaly detection using Isolation Forest.

> The key difference? I intentionally ignored the fraud labels during training. The model learned what 'normal' transactions look like and flagged anything unusual as potential anomalies.

> Why would I do this? Because in the real world, new fraud patterns emerge constantly. Supervised models only catch frauds they've seen before. Unsupervised methods can detect novel attacks.

> The results show the trade-off clearly: only 29% precision and 17% recall. The model caught just 83 of 492 frauds, with 202 false positives.

> But here's the insight: those 83 detected frauds represent discoveries made WITHOUT any labeled training data. In a real workflow, analysts would review these cases first, label them, and then train a supervised model—bootstrapping from unsupervised to supervised learning."

---

## SLIDE 7: Performance Comparison Table
**Duration**: ~40 seconds

> "Let's compare the three approaches side by side.

> CRISP-DM with Random Forest achieved 96.52% precision—the highest—and 75% recall.

> SEMMA achieved the best ROC AUC at 97.79%, with 93.85% precision and the highest recall at 82.43%. Its F1 score of 87.77% was also the best overall.

> KDD's unsupervised approach achieved only 29% precision and 17% recall—but remember, it used zero labeled data during training.

> The performance gap between supervised and unsupervised methods is stark—about 67 percentage points in precision. But that doesn't make unsupervised methods worthless; they serve different purposes."

---

## SLIDE 8: Business Value Analysis
**Duration**: ~40 seconds

> "Let's quantify the business impact.

> Both supervised approaches—CRISP-DM and SEMMA—delivered approximately $11,500 in net value on the test set alone.

> Here's how I calculated it: With an average fraud of $120, detecting 122 frauds saves about $14,600. Subtract the $3,100 loss from 26 missed frauds, and the $45 cost of investigating 9 false positives, and you get $11,475 saved.

> Scaled to millions of daily transactions, this translates to millions in annual savings for a financial institution. That's the real-world value of choosing the right methodology and model."

---

## SLIDE 9: When to Use Each Methodology
**Duration**: ~45 seconds

> "So when should you use each methodology?

> Use CRISP-DM when you need production deployment, stakeholder alignment, and comprehensive documentation. It's ideal when business ROI must be quantified upfront.

> Use SEMMA when speed matters more than comprehensiveness—for proof-of-concept projects, rapid prototyping, and iterative experimentation where the business context is already well understood.

> Use KDD when labels are unavailable or unreliable, for exploratory research, or when you need to discover unknown patterns. It's also valuable for bootstrapping a labeled dataset from scratch.

> No methodology is universally superior—each excels in its intended context."

---

## SLIDE 10: Conclusion & Resources
**Duration**: ~35 seconds

> "To summarize: I applied three data mining methodologies to the same fraud detection problem.

> CRISP-DM delivered 96.5% precision—production-ready performance with business alignment.

> SEMMA achieved the best ROC AUC at 97.8% through rapid iteration and strategic sampling.

> KDD demonstrated unsupervised learning's trade-offs—lower metrics, but valuable when labels don't exist.

> All code, notebooks, and detailed articles are available on my GitHub repository and published on Medium. The links are shown here.

> Thank you for watching! If you have questions, feel free to reach out at bala.anbalagan@sjsu.edu."

---

## TIPS FOR SYNTHESIA

1. **Pacing**: Each slide script is designed for natural reading speed (~150 words/minute)
2. **Emphasis**: Words in **bold** in original should have slight vocal emphasis
3. **Pauses**: Add brief pauses after key metrics (96.5%, 97.79%, etc.)
4. **Tone**: Professional but approachable, like explaining to a colleague
5. **Avatar**: Choose a professional presenter avatar
6. **Background**: Neutral or office setting works best

## TOTAL WORD COUNT
Approximately 1,100 words = ~7 minutes at natural speaking pace

---

## SHORTENED VERSION (3-4 minutes)

If you need a shorter version, use these condensed scripts:

### Slide 1 (10 sec)
> "Hi, I'm Bala Anbalagan. Today I'll compare three data mining methodologies—CRISP-DM, SEMMA, and KDD—using credit card fraud detection."

### Slide 2 (20 sec)
> "Our dataset has 285,000 transactions with only 492 frauds—a 579-to-1 class imbalance that makes accuracy metrics meaningless."

### Slide 3 (25 sec)
> "CRISP-DM focuses on business value and deployment. SEMMA enables rapid prototyping. KDD uses unsupervised learning when labels aren't available."

### Slide 4 (25 sec)
> "CRISP-DM achieved 96.5% precision with Random Forest—only 4 false positives per 111 detected frauds."

### Slide 5 (25 sec)
> "SEMMA's strategic sampling achieved 97.8% ROC AUC—the best class separation—with 6x faster training."

### Slide 6 (25 sec)
> "KDD's unsupervised Isolation Forest achieved 29% precision—lower, but without using any labeled training data."

### Slide 7 (20 sec)
> "Supervised methods achieved 93-96% precision versus 29% for unsupervised—a 67 percentage point gap when labels exist."

### Slide 8 (20 sec)
> "Both supervised approaches save approximately $11,500 on the test set—millions annually at scale."

### Slide 9 (20 sec)
> "Use CRISP-DM for production, SEMMA for prototyping, and KDD for exploration when labels are unavailable."

### Slide 10 (15 sec)
> "All code and articles are on GitHub and Medium. Thank you for watching!"

---

*Script created for Synthesia AI video generation*
