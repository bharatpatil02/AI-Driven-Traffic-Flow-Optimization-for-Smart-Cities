import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from itertools import islice

# Step 1: Load graph
center_point = (18.5204, 73.8567)

G = ox.graph_from_point(
    center_point,
    dist=2000,
    network_type="drive"
)

# Step 2: Convert to DiGraph
G_simple = nx.DiGraph()

for u, v, data in G.edges(data=True):
    weight = data.get("length", 1)
    G_simple.add_edge(u, v, smart_cost=weight)

print("Converted graph successfully")

# Step 3: Source and destination
origin = ox.distance.nearest_nodes(G, 73.8567, 18.5204)
destination = ox.distance.nearest_nodes(G, 73.8700, 18.5300)

# Step 4: Get only first 3 shortest routes
path_generator = nx.shortest_simple_paths(
    G_simple,
    origin,
    destination,
    weight="smart_cost"
)

top_routes = list(islice(path_generator, 3))

# Step 5: Print routes
for i, route in enumerate(top_routes, 1):
    print(f"Route {i}: {len(route)} nodes")

# Step 6: Plot routes
ox.plot_graph_routes(G, top_routes)
plt.show()