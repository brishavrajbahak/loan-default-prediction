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


## Day 5 — Time-Based Data Split

**Date:** July 21, 2026

### Completed

- Created a chronological train, validation, and test split.
- Used 2007–2015 for training.
- Used 2016–2017 for validation.
- Used 2018 for final testing.
- Confirmed the test set contains only 2018 loans.
- Confirmed split sizes add up to the complete dataset.
- Confirmed no row overlap between the splits.
- Separated input features from `default_flag`.

### Concepts Learned

- Temporal validation
- Future-data leakage
- Train, validation, and test roles
- Feature-target separation
- Target-rate drift across time

### Next Session

Build a dummy baseline and logistic-regression pipeline.

## Day 6 — Baseline and Logistic Models

**Date:** July 22, 2026

### Completed

- Created `notebooks/04_baseline_models.ipynb`.
- Recreated the chronological train, validation, and test splits.
- Separated input features from `default_flag`.
- Identified numeric and categorical features.
- Built a preprocessing pipeline with imputation, scaling, and one-hot encoding.
- Trained a majority-class dummy baseline.
- Trained a balanced logistic-regression model.
- Evaluated accuracy, precision, recall, F1-score, and ROC-AUC.
- Generated and interpreted the logistic-regression confusion matrix.

### Results

- Dummy accuracy: 76.77%
- Dummy recall: 0.00
- Logistic accuracy: 61.57%
- Logistic precision: 33.98%
- Logistic recall: 69.40%
- Logistic F1-score: 0.4562
- Logistic ROC-AUC: 0.697

### Key Finding

The dummy model achieves higher accuracy by predicting only the majority good-loan class, but it detects no bad loans. Logistic regression has lower accuracy but identifies substantially more bad loans. This shows why recall, precision, F1-score, and ROC-AUC are more informative than accuracy alone for this imbalanced classification problem.

### Blockers

The first logistic-regression run reached the iteration limit. Increasing `max_iter` and adjusting `tol` resolved the convergence warning.

### Next Session

Train and compare a decision tree and random forest.

## Day 7 — Tree-Based Models

**Date:** July 23, 2026

### Completed

- Created `notebooks/05_tree_models.ipynb`.
- Recreated the chronological data splits.
- Built tree-model preprocessing for numeric and categorical features.
- Trained a decision tree.
- Trained a random forest.
- Evaluated both models using accuracy, precision, recall, F1-score, and ROC-AUC.
- Detected and corrected target leakage caused by including `default_flag` in the feature list.
- Retrained both models after separating the target correctly.

### Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
| --- | ---: | ---: | ---: | ---: | ---: |
| Decision tree | 0.6208 | 0.3405 | 0.6749 | 0.4526 | 0.6944 |
| Random forest | 0.6328 | 0.3482 | 0.6664 | 0.4574 | 0.6989 |

### Key Finding

After correcting target leakage, performance became realistic. Random forest is currently the strongest balanced candidate based on F1-score and ROC-AUC. Logistic regression remains competitive and provides higher recall.

### Concepts Learned

- Decision trees
- Random forests
- Ensemble modeling
- Target leakage detection
- Model comparison
- Precision-recall trade-offs

### Blockers

The first model results were artificially perfect because `default_flag` was accidentally included in the input features. The feature-target separation was corrected and both models were retrained.

### Next Session

Perform formal model evaluation and compare all models on validation and test data.

## Day 8 — Evaluation and Explainability

**Date:** July 24, 2026

### Completed

- Evaluated the decision tree and random forest on the untouched 2018 test set.
- Corrected the decision-tree ROC-AUC calculation so it uses the matching test probabilities.
- Generated confusion matrices for both tree models.
- Generated ROC curves and precision-recall curves.
- Calculated average precision for both models.
- Extracted random-forest feature importances from the encoded features.
- Aggregated encoded importances back to the original business features.
- Documented that feature importance indicates predictive usefulness, not causation.

### Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC | Average Precision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Decision tree - 2018 test | 0.5948 | 0.2335 | 0.6882 | 0.3486 | 0.6840 | 0.27 |
| Random forest - 2018 test | 0.6206 | 0.2428 | 0.6645 | 0.3557 | 0.6912 | 0.28 |

### Key Findings

- Random forest is the stronger overall candidate on the 2018 test set, with the highest accuracy, F1-score, ROC-AUC, and average precision.
- The decision tree has slightly higher recall, so it identifies more bad loans but also produces more false positives.
- The strongest aggregated random-forest features are interest rate (29.84%), grade (24.66%), term (18.69%), and sub-grade (10.66%).
- Grade and sub-grade are related credit-risk variables; their combined importance is approximately 35.33% and should not be treated as independent causal effects.
- Both models have only moderate ranking performance, so the results are useful for risk segmentation and further investigation, not automatic lending decisions.

### Concepts Learned

- Holdout test evaluation
- Confusion-matrix interpretation
- ROC-AUC and average precision
- Precision-recall trade-offs
- Encoded-feature importance
- Aggregating model importance to original features
- Predictive association versus causation

### Blockers

The first test-results table displayed the wrong decision-tree ROC-AUC because the probability variable did not match the model. The metric was recalculated using the correct test probabilities.

### Next Session

Perform error analysis by examining false positives and false negatives across grade, term, DTI, income, and other risk segments.
