
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
- Accuracy  (75%)
- F1 Score  (75%)
- Confusion Matrix  

### Regression
- R² Score  (70%)
- Mean Absolute Error (MAE)  (0.5)
- Mean Squared Error (MSE) (0.5) 
- Residual Analysis (Residual Plots)  

---

## 📂 Data Understanding

### 📌 Dataset Features

1. **county**  
- The administrative region in Kenya where the data point is located. This categorical feature enables geographic grouping and regional analysis of flood risk patterns.

2. **nearest_town**  
- The closest town to the given location. This helps capture spatial relationships and accessibility to urban centers.

3. **town_size**  
- A categorical indicator of the size of the nearest town (e.g., small, medium, large). It reflects the level of urbanization and infrastructure development in nearby areas.

4. **landcover_types**  
- The dominant land cover classification of the area (e.g., forest, urban, wetland, rangeland). This feature is critical in understanding how surface characteristics influence flood behavior.

5. **elevation_m**  
- The elevation of the location in meters above sea level, derived from DEM data. Lower elevations are generally more prone to flooding.

6. **dist_to_town_m**  
- The distance (in meters) from the location to the nearest town. This helps measure remoteness and potential access to infrastructure and drainage systems.

7. **dist_to_water_m**  
- The distance (in meters) from the location to the nearest water body (e.g., river, lake). Areas closer to water sources are typically at higher flood risk.

8. **topographic_hazard**  
- A derived feature representing terrain-related flood risk, calculated using elevation and slope. It captures how landscape structure influences water accumulation and flow.

9. **landcover_risk**  
- A risk score assigned based on land cover type. For example, wetlands and floodplains may have higher risk scores compared to forests or bare land.

10. **water_proximity_risk**  
- A derived risk metric based on distance to water bodies. Shorter distances correspond to higher flood risk.

11. **vulnerability_score**  
- A composite score representing overall susceptibility to flooding. It combines multiple risk factors such as land cover, proximity to water, and topographic characteristics.

12. **flood_risk_score**  
- A continuous numerical value representing the predicted level of flood risk. This is the target variable for the regression model.

13. **risk_category**  
- A categorical classification of flood risk (e.g., Low, Moderate, High) derived from the flood risk score. This is the target variable for the classification model.


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

## Spatial view of the dataset

<img width="1020" height="1143" alt="image" src="https://github.com/user-attachments/assets/f1ad7bc1-b5b6-4944-b287-3d252182289b" />

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

* Distribution of numeric features (eg flood risk score)
* Relationship between elevation and flood risk
* Influence of landcover types
* Effect of proximity to water bodies
* Class distribution analysis

### 📊 Visuals 
<img width="1190" height="790" alt="image" src="https://github.com/user-attachments/assets/76e2224b-3f49-41a0-84f1-c9005eb3a658" />

Elevation & Proximity: Most data points represent low-lying areas (peaking under 1,000m) that are relatively close to towns (peaking between 0 and 20,000m).
Water Proximity: The dist_to_water_m graph shows a high concentration of data around a very specific, large-scale value (or 10,000 km), which may indicate a data normalization issue or that most locations in this dataset are extremely far from a primary water source.

<img width="640" height="428" alt="image" src="https://github.com/user-attachments/assets/af13301e-6011-4b51-8688-4aafb2f13517" />

Balanced Distribution: All three categories are relatively close in size, with only a 6.5% difference between the largest (High Risk) and smallest (Moderate Risk) segments.
Moderate Risk is the smallest: This category accounts for 30.9% of the total frequency.

<img width="900" height="552" alt="image" src="https://github.com/user-attachments/assets/12df00f6-6556-4817-a278-7639f45a3eb9" />

- Coastal Crisis: The two highest-risk counties are Lamu and Mombasa, both scoring near 3.0. This indicates that coastal flooding (likely driven by sea-level rise and storm surges) is the most severe threat in this model.
- Riverine Risk: Garissa and Tana River follow closely. This aligns with their geographic position along the Tana River basin, which is prone to heavy seasonal flooding.

