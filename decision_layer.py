import osmnx as ox
import matplotlib.pyplot as plt

# Step 1: Load map
center_point = (18.5204, 73.8567)

G = ox.graph_from_point(
    center_point,
    dist=2000,
    network_type="drive"
)

print("Graph loaded successfully")

# Step 2: Assign predicted travel time + congestion penalty
for u, v, key, data in G.edges(keys=True, data=True):
    road_length = data.get("length", 1)

    # estimated speed km/h
    avg_speed = 30

    # convert to travel time in minutes
    travel_time = (road_length / 1000) / avg_speed * 60

    # congestion penalty
    congestion_penalty = 2

    # final road cost
    data["smart_cost"] = travel_time + congestion_penalty

# Step 3: Source and destination
origin = ox.distance.nearest_nodes(G, 73.8567, 18.5204)
destination = ox.distance.nearest_nodes(G, 73.8700, 18.5300)

# Step 4: Smart routing
smart_route = ox.shortest_path(
    G,
    origin,
    destination,
    weight="smart_cost"
)

print("Smart decision route generated")

# Step 5: Plot
ox.plot_graph_route(G, smart_route)
plt.show()