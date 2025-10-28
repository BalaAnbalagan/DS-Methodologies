# KDD Selection Critique Log

## Persona Prompt
> You are a world-renowned authority on KDD. You have authored multiple award-winning books and mentor Fortune 500 data teams. Critique my Selection phase with 10–15 actionable improvements, focusing on methodological rigor, completeness, and clarity.

## Pass 1
- **Prompt Sent**: _Assess dataset selection justification, sampling strategy, and coverage of business requirements._
- **Feedback Highlights (sample)**:
  - Explain rationale for using entire dataset vs temporal slice.
  - Validate absence of post-event features to avoid leakage.
  - Add criteria for refreshing data quarterly.
  - Map selected features to fraud detection objectives.
- **Revision Notes**:
  - Documented temporal window reasoning in notebook.
  - Audited features for leakage and flagged risky columns.
  - Added data refresh SOP to README.
  - Created traceability table linking features to objectives.

## Pass 2
- **Prompt Sent**: _Confirm sampling/selection rigor after updates. Suggest final refinements._
- **Feedback Highlights (sample)**:
  - Provide governance contacts for data source.
  - Clarify data latency expectation.
  - Note assumptions around anonymized PCA components.
- **Revision Notes**:
  - Added data steward contact info to README.
  - Captured latency expectation (T+1 day) in charter.
  - Documented PCA feature interpretation constraints.
