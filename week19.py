import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

G = 6.67430e-11
M = 5.972e24

def orbit(t, state):

    x, y, vx, vy = state

    r = np.sqrt(x**2 + y**2)

    ax = -G * M * x / r**3
    ay = -G * M * y / r**3

    return [vx, vy, ax, ay]


earth_radius = 6_371_000
altitude = 400_000

r = earth_radius + altitude

velocity = np.sqrt(G * M / r)

initial_state = [
    r,
    0,
    0,
    velocity
]

result = solve_ivp(
    orbit,
    [0, 6000],
    initial_state,
    max_step=10
)

x = result.y[0]
y = result.y[1]

plt.plot(x, y)
plt.scatter(0, 0)

plt.axis("equal")
plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")
plt.title("Satellite Orbit using SciPy")

plt.show()