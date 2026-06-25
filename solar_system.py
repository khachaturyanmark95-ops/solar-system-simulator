import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

G = 6.674e-11
M_sun = 1.989e30

planets_data = [
    ["Mercury", 3.285e23, 5.791e10, 47400, "gray"],
    ["Venus", 4.867e24, 1.082e11, 35020, "orange"],
    ["Earth", 5.972e24, 1.496e11, 29780, "blue"],
    ["Mars", 6.390e23, 2.279e11, 24130, "red"]
]

positions = []
velocities = []

for planet in planets_data:
    distance = planet[2]
    velocity = planet[3]
    positions.append([distance, 0.0])
    velocities.append([0.0, velocity])

def calculate_acceleration(position):
    x = position[0]
    y = position[1]
    r = np.sqrt(x**2 + y**2)
    a = -G * M_sun / r**2
    ax = a * x / r
    ay = a * y / r
    return [ax, ay]

def update_positions(dt):
    for i in range(len(planets_data)):
        ax, ay = calculate_acceleration(positions[i])
        velocities[i][0] += ax * dt
        velocities[i][1] += ay * dt
        positions[i][0] += velocities[i][0] * dt
        positions[i][1] += velocities[i][1] * dt

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor("black")
ax.set_xlim(-2.5e11, 2.5e11)
ax.set_ylim(-2.5e11, 2.5e11)
ax.set_aspect("equal")

sun = ax.plot(0, 0, "o", color="yellow", markersize=15)[0]

planet_plots = []
for i, planet in enumerate(planets_data):
    p, = ax.plot(positions[i][0], positions[i][1], "o", color=planet[4], markersize=5)
    planet_plots.append(p)

def animate(frame):
    for step in range(24):
        update_positions(3600)
    for i, p in enumerate(planet_plots):
        p.set_data([positions[i][0]], [positions[i][1]])
    return planet_plots

ani = animation.FuncAnimation(fig, animate, frames=1000, interval=20, blit=True)
plt.title("Solar System Orbital Simulator", color="white")
fig.patch.set_facecolor("black")
plt.show()