<img width="682" height="475" alt="image" src="https://github.com/user-attachments/assets/bfabc866-7cfb-44c7-b94d-d68baa501032" />

- Negative Correlation: There is a clear inverse relationship; as elevation increases, the maximum flood risk score significantly decreases.
- Lowland Concentration: The highest risk scores (above 4.0) are almost exclusively found at elevations below 500 meters. These likely represent coastal zones or deep river basins.

<img width="682" height="475" alt="image" src="https://github.com/user-attachments/assets/a77c083c-bd7f-40e9-80b3-32de36ab2861" />

- Massive Distance Values: The x-axis (Distance to Water) uses scientific notation ( 10^7), showing distances between 9,600 km and 10,400 km. This is significantly larger than the width of most countries, suggesting these values might be measured from a specific global reference point or indicate a scaling issue in the dataset.
- Peak Risk Clusters: The highest risk scores (>50) are concentrated on the left side of the graph (shorter distances relative to the rest of the set).

<img width="790" height="590" alt="image" src="https://github.com/user-attachments/assets/d52ba9cf-7575-4fc3-9123-ff806d807fbc" />

- Observation: Garissa has the highest count of risk points, far exceeding any other county with over 1,100.
- Insight: The vast majority of its points fall under the High Risk category (dark purple). For your analysis, Garissa represents the most critical region for urgent flood mitigation and infrastructure investment.

<img width="901" height="807" alt="image" src="https://github.com/user-attachments/assets/0b13680d-b661-40a0-9871-4108da2f9751" />

- Landcover is the strongest predictor: landcover_risk has the highest positive correlation with flood_risk_score (0.77). This confirms that the type of ground surface (like impermeable urban areas or saturated wetlands) is the single most influential factor in your risk model.
- Topography is a major secondary factor: topographic_hazard also shows a strong positive correlation (0.66) with the final risk score. Areas with hazardous terrain features (like low-lying basins) are significantly more likely to be high-risk.

<img width="844" height="702" alt="image" src="https://github.com/user-attachments/assets/70f420fe-bda9-4e70-92d3-9d9eeb4415c7" />

- Clear Risk Segmentation: The risk categories (High, Moderate, Low) are neatly separated along Principal Component 1 (PC1). As PC1 increases from left to right, the risk transitions from Low to High.
- PC1 is the Primary Driver: Accounting for 44.9% of the variance, PC1 is the strongest mathematical indicator of risk. Based on your project's previous charts, PC1 likely represents a combination of Elevation (negative) and Landcover Risk (positive).

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

### Evaluation

* Accuracy
* F1 Score
* Confusion Matrix

#### Results 

Classification Model Performance

| Model                          | Accuracy (%) | F1 Score (%) |
|--------------------------------|-------------|--------------|
| Random Forest Classifier       | 81.07       | 80.93        |
| XGBoost Classifier             | 80.97       | 80.86        |
| Ensemble Voting Classifier     | 81.31       | 81.17        |
| **Ensemble Stacking Classifier** | **81.93**   | **81.84**    |

---

🔍 Insights


- The **Ensemble Stacking Classifier** achieved the best performance, indicating that combining multiple models in a hierarchical manner improves predictive power.
- Both **Random Forest** and **XGBoost** performed similarly, showing strong baseline performance for tree-based models.
- The **Voting Classifier** provided a slight improvement over individual models, but not as significant as stacking.
- The close performance across models suggests that the dataset is well-structured, and further gains may come from feature engineering rather than model complexity.
- The consistency between **Accuracy** and **F1 Score** indicates a balanced model performance across classes.



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

| Model                          | R-Squared (%) | MAE        | MSE  |     
|--------------------------------|-------------|--------------|----------|
| Random Forest Regressor   | 71       | 0.31                 |   0.24   |
| XGBoost Regressor              | 70     |  0.32      |    0.25  |
| **Tuned  Random Forest Regressor** | **72**      | **0.31**        |  **0.23**    |
| Tuned XGBoost Regressor        | 71   | 0.32   |     0.24 |

