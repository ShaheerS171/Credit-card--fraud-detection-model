import streamlit as st
import pandas as pd
import joblib
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(base_dir, 'model.pkl'))
columns = joblib.load(os.path.join(base_dir, 'columns.pkl'))


st.set_page_config(page_title="Fraud Detector", page_icon="💳")
st.title("💳 Credit Card Fraud Detection")
st.markdown("Fill in the transaction values to predict if it's **fraudulent** or **legit**.")


v17 = st.number_input("V17", format="%.5f")
v12 = st.number_input("V12", format="%.5f")
v14 = st.number_input("V14", format="%.5f")
v16 = st.number_input("V16", format="%.5f")
v10 = st.number_input("V10", format="%.5f")
v11 = st.number_input("V11", format="%.5f")
v18 = st.number_input("V18", format="%.5f")
v9  = st.number_input("V9", format="%.5f")
v7  = st.number_input("V7", format="%.5f")
v4  = st.number_input("V4", format="%.5f")

if st.button("Predict"):
    input_data = pd.DataFrame([{
        'V17': v17, 'V12': v12, 'V14': v14, 'V16': v16, 'V10': v10,
        'V11': v11, 'V18': v18, 'V9': v9, 'V7': v7, 'V4': v4
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legit Transaction.")
