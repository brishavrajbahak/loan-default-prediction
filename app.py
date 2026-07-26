from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


MODEL_PATH = Path(__file__).parent / "models" / "random_forest_model.joblib"
model = joblib.load(MODEL_PATH)

st.set_page_config(
    page_title="Loan Default Risk Predictor",
)

st.title("Loan Default Risk Predictor")
st.write("Enter origination-time loan details to estimate default risk.")

loan_amnt = st.number_input(
    "Loan amount",
    min_value=500.0,
    value=10000.0,
)

term_months = st.selectbox(
    "Loan term",
    [36, 60],
)

int_rate = st.number_input(
    "Interest rate (%)",
    min_value=0.0,
    value=12.0,
)

sub_grade_options = {
    "A": ["A1", "A2", "A3", "A4", "A5"],
    "B": ["B1", "B2", "B3", "B4", "B5"],
    "C": ["C1", "C2", "C3", "C4", "C5"],
    "D": ["D1", "D2", "D3", "D4", "D5"],
    "E": ["E1", "E2", "E3", "E4", "E5"],
    "F": ["F1", "F2", "F3", "F4", "F5"],
    "G": ["G1", "G2", "G3", "G4", "G5"],
}

grade = st.selectbox(
    "Grade",
    list(sub_grade_options.keys()),
)

sub_grade = st.selectbox(
    "Sub-grade",
    sub_grade_options[grade],
)

emp_length_years = st.number_input(
    "Employment length (years)",
    min_value=0.0,
    max_value=50.0,
    value=5.0,
)

home_ownership = st.selectbox(
    "Home ownership",
    ["RENT", "MORTGAGE", "OWN", "OTHER"],
)

annual_inc = st.number_input(
    "Annual income",
    min_value=0.0,
    value=60000.0,
)

verification_status = st.selectbox(
    "Verification status",
    ["Verified", "Source Verified", "Not Verified"],
)

issue_year = st.number_input(
    "Issue year",
    min_value=2007,
    max_value=2018,
    value=2018,
    step=1,
)

purpose = st.text_input(
    "Loan purpose",
    value="debt_consolidation",
)

dti = st.number_input(
    "Debt-to-income ratio",
    min_value=0.0,
    value=15.0,
)

if st.button("Estimate Risk"):
    input_data = pd.DataFrame([{
        "loan_amnt": loan_amnt,
        "term_months": term_months,
        "int_rate": int_rate,
        "grade": grade,
        "sub_grade": sub_grade,
        "emp_length_years": emp_length_years,
        "home_ownership": home_ownership,
        "annual_inc": annual_inc,
        "verification_status": verification_status,
        "issue_year": issue_year,
        "purpose": purpose,
        "dti": dti,
    }])

    prediction = model.predict(input_data)[0]
    probability_bad = model.predict_proba(input_data)[0, 1]

    if prediction == 1:
        st.error("Higher estimated default risk")
    else:
        st.success("Lower estimated default risk")

    st.metric(
        "Estimated probability of bad outcome",
        f"{probability_bad:.1%}",
    )

    st.warning(
        "This is an educational model estimate, not a lending decision."
    )