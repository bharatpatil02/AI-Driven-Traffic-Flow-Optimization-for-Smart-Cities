import osmnx as ox
import joblib
import pandas as pd
import matplotlib.pyplot as plt

model = joblib.load("traffic_model.pkl")

center_point = (18.5204, 73.8567)

G = ox.graph_from_point(
    center_point,
    dist=2000,
    network_type="drive"
)

print("Graph loaded successfully")

for u, v, key, data in G.edges(keys=True, data=True):
    road_length = data.get("length", 100)

    sample_input = pd.DataFrame([{
        "start_area": 1,
        "end_area": 2,
        "distance_km": road_length / 1000,
        "time_of_day": 1,
        "day_of_week": 2,
        "weather_condition": 0,
        "traffic_density_level": 1,
        "road_type": 0,
        "average_speed_kmph": 30
    }])

    predicted_time = model.predict(sample_input)[0]
    data["ai_weight"] = predicted_time

origin = ox.distance.nearest_nodes(G, 73.8567, 18.5204)
destination = ox.distance.nearest_nodes(G, 73.8700, 18.5300)

route = ox.shortest_path(
    G,
    origin,
    destination,
    weight="ai_weight"
)

print("AI optimized route generated")

fig, ax = ox.plot_graph_route(G, route)
plt.show()