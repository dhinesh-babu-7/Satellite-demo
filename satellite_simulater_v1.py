import math

G = 6.67430e-11
EARTH_MASS = 5.972e24
EARTH_RADIUS = 6371e3

def calculate_orbital_velocity(altitude_km):
    altitude_m = altitude_km * 1000
    orbital_radius = EARTH_RADIUS + altitude_m
    
    velocity = math.sqrt((G*EARTH_MASS)/orbital_radius)
    
    return velocity

def calculate_orbital_period(altitude_km):
    altitude_m = altitude_km * 1000
    orbital_radius = EARTH_RADIUS + altitude_m
    
    period_seconds = (2*math.pi*(math.sqrt(orbital_radius**3/G*EARTH_MASS))) 
    
    return period_seconds

def calculate_gravity(altitude_km):
    altitude_m = altitude_km * 1000
    orbital_radius = EARTH_RADIUS + altitude_m
    
    gravity = (G*EARTH_MASS)/(orbital_radius**2)
    
    return gravity

def calculate_circumference(altitude_km):
    altitude_m = altitude_km * 1000
    orbital_radius = EARTH_RADIUS + altitude_m
    
    circumference = 2*math.pi*orbital_radius
    
    return circumference

def display_report(altitude, mass, velocity, period, gravity, circumference):

    print("\n================================")
    print("   SATELLITE MISSION REPORT")
    print("================================")

    print(f"Altitude          : {altitude:.2f} km")
    print(f"Satellite Mass    : {mass:.2f} kg")
    print(f"Orbital Velocity  : {velocity / 1000:.2f} km/s")
    print(f"Orbital Period    : {period / 60:.2f} minutes")
    print(f"Gravity           : {gravity:.2f} m/s²")
    print(f"Orbit Circumference: {circumference / 1000:.2f} km")

    print("================================")
    
def main():

    print("SATELLITE MISSION SIMULATOR V1")

    while True:

        try:
            altitude = float(
                input("Enter satellite altitude in km: ")
            )

            mass = float(
                input("Enter satellite mass in kg: ")
            )

            if altitude < 0:
                print("Altitude cannot be negative.")
                continue

            if mass <= 0:
                print("Mass must be greater than 0.")
                continue

            velocity = calculate_orbital_velocity(altitude)

            period = calculate_orbital_period(altitude)

            gravity = calculate_gravity(altitude)

            circumference = calculate_circumference(altitude)

            display_report(
                altitude,
                mass,
                velocity,
                period,
                gravity,
                circumference
            )

        except ValueError:
            print("Please enter numbers only.")
            continue


        again = input(
            "\nDo you want to simulate another satellite? (y/n): "
        ).lower()

        if again != "y":
            print("\nSatellite Mission Simulator closed.")
            break


main()