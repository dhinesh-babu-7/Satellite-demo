import pandas as pd
import random
from datetime import datetime, timedelta

rows = []

start_time = datetime(2026, 1, 1, 0, 0, 0)

for i in range(10000):
    timestamp = start_time + timedelta(seconds=i)
    temperature = random.uniform(20, 45)
    battery = 100 - (i / 10000) * 40
    altitude = random.uniform(398, 402)
    velocity = random.uniform(7.6, 7.8)
    latitude = random.uniform(8, 37)
    longitude = random.uniform(68, 97)
    pressure = random.uniform(980, 1020)
    
    rows.append({
        "timestamp": timestamp,
        "temperature": temperature,
        "battery": battery,
        "altitude": altitude,
        "velocity": velocity,
        "latitude": latitude,
        "longitude": longitude,
        "pressure": pressure
    })
    
df = pd.DataFrame(rows)

df.to_csv("vyom_telemetry_10000.csv", index=False)

print("VYOM TELEMETRY")
print(df.head())
print(df.tail())
print(df.shape)