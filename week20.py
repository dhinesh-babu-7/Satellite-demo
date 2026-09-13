import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.integrate import solve_ivp


# =====================================
# 1. CONSTANTS
# =====================================

G = 6.67430e-11
M = 5.972e24

earth_radius = 6_371_000


# =====================================
# 2. SATELLITE INPUT
# =====================================

altitude = 400_000


# =====================================
# 3. ORBITAL RADIUS
# =====================================

r = earth_radius + altitude


# =====================================
# 4. ORBITAL VELOCITY
# =====================================

velocity = np.sqrt(G * M / r)


print("Orbital radius:", r, "m")
print("Orbital velocity:", velocity, "m/s")


# =====================================
# 5. INITIAL STATE
# =====================================

initial_state = [
    r,
    0,
    0,
    velocity
]


# =====================================
# 6. ORBIT EQUATIONS
# =====================================

def orbit(t, state):

    x, y, vx, vy = state

    r = np.sqrt(x**2 + y**2)

    ax = -G * M * x / r**3

    ay = -G * M * y / r**3

    return [vx, vy, ax, ay]


# =====================================
# 7. RUN SCIPY SIMULATION
# =====================================

result = solve_ivp(
    orbit,
    [0, 6000],
    initial_state,
    max_step=10
)


# =====================================
# 8. EXTRACT DATA
# =====================================

time = result.t

x = result.y[0]
y = result.y[1]

vx = result.y[2]
vy = result.y[3]


# =====================================
# 9. CALCULATE SPEED
# =====================================

speed = np.sqrt(vx**2 + vy**2)


# =====================================
# 10. CALCULATE ACCELERATION
# =====================================

r_values = np.sqrt(x**2 + y**2)

ax = -G * M * x / r_values**3

ay = -G * M * y / r_values**3

acceleration = np.sqrt(ax**2 + ay**2)


# =====================================
# 11. CREATE TELEMETRY TABLE
# =====================================

telemetry = pd.DataFrame({

    "time": time,

    "x": x,

    "y": y,

    "velocity": speed,

    "acceleration": acceleration

})


print("\nTelemetry:")
print(telemetry.head())


# =====================================
# 12. TELEMETRY ANALYSIS
# =====================================

print("\nMaximum velocity:",
      telemetry["velocity"].max())

print("Minimum velocity:",
      telemetry["velocity"].min())

print("Average velocity:",
      telemetry["velocity"].mean())


# =====================================
# 13. SAVE CSV
# =====================================

telemetry.to_csv(
    "telemetry_v2.csv",
    index=False
)

print("\nTelemetry saved!")


# =====================================
# 14. ORBIT GRAPH
# =====================================

plt.plot(x, y)

plt.scatter(0, 0)

plt.axis("equal")

plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")

plt.title("Satellite Orbit - V2")

plt.show()


# =====================================
# 15. VELOCITY GRAPH
# =====================================

plt.plot(time, speed)

plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")

plt.title("Satellite Velocity")

plt.show()


# =====================================
# 16. ACCELERATION GRAPH
# =====================================

plt.plot(time, acceleration)

plt.xlabel("Time (seconds)")
plt.ylabel("Acceleration (m/s²)")

plt.title("Satellite Acceleration")

plt.show()