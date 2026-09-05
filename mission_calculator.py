import math

GM = 3.986e14
earth_radius = 6371e3

def orbital_velocity(altitude):
    
    altitude_m = altitude * 1000
    r = earth_radius + altitude_m
    velocity = math.sqrt(GM/r)
    
    return velocity

def gravity(altitude):
    
    altitude_m = altitude * 1000
    r = earth_radius + altitude_m
    
    g = GM / r**2
    
    return g

def orbital_period(altitude):
    
    altitude_m = altitude * 1000
    r = earth_radius + altitude_m
    
    velocity = orbital_velocity(altitude)
    
    period = (2 * math.pi * r) / velocity
    
    return period
    
altitude = float(input("Enter satellite altitude in km:"))

print()
print("--- Satellite Information ---")
print()
print("Altitude:", altitude, "km")
print("Orbital Velocity:", orbital_velocity(altitude)/1000, "km/s")
print("Gravity:", gravity(altitude), "m/s^2")
print("Orbital Period:", orbital_period(altitude), "s")
