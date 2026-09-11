import math
import matplotlib.pyplot as plt

G = 6.67430e-11
M = 5.972e24
EARTH_RADIUS = 6.371e6

altitude = 400_000

r0 = EARTH_RADIUS + altitude

x = r0
y = 0

v = math.sqrt(G * M / r0)

vx = 0
vy = v

x_positions = []
y_positions = []

dt = 1
simulation_time = 6000

for step in range(simulation_time):
    
    r = math.sqrt(x**2 + y**2)
    
    ax = -G * M * x / r**3
    ay = -G * M * y / r**3
    
    vx = vx + ax*dt
    vy = vy + ay*dt
    
    x = x + vx*dt
    y = y + vy*dt
    
    x_positions.append(x)
    y_positions.append(y)
    
plt.plot(x_positions, y_positions)

plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Orbit Simulation')
plt.axis('equal')
plt.grid()
plt.show()