import math

G = 6.67430e-11  # Gravitational constant
M = 5.972e24  # Mass of the Earth

x = 6771000
y = 0

vx = 0
vy = 7670

dt = 1

for step in range(10000):
    
    r = math.sqrt(x**2 + y**2)
    
    ax = -G * M * x / r**3
    ay = -G * M * y / r**3
    
    vx += ax * dt
    vy += ay * dt   
    
    x += vx * dt
    y += vy * dt        
    
    print(f"Step {step}: Position = ({x:.2f}, {y:.2f}), Velocity = ({vx:.2f}, {vy:.2f})")
    