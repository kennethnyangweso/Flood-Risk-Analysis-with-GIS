import streamlit as st
import joblib
import pandas as pd

# -----------------------------
# LOAD MODELS & ENCODERS
# -----------------------------
rf_model = joblib.load("flood_risk_regressor.pkl")
clf_model = joblib.load("flood_risk_classifier.pkl")

county_encoder = joblib.load("county_encoder.pkl")
town_encoder = joblib.load("town_encoder.pkl")
town_size_encoder = joblib.load("town_size_encoder.pkl")

features = joblib.load("features.pkl")

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Flood Risk Prediction", layout="centered")

st.title("🌍 Flood Risk Prediction System")
st.markdown("Predict flood risk using environmental and spatial features.")

# -----------------------------
# INPUT SECTION
# -----------------------------
st.subheader("📥 Input Features")

# Categorical inputs
county = st.selectbox("County", county_encoder.classes_)
nearest_town = st.selectbox("Nearest Town", town_encoder.classes_)
town_size = st.selectbox("Town Size", town_size_encoder.classes_)
# Numerical inputs
elevation = st.number_input("Elevation (m)", value=100.0)
dist_town = st.number_input("Distance to Town (m)", value=1000.0)
dist_water = st.number_input("Distance to Water (m)", value=500.0)

topographic_hazard = st.slider("Topographic Hazard", 0.0, 1.0, 0.5)
water_proximity_risk = st.slider("Water Proximity Risk", 0.0, 1.0, 0.5)
vulnerability_score = st.slider("Vulnerability Score", 0.0, 1.0, 0.5)

# -----------------------------
# ENCODE INPUTS
# -----------------------------
county_encoded = county_encoder.transform([county])[0]
town_encoded = town_encoder.transform([nearest_town])[0]

# -----------------------------
# CREATE INPUT DATAFRAME
# -----------------------------
input_data = pd.DataFrame({
    'county': [county_encoded],
    'nearest_town': [town_encoded],
    'town_size': [town_size],
    'elevation_m': [elevation],
    'dist_to_town_m': [dist_town],
    'dist_to_water_m': [dist_water],
    'topographic_hazard': [topographic_hazard],
    'water_proximity_risk': [water_proximity_risk],
    'vulnerability_score': [vulnerability_score]
})

# Align with training features
input_data = input_data.reindex(columns=features, fill_value=0)

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("🔍 Predict Flood Risk"):

    risk_score = rf_model.predict(input_data)[0]
    risk_category = clf_model.predict(input_data)[0]

    st.subheader("📊 Results")

    st.metric("Flood Risk Score", f"{risk_score:.2f}")
    st.metric("Risk Category", risk_category)

    # Visual feedback
    if risk_category == "High":
        st.error("⚠️ High Flood Risk Area")
    elif risk_category == "Medium":
        st.warning("⚠️ Moderate Flood Risk")
    else:
        st.success("✅ Low Flood Risk")