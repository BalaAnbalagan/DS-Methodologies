# CRISP‑DM Report

**Dataset:** Credit Card Fraud Detection

**Business Understanding:**

Fraudulent credit card transactions cause significant financial losses.  The objective is to predict fraudulent transactions and understand transaction patterns.  

**Data Understanding:**

The dataset contains anonymised numeric features (V1–V28) derived from PCA, plus `Time`, `Amount` and `Class`.  There are 284807 records with an extremely imbalanced distribution (only 492 fraud cases).  

**Data Preparation:**

An `Hour` feature was derived from `Time` to examine temporal patterns.  Features were standardised and the dataset was stratified into train and test subsets.  

**Modelling:**

Two models were trained: logistic regression and random forest. Evaluation metrics highlight the difficulty of the task given the imbalance.  

**Evaluation & Deployment:**

Both models achieved high ROC AUC, but precision and recall remained modest.  In production, one would need to tune the threshold and integrate the model into a real‑time monitoring pipeline.  

**Expert Review & Recommendations:**

* Imbalanced classes necessitate careful choice of metrics and algorithms.
* Additional features (e.g. device information, merchant data) could improve detection.
* Forecasting transaction volume could help anticipate periods of elevated fraud risk.
