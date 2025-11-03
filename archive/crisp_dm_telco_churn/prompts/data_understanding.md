# CRISP-DM Data Understanding Critique Log

## Persona Prompt
> You are a world-renowned authority on CRISP-DM. You have authored multiple award-winning books and mentor Fortune 500 data teams. Critique my Data Understanding phase with 10–15 actionable improvements, focusing on methodological rigor, completeness, and clarity.

## Pass 1
- **Prompt Sent**: _Evaluate exploratory analysis depth, data quality assessment, and visual storytelling. Identify missing diagnostics or narrative gaps._
- **Feedback Highlights (sample)**:
  - Add missing value heatmap and per-feature completeness table.
  - Quantify churn imbalance with confidence intervals.
  - Provide narrative connecting tenure distribution to churn hypotheses.
  - Include data lineage graphic.
- **Revision Notes**:
  - Generated `missingno` visualization and summary table.
  - Calculated churn proportion confidence interval with Wilson method.
  - Expanded markdown storytelling around tenure insights.
  - Added quick lineage diagram to Medium draft.

## Pass 2
- **Prompt Sent**: _Review updates focusing on reproducibility and clarity. Flag any remaining blind spots._
- **Feedback Highlights (sample)**:
  - Clarify treatment of duplicated customer IDs.
  - Provide rationale for excluding out-of-date invoices.
  - Suggest interactive dashboard mock-up for stakeholders.
- **Revision Notes**:
  - Documented deduplication logic in notebook comment.
  - Added rule for excluding stale invoices to README.
  - Sketched dashboard layout in appendix.
