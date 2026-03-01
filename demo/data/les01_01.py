import pandas as pd
import numpy as np

t = np.trapz

df = pd.read_csv("temperature-anomaly.csv")

#result =df.dtypes#
#print(result)

# result = df.shape
# print(result)

# result = df.dtypes
# print(result)

filter = df["Entity"] == "Northern Hemisphere"
north = df[filter]

result = north.head()
print(result)

# print(df[df["Entity"] == "Northern Hemisphere"].head())

#print(df["Entity"].unique())

#print(north["Year"].mean())

baseline = north[(north["Year"] >= 1861) & (north["Year"] <= 1890)]
print(baseline["Average"].mean() )

np.trape

# years = north["Year"] # kies je kolom
# anomaly = north["Average"] # kies je kolom

# south = df[df["Entity"] == "Southern hemisphere"] 

# import matplotlib.pyplot as plt

# plt.figure()
# plt.plot(north["Year"], north["Average"], label="Northern Hemisphere")
# plt.plot(south["Year"], south["Average"], label="Southern Hemisphere")
# plt.xlabel("Year")
# plt.ylabel("Temperature anomaly (°C)")
# plt.title("Northern Hemisphere temperature anomaly")
# plt.legend()
# plt.grid(True)
# plt.show()


