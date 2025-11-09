import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Page setup
st.set_page_config(page_title="Air Quality Prediction", page_icon="🌤️", layout="centered")

st.title("🌤️ Air Quality Index (AQI) Prediction App")
st.markdown("Enter pollutant levels below to predict the **Air Quality Index (AQI)**.")

# --- Input Section ---
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        pm25 = st.number_input("PM2.5 (µg/m³)", min_value=0.0, value=45.6)
        no2 = st.number_input("NO₂ (µg/m³)", min_value=0.0, value=32.1)
    with col2:
        pm10 = st.number_input("PM10 (µg/m³)", min_value=0.0, value=78.2)
        co = st.number_input("CO (mg/m³)", min_value=0.0, value=0.9)
    with col3:
        so2 = st.number_input("SO₂ (µg/m³)", min_value=0.0, value=20.3)
        o3 = st.number_input("O₃ (µg/m³)", min_value=0.0, value=40.7)

# --- AQI Category Function ---
def aqi_category(aqi_value):
    if aqi_value <= 50:
        return "Good 😊", "🟢"
    elif aqi_value <= 100:
        return "Moderate 🙂", "🟡"
    elif aqi_value <= 200:
        return "Unhealthy for Sensitive Groups 😷", "🟠"
    elif aqi_value <= 300:
        return "Unhealthy 😨", "🔴"
    elif aqi_value <= 400:
        return "Very Unhealthy ☠️", "🟣"
    else:
        return "Hazardous 💀", "⚫"

# --- Buttons Section ---
colA, colB = st.columns(2)
with colA:
    predict = st.button("🔮 Predict AQI", key="predict")
with colB:
    clear = st.button("🧹 Clear Inputs", key="clear")

# --- Prediction Section ---
if predict:
    input_array = np.array([[pm25, pm10, no2, co, so2, o3]], dtype=float)
    prediction = model.predict(input_array)[0]
    st.success(f"Predicted AQI: {prediction:.2f}")

    category, emoji = aqi_category(prediction)
    st.markdown(f"### Air Quality: {emoji} {category}")

    st.progress(min(prediction / 500, 1.0))

elif clear:
    st.rerun()


st.markdown("---")
st.caption("Developed by A.A Singh 💻 | Powered by Streamlit")
