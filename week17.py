# import matplotlib.pyplot as plt
# import numpy as np

# time = np.linspace(0, 10,100)

# velocity = 10 * time 
# distance = 5 * time**2

# plt.plot(time, velocity, label='Velocity')
# plt.plot(time, distance, label='Distance')

# plt.xlabel('Time (s)')
# plt.ylabel('Value')
# plt.title('Simple Plot')
# plt.legend()

# plt.grid()

# plt.show()






# fig, ax = plt.subplots()

# ax.plot([1, 2, 3], [2, 4, 6])

# ax.set_xlabel("Time")
# ax.set_ylabel("Distance")
# ax.set_title("Distance vs Time")

# ax.grid()

# plt.show()







# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# fig, ax = plt.subplots()

# x_data = []
# y_data = []

# line, = ax.plot([], [])

# ax.set_xlim(0, 10)
# ax.set_ylim(0, 10)


# def update(frame):

#     x_data.append(frame)
#     y_data.append(frame)

#     line.set_data(x_data, y_data)

#     return line,


# animation = FuncAnimation(
#     fig,
#     update,
#     frames=10,
#     interval=200
# )

# plt.show()





import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


radius = 10

angles = np.linspace(0, 2 * np.pi, 360)

orbit_x = radius * np.cos(angles)
orbit_y = radius * np.sin(angles)


fig, ax = plt.subplots()

ax.set_aspect("equal")

ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)

ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")
ax.set_title("Satellite Orbit Simulation")

ax.grid()


# Earth
ax.plot(
    0,
    0,
    marker="o",
    markersize=20
)


# Full orbit
ax.plot(
    orbit_x,
    orbit_y,
    linestyle="--"
)


# Satellite trail
trail, = ax.plot([], [])


# Satellite
satellite, = ax.plot(
    [],
    [],
    marker="o",
    markersize=8
)


def update(frame):

    satellite.set_data(
        [orbit_x[frame]],
        [orbit_y[frame]]
    )

    trail.set_data(
        orbit_x[:frame + 1],
        orbit_y[:frame + 1]
    )

    return satellite, trail


animation = FuncAnimation(
    fig,
    update,
    frames=len(angles),
    interval=20,
    blit=True
)


plt.show()