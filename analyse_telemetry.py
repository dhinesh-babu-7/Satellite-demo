import pandas as pd

df = pd.read_csv("vyom_telemetry_10000.csv", parse_dates=["timestamp"])

print(df.head())

print(df.describe())