# 🚦 AI-Driven Traffic Flow Optimization for Smart Cities

## 📌 Overview

This project is an AI-powered smart city traffic management system designed to predict traffic congestion and generate optimized routes using Machine Learning and Graph-based Routing algorithms.

The system integrates:

* Traffic prediction using Machine Learning
* Real road network data using OpenStreetMap
* AI-based route optimization
* Alternative route generation
* Smart dashboard monitoring
* Traffic impact evaluation

The main objective of the project is to reduce:

* Traffic congestion
* Travel time
* Fuel consumption
* Air pollution

---

# 🎯 Project Objectives

✅ Predict traffic congestion before it occurs

✅ Generate optimized traffic-aware routes

✅ Suggest multiple alternative routes

✅ Reduce fuel consumption and CO₂ emissions

✅ Support emergency vehicle priority routing

✅ Provide a smart city dashboard interface

---

# 🛠️ Technologies Used

## Programming Language

* Python

## Libraries & Frameworks

* pandas
* scikit-learn
* matplotlib
* networkx
* osmnx
* streamlit
* joblib

## Machine Learning

* Random Forest Regressor

## Mapping & Routing

* OpenStreetMap (OSM)
* OSMnx
* NetworkX

## Dashboard UI

* Streamlit
* React-style Smart Dashboard UI

---

# 📂 Project Structure

```bash
traffic_project/
│
├── dataset/
│   ├── delhi_traffic_features.csv
│   └── delhi_traffic_target.csv
│
├── route.py
├── smart_route.py
├── decision_layer.py
├── alternate_routes.py
├── train_model.py
├── ai_route_optimizer.py
├── dashboard.py
├── evaluation.py
├── dynamic_route.py
├── any_city_route.py
└── traffic_model.pkl
```

---

# 📊 Dataset Features

The dataset contains the following traffic-related features:

* start_area
* end_area
* distance_km
* time_of_day
* day_of_week
* weather_condition
* traffic_density_level
* road_type
* average_speed_kmph

Target Variable:

* travel_time_minutes

---

# 🧠 Machine Learning Model

The project uses a **Random Forest Regression** model to predict travel time.

## Model Performance

| Metric                    | Value    |
| ------------------------- | -------- |
| Mean Absolute Error (MAE) | 1.59 min |

This indicates strong prediction accuracy for traffic travel time estimation.

---

# 🗺️ Real Road Network Integration

The project integrates real-world road maps using:

* OpenStreetMap
* OSMnx

A city road graph is generated where:

* Nodes represent intersections
* Edges represent roads

---

# 🚗 Routing Features

## ✅ Shortest Path Routing

Finds the minimum-distance route.

## ✅ AI-Based Smart Routing

Uses predicted travel time as routing weight.

## ✅ Alternate Route Generation

Generates top 3 optimized alternative routes.

## ✅ Dynamic City Routing

Supports routing for multiple cities such as:

* Pune
* Sangli
* Mumbai
* Delhi
* Bangalore

---

# 📈 Smart Dashboard Features

The dashboard includes:

* Live traffic monitoring
* Route search input
* City dropdown
* Traffic congestion charts
* Suggested routes
* Emergency vehicle priority card
* Smart dark theme UI

---

# 📉 Project Evaluation

| Evaluation Metric | Result     |
| ----------------- | ---------- |
| Time Saved        | 8 min      |
| Fuel Saved        | 0.4 liters |
| CO₂ Reduced       | 0.92 kg    |

---

# ⚡ Installation & Setup

## Step 1 — Clone Repository

```bash
git clone <repository-link>
cd traffic_project
```

## Step 2 — Install Dependencies

```bash
pip install pandas scikit-learn matplotlib networkx osmnx streamlit joblib
```

## Step 3 — Train AI Model

```bash
python train_model.py
```

## Step 4 — Run AI Route Optimizer

```bash
python ai_route_optimizer.py
```

## Step 5 — Run Dashboard

```bash
python -m streamlit run dashboard.py
```

---

# 🔄 Project Workflow

```text
Traffic Dataset
      ↓
Data Preprocessing
      ↓
Machine Learning Model
      ↓
Travel Time Prediction
      ↓
Road Network Graph
      ↓
AI Route Optimization
      ↓
Alternative Routes
      ↓
Smart Dashboard
      ↓
Performance Evaluation
```

---

# 🌍 Real-World Applications

* Smart Cities
* Traffic Management Systems
* Emergency Vehicle Routing
* Logistics & Delivery Optimization
* Urban Planning
* Sustainable Transportation

---

# 🚀 Future Improvements

* Real-time live traffic API integration
* IoT traffic sensor integration
* Google Maps API support
* Live GPS tracking
* AI traffic forecasting using LSTM
* Mobile application deployment

---

# 👨‍💻 Author

**Bharat Patil**

AI & Smart City Traffic Optimization Project

---

# 📜 License

This project is developed for educational and research purposes.
