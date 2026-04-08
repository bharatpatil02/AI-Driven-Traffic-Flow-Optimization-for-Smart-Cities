import pandas as pd

features = pd.read_csv("dataset/delhi_traffic_features.csv")
target = pd.read_csv("dataset/delhi_traffic_target.csv")

print("FEATURE COLUMNS:")
print(features.columns)

print("\nTARGET COLUMNS:")
print(target.columns)