---

### Best Model Results:

#### **Classification (Stacked Ensemble Model)**

<img width="649" height="547" alt="image" src="https://github.com/user-attachments/assets/6c8d3988-f978-4ead-bbf0-934d3e79a7f8" />

##### **Observations for Confusion Matrix - Stacked Ensemble Model:**  
- Superior Safety Margin: Only 8 actual High Risk areas were misclassified as Low Risk. This is the lowest "critical failure" rate of all the models you've evaluated, making it the safest choice for disaster planning.
- Extremely Low "False Alarm" Rate: Only 27 High Risk predictions were actually Low Risk. This high precision ensures that when you call for an evacuation or structural reinforcement, the data strongly supports it.
- Moderate Risk "Buffer": The most frequent errors are still between Moderate and Low Risk (176 and 123). This confirms that "Moderate" continues to act as a statistical middle ground between the clear extremes of high and low.
- High True Positive Counts: The primary diagonal (983, 773, 620) shows the highest volume of correct hits across the entire analysis.

<img width="1123" height="547" alt="image" src="https://github.com/user-attachments/assets/0b152ba9-6266-4fd0-8b24-133f84c18920" />

##### **Observations for Feature Importance - Stacked Ensemble Model:**  
- The "Hazard" Heavyweight: topographic_hazard is the overwhelming driver for the XGBoost component (green), accounting for over 80% of its logic. This ensures the model is highly sensitive to dangerous terrain shapes.
- The "Physicality" Anchor: Random Forest (blue) provides the necessary balance by prioritizing raw physical geography: elevation_m, dist_to_water_m, and dist_to_town_m.
- Complementary Strengths: Notice how the blue and green bars often don't overlap. Where XGBoost ignores physical distance, Random Forest captures it; where Random Forest is less certain about topographic hazard, XGBoost anchors it.
- Minimal Variables: town_size and water_proximity_risk contribute almost nothing to either model, suggesting they can be safely excluded from future iterations.

#### **Regression**

<img width="790" height="590" alt="image" src="https://github.com/user-attachments/assets/a0d6d2d3-df9e-4e24-a752-6541f8f244d6" />

##### **Observations for Scatter Plot - Random Forest Regressor (Actual vs Predicted):**  

- Strong Positive Linear Correlation: The data points cluster tightly around the dashed red line (the "Identity Line"), indicating that the model's predictions closely track the real-world values across the entire range.
- Vertical Banding: The data is organized in distinct vertical columns at specific "Actual Values" (e.g., at 0.4, 0.8, 1.4, 3.2, 3.7). This confirms that your target variable is derived from weighted categories or specific thresholds.
- Central Tightness: The model is most accurate in the 0.5 to 3.5 range. This is where the majority of your "Towns" and "Rangelands" sit, making the model highly reliable for the bulk of your study area.
- Under-prediction at the Top: For the most extreme actual values (
), the blue dots fall below the red line. This means the model tends to be slightly conservative, under-predicting the absolute worst flood scenarios.

<img width="968" height="547" alt="image" src="https://github.com/user-attachments/assets/6f44f2ce-ecd7-4d05-81c8-3af2d1bc0c99" />

##### **Observations for Feature Importance - Random Forest Regressor:**  

- The Primary Driver: elevation_m is the overwhelming dominant feature, with a score exceeding 0.45. This confirms that in your model, vertical height is the single most important factor for predicting flood intensity.
- The Secondary Tier: Three features share a similar level of importance (between ~0.13 and ~0.17):
   - dist_to_water_m
   - topographic_hazard
   - dist_to_town_m
- Low Impact Features: county and vulnerability_score provide very little predictive power (<0.05>).
- Non-Factors: town_size and water_proximity_risk have scores of zero, meaning they do not contribute to the model's decisions at all.


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
├── risk_category_app.py
├── flood_score_app.py
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
