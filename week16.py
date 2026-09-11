import numpy as np
import matplotlib.pyplot as plt 

g = 9.81

v0 = float(input("Enter the initial velocity (m/s): "))
angle_deg = float(input("Enter the launch angle (degrees): "))

angle_rad = np.radians(angle_deg)

vx = v0 * np.cos(angle_rad)
vy = v0 * np.sin(angle_rad)

flight_time = (2 * vy) / g

time = np.arange(0, flight_time, 0.01)

x = vx * time
y = vy * time - 0.5 * g * time**2

max_height = np.max(y)
max_distance = np.max(x)

print()
print("===== RESULTS =====")
print(f"Horizontal velocity: {vx:.2f} m/s")
print(f"Vertical velocity: {vy:.2f} m/s")
print(f"Flight time: {flight_time:.2f} s")
print(f"Maximum height: {max_height:.2f} m")
print(f"Maximum distance: {max_distance:.2f} m")

plt.plot(x, y)

plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Projectile Motion")

plt.grid()

plt.show()