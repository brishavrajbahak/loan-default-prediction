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

## Day 2 — Define and Validate the Prediction Target

**Date:** July 18, 2026

### Completed

- Reviewed `loan_status`, `outcome_group`, and `default_flag`.
- Confirmed `final_good` maps to `default_flag = 0`.
- Confirmed `final_bad` maps to `default_flag = 1`.
- Confirmed zero unexpected target rows.
- Confirmed the target columns agree for every record.
- Added automated assertions for target validation.

### Concepts Learned

- Business outcome versus machine-learning target
- Binary target encoding
- Target consistency validation
- Reproducible assertions
- Why unresolved loan statuses should not be training labels

### Blockers

None.

### Next Session

Separate origination-time features from post-loan fields and audit the dataset for leakage.