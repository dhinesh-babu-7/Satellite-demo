import csv

def analyze_data(name, values):
    
    print()
    print("===", name,"Analysis ===")
    
    print("Maximum:", max(values))
    print("Minimum:", min(values))
    print("Average:",round(sum(values)/len(values),2))
    
    
def health_check(temperature, battery, velocity, altitude, reading):
    
    anomaly = False
    
    if temperature < -20:
        print("⚠️ WARNING: Battery is critically low!")
        print("Reading:", reading)
        print("Battery:", battery)
        anomaly = True
        
    if temperature > 80:
        print("⚠️ WARNING: Temperature is too high!")
        print("Reading:", reading)
        print("Temperature:", temperature)
        anomaly = True

    if temperature < -20:
        print("⚠️ WARNING: Temperature is too low!")
        print("Reading:", reading)
        print("Temperature:", temperature)
        anomaly = True

    if altitude > 420:
        print("⚠️ WARNING: Satellite altitude is too high!")
        print("Reading:", reading)
        print("Altitude:", altitude)
        anomaly = True

    if altitude < 380:
        print("⚠️ WARNING: Satellite altitude is too low!")
        print("Reading:", reading)
        print("Altitude:", altitude)
        anomaly = True

    if velocity > 8.0:
        print("⚠️ WARNING: Satellite velocity is too high!")
        print("Reading:", reading)
        print("Velocity:", velocity)
        anomaly = True

    if velocity < 7.5:
        print("⚠️ WARNING: Satellite velocity is too low!")
        print("Reading:", reading)
        print("Velocity:", velocity)
        anomaly = True
        
    if not anomaly:
        print("Reading within safe limits") 
        
    print()
    
temperature_values = []
battery_values = []
altitude_values = []
velocity_values = []


with open ("telemetry.csv", "r", newline="") as file:
    
    reader = csv.reader(file)
    
    next(reader)
    
    for reading_values, row in enumerate(reader, start=1):
        
        if not row:
            continue
        
        if row[0] == "temperature":
            continue
        
        temperature = float(row[0])
        battery = float(row[1])
        altitude = float(row[2])
        velocity = float(row[3])
        
        temperature_values.append(temperature)
        battery_values.append(battery)
        altitude_values.append(altitude)
        velocity_values.append(velocity)
                    
        print("=== Satellite Telemetry ===")
        print("Reading:", reading_values)
        print("Temperature:", temperature)
        print("Battery:", battery)
        print("Altitude:", altitude)
        print("Velocity:", velocity)
        print()
        
        health_check(
            temperature,
            battery,
            altitude,
            velocity,
            reading_values
        )
        
print()
print("================================")
print("      SATELLITE REPORT")
print("================================")

analyze_data("Temperature", temperature_values)
analyze_data("Battery", battery_values)
analyze_data("Altitude", altitude_values)
analyze_data("Velocity", velocity_values)