# CRISP-DM Evaluation Critique Log

## Persona Prompt
> You are a world-renowned authority on CRISP-DM. You have authored multiple award-winning books and mentor Fortune 500 data teams. Critique my Evaluation phase with 10–15 actionable improvements, focusing on methodological rigor, completeness, and clarity.

## Pass 1
- **Prompt Sent**: _Assess whether the model meets business metrics, statistical significance, and risk tolerances. Probe for missing validation strategies._
- **Feedback Highlights (sample)**:
  - Include uplift of retention campaign to show ROI impact.
  - Provide bootstrapped confidence intervals on ROC-AUC.
  - Detail error analysis by contract type and tenure bucket.
  - Document acceptance criteria vs achieved metrics.
- **Revision Notes**:
  - Added ROI calculator for retention offer scenarios.
  - Bootstrapped AUC with 1000 iterations and reported CI.
  - Expanded confusion matrix commentary by key segments.
  - Matched acceptance checklist to evaluation summary table.

## Pass 2
- **Prompt Sent**: _Re-check evaluation narrative for executive readiness. Identify final polish suggestions._
- **Feedback Highlights (sample)**:
  - Clarify statistical power of evaluation sample.
  - Add risk of decay plan (monitoring cadence, triggers).
  - Provide one-slide executive summary graphic.
- **Revision Notes**:
  - Calculated power assuming monthly churn base rate.
  - Drafted monitoring playbook in README.
  - Designed infographic placeholder for executive deck.
