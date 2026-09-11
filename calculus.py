import math

time = [0, 1, 2, 3, 4]
position = [0, 5, 20, 45, 80]

velocity = []
acceleration = []

for i in range(1, len(time)):
    
    change_position = position[i] - position[i - 1]
    change_time = time[i] - time[i - 1]
    
    v = change_position / change_time
    
    velocity.append(v)
    
for i in range(1, len(velocity)):
    
    change_velocity = velocity[i] - velocity[i - 1]
    change_time = time[i] - time[i - 1]
    
    a = change_velocity / change_time
    
    acceleration.append(a)
    
print("Time:", time)
print("Position:", position)
print("Velocity:", velocity)
print("Acceleration:", acceleration)
 