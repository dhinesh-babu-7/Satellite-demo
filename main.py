import math

    
while True:
    again = input("Do You want to calculate another satellite? (y/n):").lower()
    if again == "y":
        altitude = float(input("Enter satellite altitude in km:"))

        GM = 3.986e14
        earth_radius = 6371e3

        altitude_m = altitude * 1000
        total_altitude = earth_radius + altitude_m
        altitude_km = total_altitude / 1000

        orbital_velocity = math.sqrt(GM/total_altitude)
        orbital_velocity_km = orbital_velocity / 1000


        print("--- Satellite Information ---")
        print("Altitude: ",altitude,"km")
        print("Distance from the Earth:", altitude_km, "km")
        print("Orbital velocity:", orbital_velocity_km, "km/s")

        if altitude <= 160:
            print("Warning: The altitude is below the minimum for a stable orbit.")
        elif altitude > 160 and altitude <= 2000:
            print("The Satellite is in Low Earth Orbit (LEO)")
        elif altitude > 2000 and altitude < 35786:
            print("The Satellite is in Medium Earth Orbit (MEO)") 
        elif altitude == 35786:
            print("The satellite is approximately in GeoStationary Orbit (GEO)")
        else: 
            print("The satellite is above GeoStationary Orbit (GEO)")
    
    elif again == "n":
        print("--- Exiting the program ---")
        break