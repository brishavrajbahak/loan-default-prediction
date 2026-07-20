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

## Day 3 — Leakage Audit and PostgreSQL Setup

**Date:** July 19, 2026

### Completed

- Created the approved origination-time feature list.
- Created the excluded-feature list.
- Confirmed the target is separate from the input features.
- Passed the automated leakage audit.
- Created `data/processed/modeling_dataset.csv`.
- Created the PostgreSQL database `loan_default_prediction`.
- Created the `analytics.loan_modeling` table.
- Imported the modeling dataset through DBeaver.
- Confirmed no missing values in the checked database columns.
- Saved `sql/01_import_validation.sql`.

### Concepts Learned

- Data leakage
- Feature boundaries
- Target versus input features
- PostgreSQL schemas and tables
- Import validation with SQL
- Reproducible SQL audit trails

### Blockers

The first leakage assertion included the target column by mistake. It was corrected by checking only the input features.

### Next Session

Explore default-rate patterns across the approved features.
## Day 4 — Feature Exploration

**Date:** July 20, 2026

### Completed

- Created DTI, income, and interest-rate analysis bands.
- Built a reusable default-rate summary function.
- Analyzed default rate by grade and sub-grade.
- Analyzed default rate by DTI band, interest-rate band, loan term, income band, purpose, and issue year.
- Added charts using Matplotlib and Seaborn.
- Added evidence-based observations to the feature-exploration notebook.
- Documented that these are associations, not causal conclusions.

### Concepts Learned

- Feature engineering for analysis
- Binning continuous variables
- Grouped default-rate calculations
- Sample-size-aware interpretation
- Matplotlib and Seaborn visualization
- Association versus causation

### Blockers

None.

### Next Session

Create a time-based train, validation, and test split without future-data leakage.