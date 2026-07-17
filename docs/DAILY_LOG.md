# Daily Project Log

## Day 1 - Setup and Dataset Audit

**Date:** July 17, 2026

### Completed

- Initialized the Git repository and project structure.
- Added `.gitignore` and `README.md`.
- Copied the cleaned dataset into `data/processed`.
- Created `notebooks/01_dataset_audit.ipynb`.
- Confirmed 1,348,099 rows and 18 columns.
- Confirmed zero duplicate rows and zero duplicate loan IDs.
- Identified missing values in `emp_length_years`, `dti`, and `annual_inc`.
- Confirmed 1,078,739 good loans and 269,360 bad loans.
- Confirmed a 19.98% bad-loan rate.
- Confirmed `outcome_group` and `default_flag` agree fully.

### Concepts Learned

- Loan-level unit of analysis
- Missing-value profiling
- Duplicate validation
- Binary classification targets
- Class imbalance
- Target consistency checks

### Blockers

None.

### Next Session

Define and validate the prediction target, then document the target logic clearly.

