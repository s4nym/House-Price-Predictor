
import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("house_price_model.pkl")

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

# App title
st.title("🏠 House Price Predictor")
st.write("Enter house details below to predict its price.")

# User inputs
MedInc = st.slider("Median Income in Area (10k USD)", 0.0, 15.0, 5.0)
HouseAge = st.slider("House Age (years)", 1, 100, 20)
AveRooms = st.slider("Average Rooms per Household", 1.0, 15.0, 6.0)
AveBedrms = st.slider("Average Bedrooms per Household", 1.0, 5.0, 1.0)
Population = st.slider("Population in Area", 100, 50000, 1000)
AveOccup = st.slider("Average Occupancy per Household", 1.0, 10.0, 3.0)
Latitude = st.slider("Latitude", 32.0, 42.0, 35.0)
Longitude = st.slider("Longitude", -124.0, -114.0, -120.0)

# Make prediction
if st.button("Predict Price"):
    input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted House Price: **${prediction*100000:,.2f}**")
