import matplotlib.pyplot as plt

locations = {
    "Chennai": (13.08, 80.27),
    "Bengaluru": (12.97, 77.59),
    "Hyderabad": (17.39, 78.49),
    "Mumbai": (19.08, 72.88),
    "New Delhi": (28.61, 77.21)
}

for city, (lat, lon) in locations.items():
    plt.scatter(lat, lon)
    plt.text(lat, lon, city)
    
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Indian Locations")
plt.show()