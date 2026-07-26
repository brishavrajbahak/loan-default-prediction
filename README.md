# Explainable Loan Default Prediction System

An educational machine-learning project that estimates historical bad-loan risk from information available when a loan is issued.

## Business Question

Can loan-level characteristics at origination help identify loans with higher historical default risk?

## Dataset

This project uses a cleaned Lending Club loan-level dataset. Each row represents one loan.

Current or unresolved loans are excluded because their final repayment outcome is not yet known.

## Prediction Target

| Value | Meaning |
| --- | --- |
| `0` | Good completed outcome |
| `1` | Bad completed outcome |

The target is based on the final completed outcome, not an intermediate status such as `Current` or `Late`.

## Features Used

Only origination-time information will be used:

- Loan amount and term
- Interest rate
- Grade and sub-grade
- Employment length
- Home ownership
- Annual income
- Verification status
- Issue year
- Loan purpose
- Debt-to-income ratio

## Leakage Exclusions

The model will exclude loan-status fields, payment history, recoveries, collections, last-payment information, and all other post-issuance variables.

## Project Workflow

1. Audit and validate the dataset
2. Define the prediction target
3. Audit possible data leakage
4. Store and validate data with PostgreSQL
5. Explore risk patterns
6. Train baseline and tree-based models
7. Evaluate model performance
8. Explain model predictions
9. Build a Streamlit interface
10. Deploy the application

## Streamlit Demo

Run the application locally from the repository root:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The app accepts origination-time loan details and displays an estimated probability of a bad outcome. Grade and sub-grade use dependent selections so invalid combinations cannot be entered.

### Live Demo

[Open the deployed Loan Default Risk Predictor](https://brishav-loan-default-prediction.streamlit.app/)

### Screenshots

![Higher-risk prediction](reports/screenshots/Screenshot%202026-07-26%20100842.png)

![Lower-risk prediction](reports/screenshots/Screenshot%202026-07-26%20101131.png)

![Streamlit input form](reports/screenshots/Screenshot%202026-07-26%20101320.png)

## Tools

Python, pandas, scikit-learn, PostgreSQL, SQL, Power BI, Streamlit, Git, and GitHub.

## Repository Structure

```text
data/          Dataset files kept locally
notebooks/     Reproducible analysis notebooks
src/           Reusable Python code
app.py         Streamlit application
models/        Saved model artifacts
docs/          Daily logs and project documentation
reports/       Screenshots and project outputs
```

## Important Limitation

This is an educational and retrospective analysis. It is not a production lending or credit-approval system.

## Status

Completed through the merged Day 10 milestone: dataset audit, target validation, leakage audit, PostgreSQL validation, feature exploration, time-based splitting, baseline and tree models, test evaluation, explainability, error analysis, and a working Streamlit application.

Progress is recorded in [`docs/DAILY_LOG.md`](docs/DAILY_LOG.md).
