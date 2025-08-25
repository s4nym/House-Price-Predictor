# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# --- Load model ---
model = joblib.load("house_price_xgb.pkl")

st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("🏠 House Price Predictor (India)")
st.markdown("Enter the property details below to estimate the price:")

# --- User Inputs ---
def user_input_features():
    data = {
        'number of bedrooms': st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3),
        'number of bathrooms': st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2),
        'living area': st.number_input("Living Area (sq.ft)", min_value=100, max_value=10000, value=1000),
        'lot area': st.number_input("Lot Area (sq.ft)", min_value=100, max_value=20000, value=5000),
        'number of floors': st.number_input("Number of Floors", min_value=1, max_value=5, value=1),
        'waterfront present': st.selectbox("Waterfront Present?", [0, 1]),
        'number of views': st.number_input("Number of Views", min_value=0, max_value=5, value=0),
        'condition of the house': st.number_input("Condition of the House (1-5)", min_value=1, max_value=5, value=3),
        'grade of the house': st.number_input("Grade of the House (1-13)", min_value=1, max_value=13, value=7),
        'Area of the house(excluding basement)': st.number_input("Area of House (Excl. Basement)", min_value=100, max_value=10000, value=1000),
        'Area of the basement': st.number_input("Area of Basement", min_value=0, max_value=5000, value=0),
        'Built Year': st.number_input("Built Year", min_value=1800, max_value=2025, value=2000),
        'Renovation Year': st.number_input("Renovation Year", min_value=1800, max_value=2025, value=2000),
        'Postal Code': st.number_input("Postal Code", min_value=100000, max_value=999999, value=110001),
        'Lattitude': st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=28.61, format="%.5f"),
        'Longitude': st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=77.20, format="%.5f"),
        'living_area_renov': st.number_input("Living Area Renovation", min_value=0, max_value=10000, value=0),
        'lot_area_renov': st.number_input("Lot Area Renovation", min_value=0, max_value=20000, value=0),
        'Number of schools nearby': st.number_input("Number of Schools Nearby", min_value=0, max_value=50, value=5),
        'Distance from the airport': st.number_input("Distance from Airport (km)", min_value=0, max_value=500, value=20)
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# --- Prediction ---
if st.button("Predict Price"):
    pred_log = model.predict(input_df)[0]
    pred = np.expm1(pred_log)  # undo log-transform
    st.success(f"Estimated House Price: ₹{pred:,.0f}")