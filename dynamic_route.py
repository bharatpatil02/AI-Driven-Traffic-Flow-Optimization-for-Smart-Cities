import osmnx as ox
import matplotlib.pyplot as plt

# Load Pune road network
place_name = "Pune, Maharashtra, India"

G = ox.graph_from_place(
    place_name,
    network_type="drive"
)

print("Graph loaded successfully")

# Take user input
source = input("Enter source location: ")
destination = input("Enter destination location: ")

# Convert location names to coordinates
source_point = ox.geocode(source + ", Pune, Maharashtra, India")
destination_point = ox.geocode(destination + ", Pune, Maharashtra, India")

print("Source coordinates:", source_point)
print("Destination coordinates:", destination_point)

# Find nearest graph nodes
origin = ox.distance.nearest_nodes(
    G,
    source_point[1],
    source_point[0]
)

dest = ox.distance.nearest_nodes(
    G,
    destination_point[1],
    destination_point[0]
)

# Find shortest route
route = ox.shortest_path(
    G,
    origin,
    dest,
    weight="length"
)

print("Shortest route generated successfully")

# Plot route
ox.plot_graph_route(G, route)
plt.show()
