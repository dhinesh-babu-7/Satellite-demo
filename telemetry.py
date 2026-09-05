telemetry = [
    {
        "temperature": 24.5,
        "battery": 96,
        "altitude": 400.2,
        "velocity": 7.67
    },
    {
        "temperature": 27.8,
        "battery": 94,
        "altitude": 400.5,
        "velocity": 7.68
    },
    {
        "temperature": 31.2,
        "battery": 92,
        "altitude": 399.9,
        "velocity": 7.67
    },
    {
        "temperature": 28.6,
        "battery": 90,
        "altitude": 400.7,
        "velocity": 7.66
    },
    {
        "temperature": 33.1,
        "battery": 88,
        "altitude": 400.3,
        "velocity": 7.68
    }
]

temperatures = []
batteries = []
altitudes = []
velocities = []

for measurements in telemetry:
    temperatures.append(measurements["temperature"])
    batteries.append(measurements["battery"])
    altitudes.append(measurements["altitude"])
    velocities.append(measurements["velocity"])
    
print("================================")
print("      MINISAT TELEMETRY         ")
print("================================")    
    
print("Temperature Readings")
print("Maximun Temperature:", max(temperatures),"°C")
print("Minimum Temperature:", min(temperatures),"°C")

average_temperature = sum(temperatures) / len(temperatures)

print("Average Temperature:", average_temperature,"°C")


print("Battery Levels")
print("Starting Battery Level:", batteries[0])
print("Ending Battery Level:", batteries[-1])

consumed = batteries[-1] - batteries[0]

print("Battery Consumed:", consumed)

average_altitude = sum(altitudes) / len(altitudes)
print("Average altitude:", average_altitude, "km")

average_velocity = sum(velocities) / len(velocities)
print("Average velocity:", average_velocity, "km/s")