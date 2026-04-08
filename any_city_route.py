import osmnx as ox
import matplotlib.pyplot as plt

# Step 1: Take city input
city = input("Enter city name: ")

# Load city graph
place_name = city + ", Maharashtra, India"

G = ox.graph_from_place(
    place_name,
    network_type="drive"
)

print("Graph loaded successfully")

# Step 2: Take source and destination
source = input("Enter source location: ")
destination = input("Enter destination location: ")

# Step 3: Geocode locations
source_full = source + ", " + city + ", Maharashtra, India"
destination_full = destination + ", " + city + ", Maharashtra, India"

source_point = ox.geocode(source_full)
destination_point = ox.geocode(destination_full)

print("Source:", source_point)
print("Destination:", destination_point)

# Step 4: Find nearest nodes
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

# Step 5: Shortest path
route = ox.shortest_path(
    G,
    origin,
    dest,
    weight="length"
)

print("Shortest route generated successfully")

# Step 6: Plot route
ox.plot_graph_route(G, route)
plt.show()