import osmnx as ox

# Pune center point
center_point = (18.5204, 73.8567)

# Download road network
G = ox.graph_from_point(
    center_point,
    dist=2000,
    network_type="drive"
)

print("Graph loaded successfully")
print(G)

# Source point (longitude, latitude)
origin = ox.distance.nearest_nodes(G, 73.8567, 18.5204)

# Destination point (longitude, latitude)
destination = ox.distance.nearest_nodes(G, 73.8700, 18.5300)

print("Origin Node:", origin)
print("Destination Node:", destination)

# Find shortest path
route = ox.shortest_path(G, origin, destination, weight="length")

print("Route Found Successfully")
print("Total Nodes in Route:", len(route))

# Plot route
ox.plot_graph_route(G, route)