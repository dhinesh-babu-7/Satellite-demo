import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
M = 5.972e24
R = 6.371e6

altitude_km = np.linspace(0, 10000, 200)

altitude_m = altitude_km * 1000

r = R + altitude_m

gravity = G * M / r**2

plt.plot(altitude_km, gravity)

plt.title("Gravity vs Altitude")
plt.xlabel("Altitude (km)")
plt.ylabel("Gravity (m/s²)")

plt.grid(True)

plt.show()