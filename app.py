import streamlit as st
import pandas as pd
import pickle

# 1. Model Load karna
model = pickle.load(open('random_forest_model.pkl', 'rb'))

st.title("Telco Customer Churn Prediction 📉")

# 2. User se Input lena
tenure = st.number_input("Tenure (Months)", min_value=0, max_value=72, value=12)
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=50.0)
total_charges = st.number_input("Total Charges ($)", min_value=0.0, value=500.0)

# Dropdowns for categorical data (Simple example)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

# 3. Prediction Logic
if st.button("Predict Churn"):
    # Yahan aapko user input ko waisa hi banana padega jaisa model training ke waqt tha
    # (One-Hot Encoding aur Scaling apply karna padega real project mein)
    
    # Dummy prediction for demonstration (Real mein input ko preprocess karein)
    # input_data = pd.DataFrame([[tenure, monthly_charges, total_charges]], columns=['tenure', 'MonthlyCharges', 'TotalCharges'])
    # prediction = model.predict(input_data)
    
    # Example output:
    st.write("Prediction logic needs preprocessing steps same as notebook!")
    # st.success(f"Customer Churn: {'Yes' if prediction[0] == 1 else 'No'}")