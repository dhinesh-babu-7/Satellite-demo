import math

velocity = float(input("Enter the Velocity of the satellite : "))
angle_sat = float(input("Enter the Angle of the satellite:"))

angle_rad = math.radians(angle_sat)

vx = velocity*math.cos(angle_rad)
vy = velocity*math.sin(angle_rad)

print()
print("=== Satellite Direction ===")
print()
print("Velocity:", velocity,"m/s")
print("Angle:", angle_sat)
print("Angle Radian:", angle_rad)
print()
print("X component:", vx, "m/s")
print("Y component:", vy, "m/s")
print()

if vx < 0:
    print("Satellite moves left")
elif vx > 0:
    print("Satellite moves right")
else:
    print("Satellite has no horizontal movement")


if vy < 0:
    print("Satellite moves downward")
elif vy > 0:
    print("Satellite moves upward")
else:
    print("Satellite has no vertical movement")