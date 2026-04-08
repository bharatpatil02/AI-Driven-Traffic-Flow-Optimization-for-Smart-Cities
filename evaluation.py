# Project performance evaluation

normal_route_time = 35   # minutes
ai_route_time = 27       # minutes

fuel_per_minute = 0.05   # liters
co2_per_liter = 2.31     # kg CO2

# Time saved
time_saved = normal_route_time - ai_route_time

# Fuel saved
fuel_saved = time_saved * fuel_per_minute

# CO2 saved
co2_saved = fuel_saved * co2_per_liter

print("===== PROJECT EVALUATION =====")
print("Normal Route Time:", normal_route_time, "min")
print("AI Route Time:", ai_route_time, "min")
print("Time Saved:", time_saved, "min")
print("Fuel Saved:", round(fuel_saved, 2), "liters")
print("CO2 Reduction:", round(co2_saved, 2), "kg")