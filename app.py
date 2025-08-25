# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# --- Load Model ---
model = joblib.load("house_price_xgb.pkl")

st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("🏠 House Price Predictor (India)")

st.markdown("""
Enter property details below and get an estimated price!
""")

# --- User Input ---
def user_input_features():
    living_area = st.number_input("Living Area (sq.ft)", min_value=100, max_value=10000, value=1000)
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
    floors = st.number_input("Floors", min_value=1, max_value=5, value=1)
    grade = st.number_input("Grade (House Quality)", min_value=1, max_value=13, value=7)
    lat = st.number_input("Latitude", value=28.61)
    long = st.number_input("Longitude", value=77.20)

    data = {
        'LivingArea': living_area,
        'Bedrooms': bedrooms,
        'Bathrooms': bathrooms,
        'Floors': floors,
        'Grade': grade,
        'Lat': lat,
        'Long': long
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# --- Prediction ---
if st.button("Predict Price"):
    pred_log = model.predict(input_df)[0]
    pred = np.expm1(pred_log)  # undo log-transform
    st.success(f"Estimated House Price: ₹{pred:,.0f}")
