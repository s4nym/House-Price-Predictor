import streamlit as st
import numpy as np
import joblib
import requests

# Load trained model
model = joblib.load("house_price_model.pkl")

# Get real-time USD→INR conversion
def get_usd_to_inr():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url).json()
        return response["rates"]["INR"]
    except:
        return 83  # fallback value if API fails

USD_TO_INR = get_usd_to_inr()

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

# App title
st.title("🏠 House Price Predictor (INR)")
st.write("Enter details below to estimate a house price in Indian Rupees (₹).")

# User-friendly inputs
income = st.slider("Median Household Income (in Lakhs ₹)", 1, 50, 10)   # e.g. ₹10L
house_age = st.slider("House Age (years)", 1, 100, 20)
rooms = st.slider("Number of Rooms", 1, 10, 5)
bedrooms = st.slider("Number of Bedrooms", 1, 5, 2)
population = st.slider("Population in Area", 500, 30000, 5000, step=500)
occupancy = st.slider("Average Occupancy per Household", 1, 10, 3)
latitude = st.slider("Latitude", 32, 42, 35)
longitude = st.slider("Longitude", -124, -114, -120)

# Make prediction
if st.button("Predict Price"):
    # Convert inputs to match dataset scale
    MedInc = income / 0.83  # approx conversion: ₹10L ~ $12k (rough scaling)
    AveRooms = float(rooms)
    AveBedrms = float(bedrooms)
    AveOccup = float(occupancy)

    input_data = np.array([[MedInc, house_age, AveRooms, AveBedrms, population, AveOccup, latitude, longitude]])
    
    prediction_usd = model.predict(input_data)[0]
    prediction_inr = prediction_usd * 100000 * USD_TO_INR
    
    st.success(f"💰 Predicted House Price: **₹{prediction_inr:,.0f}**")
    st.caption(f"(Using live USD→INR rate: {USD_TO_INR:.2f})")