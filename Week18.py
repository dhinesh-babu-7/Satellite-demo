import pandas as pd

data = {
    "temperature": [30, 32, 35, 41, 45, 38, 33],
    "battery": [95, 92, 88, 80, 70, 65, 60],
    "altitude": [400, 401, 400, 402, 401, 400, 399]
}

df = pd.DataFrame(data)

print("DATA")
print(df)

print("\nAverage Temperature")
print(df["temperature"].mean())

print("\nMaximum Temperature")
print(df["temperature"].max())

print("\nMINIMUM TEMPERATURE:")
print(df["temperature"].min())

print("\nLow Battery")
print(df[df["battery"] < 50])

print("\nHigh Temperature")
print(df[df["temperature"] > 40])
