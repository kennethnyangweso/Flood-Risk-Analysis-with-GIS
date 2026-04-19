# ==========================================================
# 🔵 APP 2: CLASSIFICATION (RISK CATEGORY)
# File: app_classification.py
# ==========================================================

# -----------------------------
# CELL 1: IMPORTS
# -----------------------------
import streamlit as st
import joblib
import pandas as pd
import pydeck as pdk

# -----------------------------
# CELL 2: LOAD MODEL
# -----------------------------
model = joblib.load("flood_risk_classifier.pkl")

# -----------------------------
# CELL 3: COUNTY MAPPING
# -----------------------------
county_mapping = {
    1: "Mombasa", 2: "Kwale", 3: "Kilifi", 4: "Tana River", 5: "Lamu",
    6: "Taita Taveta", 7: "Garissa", 8: "Wajir", 9: "Mandera",
    10: "Marsabit", 11: "Isiolo", 12: "Meru", 13: "Tharaka Nithi",
    14: "Embu", 15: "Kitui", 16: "Machakos", 17: "Makueni",
    18: "Nyandarua", 19: "Nyeri", 20: "Kirinyaga", 21: "Murang'a",
    22: "Kiambu", 23: "Turkana", 24: "West Pokot", 25: "Samburu",
    26: "Trans Nzoia", 27: "Uasin Gishu", 28: "Elgeyo Marakwet",
    29: "Nandi", 30: "Baringo", 31: "Laikipia", 32: "Nakuru",
    33: "Narok", 34: "Kajiado", 35: "Kericho", 36: "Bomet",
    37: "Kakamega", 38: "Vihiga", 39: "Bungoma", 40: "Busia",
    41: "Siaya", 42: "Kisumu", 43: "Homa Bay", 44: "Migori",
    45: "Kisii", 46: "Nyamira", 47: "Nairobi"
}
reverse_map = {v: k for k, v in county_mapping.items()}

town_size_mapping = {
    0: "Town",
    1: "Major Town",
    
}   

reverse_map_town_size = {v: k for k, v in town_size_mapping.items()}

# -----------------------------
# CELL 4: FEATURES
# -----------------------------
features = [
    'county','town_size','elevation_m','dist_to_town_m',
    'dist_to_water_m','topographic_hazard',
    'water_proximity_risk','vulnerability_score'
]

# -----------------------------
# CELL 5: UI INPUTS
# -----------------------------
st.title("🟢 Flood Risk Classification")

county = st.selectbox("County", list(county_mapping.values()))
county = reverse_map[county]

town_size = st.selectbox("Town Size", list(town_size_mapping.values()))
town_size = reverse_map_town_size[town_size]

elevation = st.number_input("Elevation (m)")
dist_town = st.number_input("Distance to Town (m)")
dist_water = st.number_input("Distance to Water (m)")
topo = st.slider("Topographic Hazard",0.0,1.0,0.5)
water_risk = st.slider("Water Proximity Risk",0.0,1.0,0.5)
vulnerability = st.slider("Vulnerability Score",0.0,1.0,0.5)

# -----------------------------
# CELL 6: PREDICTION
# -----------------------------
input_df = pd.DataFrame([[county,town_size,elevation,
                         dist_town,dist_water,
                         topo,water_risk,vulnerability]],
                        columns=features)

if st.button("Predict Risk"):
    pred = model.predict(input_df)[0]
    mapping = {0:"High Risk",1:"Low Risk",2:"Moderate Risk"}
    st.success(f"Prediction: {mapping.get(pred,pred)}")