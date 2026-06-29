import streamlit as st
import joblib
import numpy as np

# Saved model load karo
model = joblib.load('outputs/house_price_model.pkl')

st.title("California House Price Predictor")
st.write("Enter house details to predict the price")

# Input fields
med_inc = st.slider("Median Income (in $10,000s)", 0.5, 15.0, 5.0)
house_age = st.slider("House Age (years)", 1, 50, 25)
ave_rooms = st.slider("Average Rooms", 1.0, 15.0, 6.0)
ave_bedrms = st.slider("Average Bedrooms", 0.5, 5.0, 1.0)
population = st.slider("Population", 100, 5000, 1000)
ave_occup = st.slider("Average Occupancy", 1.0, 10.0, 3.0)
latitude = st.slider("Latitude", 32.0, 42.0, 34.05)
longitude = st.slider("Longitude", -125.0, -114.0, -118.25)

if st.button("Predict Price"):
    features = np.array([[med_inc, house_age, ave_rooms, ave_bedrms, 
                            population, ave_occup, latitude, longitude]])
    prediction = model.predict(features)
    price = prediction[0] * 100000
    st.success(f"Predicted House Price: ${price:,.2f}")