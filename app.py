import streamlit as st
import pandas as pd
import pickle

# load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Employee Attrition Prediction")

# ---- USER INPUT ----
age = st.slider("Age", 18, 60)

monthly_income = st.number_input("Monthly Income", 1000, 20000)

job_role = st.selectbox("Job Role", ["Sales Executive","Research Scientist","Laboratory Technician","Manager"])

overtime = st.selectbox("OverTime", ["Yes","No"])

marital_status = st.selectbox("Marital Status", ["Single","Married","Divorced"])

years_at_company = st.slider("Years at Company", 0, 40)

job_satisfaction = st.slider("Job Satisfaction", 1, 4)

# ---- CREATE DATAFRAME ----
input_data = pd.DataFrame({
    "Age":[age],
    "MonthlyIncome":[monthly_income],
    "JobRole":[job_role],
    "OverTime":[overtime],
    "MaritalStatus":[marital_status],
    "YearsAtCompany":[years_at_company],
    "JobSatisfaction":[job_satisfaction]
})

# ---- PREDICT ----
if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Employee likely to leave")
    else:
        st.success("✅ Employee likely to stay")