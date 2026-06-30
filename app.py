import streamlit as st
import requests

st.title("Customer Churn Predictor")

# Input fields
tenure = st.slider("Tenure (months)", 0, 72, 12)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
monthly_charges = st.slider("Monthly Charges", 18.0, 120.0, 65.0)

# When button is clicked
if st.button("Predict Churn"):
    data = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": tenure,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": contract,
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": monthly_charges,
        "TotalCharges": monthly_charges * tenure
    }
    
    response = requests.post("https://customer-churn-predictor-7kix.onrender.com/predict", json=data)
    result = response.json()
    
    st.metric("Churn Probability", f"{result['churn_probability']*100:.1f}%")
    if result['prediction'] == 1:
        st.error("⚠️ This customer is likely to churn!")
    else:
        st.success("✅ This customer is unlikely to churn.")
    # Build the data dict and call the FastAPI endpoint
