````markdown
# 🌍 Flood Risk Prediction System (Kenya)

## 📌 Business Understanding
Flooding is a major environmental and socio-economic challenge in Kenya, impacting infrastructure, agriculture, and human safety. Traditional flood risk assessment methods often lack integration of diverse geospatial factors.

In this project, I built a machine learning-driven system that leverages GIS data to predict flood risk, enabling stakeholders such as urban planners, disaster response teams, and policymakers to make informed decisions.

---

## 📖 Project Overview
This project integrates **Geographic Information Systems (GIS)** and **Machine Learning** to assess flood risk across Kenya.

I implemented two modeling approaches:
- **Classification** → Predict flood risk categories (Low, Moderate, High)
- **Regression** → Predict a continuous flood risk score

The dataset was engineered from multiple geospatial data sources using:
- `GeoPandas`
- `Rasterio`
- `WhiteboxTools`

---

## ❗ Problem Statement
Flood risk prediction is complex due to the interaction of environmental, topographic, and human-related factors.

This project aims to:
- Quantify flood risk using a numerical score
- Categorize regions into actionable risk levels
- Leverage spatial data for predictive modeling

---

## 🎯 Objectives
- Develop a **Flood Risk Score**
- Classify areas into **risk categories**
- Compare **classification vs regression approaches**
- Improve model performance using **ensemble techniques (Voting & Stacking)**
- Deploy a working prediction system

---

## 📊 Metrics of Success

### Classification
- Accuracy  
- F1 Score  
- Confusion Matrix  

### Regression
- R² Score  
- Mean Absolute Error (MAE)  
- Mean Squared Error (MSE)  
- Residual Analysis (Residual Plots)  

---

## 📂 Data Understanding

### 📌 Dataset Features
```python
- county
- nearest_town
- town_size
- landcover_types
- elevation_m
- dist_to_town_m
- dist_to_water_m
- topographic_hazard
- landcover_risk
- water_proximity_risk
- vulnerability_score
- flood_risk_score
- risk_category
````

### 🗺️ Data Sources

#### Landcover Layers

* Bare Areas
* Floodplains
* Forests
* Mangroves
* Protected Areas
* Rangeland
* Sand Beaches
* Urban Areas
* Water Bodies
* Wetlands

#### Elevation

* SRTM 30m DEM (`Kenya_SRTM30meters.tif`)

#### Administrative Data

* Kenyan Counties

#### Town Data

* Kenya Towns dataset

---

## 🧹 Data Cleaning & Feature Engineering

Key steps included:

* Handling missing spatial data
* Creating **distance-based features**:

  * Distance to nearest town
  * Distance to water bodies
* Engineering **risk-based features**:

  * Landcover risk
  * Water proximity risk
  * Topographic hazard
* Generating:

  * `flood_risk_score` (regression target)
  * `risk_category` (classification target)

---

## 📊 Exploratory Data Analysis (EDA)

* Distribution of flood risk scores
* Relationship between elevation and flood risk
* Influence of landcover types
* Effect of proximity to water bodies
* Class distribution analysis

**Key Insight:**
Lower elevation and proximity to water bodies significantly increase flood risk.

---

## ⚙️ Preprocessing

* One-hot encoding for categorical features
* Feature scaling (where necessary)
* Train-test split
* Handling class imbalance

---

## 🤖 Modeling

### 1️⃣ Classification Models

#### Base Models

* Random Forest Classifier
* XGBoost Classifier

#### Ensemble Improvements

* Voting Classifier
* Stacking Classifier (**Best Performing Model**)

#### Evaluation

* Accuracy
* F1 Score
* Confusion Matrix

---

### 2️⃣ Regression Models

#### Models Used

* Random Forest Regressor (**Best Model**)
* XGBoost Regressor

#### Improvements

* Hyperparameter tuning applied

#### Evaluation

* R² Score
* MAE
* MSE
* Residual Plots

---

## 🚀 Deployment

The model was deployed using **Flask** (`app.py`), allowing users to:

* Input environmental and spatial features
* Receive:

  * Flood Risk Score
  * Risk Category

---

## 📁 Project Structure

```bash
Flood-Risk-Prediction/
│
├── data/
│
├── notebooks/
│   ├── 1_creating_dataset.ipynb
│   ├── 2_data_understanding_and_exploration.ipynb
│   ├── 3_data_cleaning_and_feature_engineering.ipynb
│   ├── 4_modeling.ipynb
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
```

---

## 📈 Results Summary

* **Best Classification Model:** Stacking Classifier
* **Best Regression Model:** Random Forest Regressor
* Hyperparameter tuning improved model performance
* Regression provides detailed scoring, while classification improves interpretability

---

## ✅ Conclusions

* GIS-based feature engineering significantly improves predictive performance
* Ensemble models (stacking) enhance classification accuracy
* Random Forest performed best for regression tasks
* Spatial features such as elevation and water proximity are critical predictors

---

## 💡 Recommendations

* Integrate **real-time rainfall/weather data**
* Expand dataset with more **temporal data**
* Develop **interactive dashboards (Tableau / Power BI)**
* Deploy as a **web or mobile application**
* Integrate with **disaster management systems**

---

## 🔮 Future Work

* Time-series flood forecasting
* Deep learning with satellite imagery
* IoT-based flood monitoring systems

---

## 📜 License

This project is licensed under the **BSD 3-Clause License**.

---

## 🙌 Acknowledgements

* Open geospatial datasets
* GIS tools: GeoPandas, Rasterio, WhiteboxTools
* Machine Learning libraries: Scikit-learn, XGBoost

---

```
```
