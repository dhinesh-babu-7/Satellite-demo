import math
import matplotlib.pyplot as plt

velocity = float(input("Enter the launch velocity:"))
angle = float(input("Enter the launch angle:"))

angle_rad = math.radians(angle)

vx = velocity * math.cos(angle_rad)
vy = velocity * math.sin(angle_rad)

x = 0
y = 0

gravity = -9.81

dt = 0.01

print("\n--- ROCKET INITIAL CONDITIONS ---")
print(f"Velocity X: {vx:.2f} m/s")
print(f"Velocity Y: {vy:.2f} m/s") 
print(f"Position X: {x:.2f} m") 
print(f"Position Y: {y:.2f} m") 

time = 0

x_position = []
y_position = []
time_position = []

print("\n--- SIMULATION START ---") 

while y >= 0:
    
    vy = vy + gravity * dt
    
    x = x + vx*dt 
    y = y + vy*dt
    
    x_position.append(x)
    y_position.append(y)
    time_position.append(time)
    
    
    time = time + dt
    
print("\n--- TRAJECTORY DATA ---")
print(f"Number of Data: {len(x_position)}")
print("\nFirst Five Positions")

for i in range(5):
    print(f"x = {x_position[i]:.2f} m, y = {y_position[i]:.2f} m")
    
print("\n--- SIMULATION COMPLETE ---")
print(f"Flight Time: {time:.2f} s")
print(f"Landing Distance: {x:.2f} m")


max_altitude = max(y_position)
max_distance = max(x_position)

max_altitude_index = y_position.index(max_altitude)

max_time_altitude = time_position[max_altitude_index]

print("\n--- ROCKET RESULTS ---")
print(f"Maximum altitude: {max_altitude:.2f} m")
print(f"Maximum distance: {max_distance:.2f} m")
print(f"Time to maximum altitude: {max_time_altitude:.2f} s")

plt.plot(x_position,y_position)

plt.grid()
plt.show()
