import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load data
features = pd.read_csv("dataset/delhi_traffic_features.csv")
target = pd.read_csv("dataset/delhi_traffic_target.csv")

# Merge using Trip_ID
df = pd.merge(features, target, on="Trip_ID")

print("Dataset Loaded Successfully")
print(df.head())

# Drop Trip_ID
df = df.drop("Trip_ID", axis=1)

# Encode categorical columns
label_encoders = {}

categorical_cols = [
    "start_area",
    "end_area",
    "time_of_day",
    "day_of_week",
    "weather_condition",
    "traffic_density_level",
    "road_type"
]

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Split X and y
X = df.drop("travel_time_minutes", axis=1)
y = df["travel_time_minutes"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
mae = mean_absolute_error(y_test, predictions)

print("Model Trained Successfully")
print("Mean Absolute Error:", mae)

# Save model
joblib.dump(model, "traffic_model.pkl")
print("Model saved successfully")