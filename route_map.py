import osmnx as ox

center_point = (18.5204, 73.8567)   # Pune center

G = ox.graph_from_point(
    center_point,
    dist=2000,
    network_type="drive"
)

print("Graph loaded successfully")
print(G)

ox.plot_graph(G)