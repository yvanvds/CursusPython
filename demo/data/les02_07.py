import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 1) data ophalen
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
data = requests.get(url).json()

# 2) lon/lat uit features halen
lons = []
lats = []

for feature in data["features"]:
    coords = feature["geometry"]["coordinates"]  # [lon, lat, depth]
    lons.append(coords[0])
    lats.append(coords[1])

# 3) kaart + punten
img = mpimg.imread("world.png")
plt.figure(figsize=(10, 5))
plt.imshow(img, extent=[-180, 180, -90, 90])
plt.xlim(-180, 180)
plt.ylim(-90, 90)

plt.scatter(lons, lats, s=8)  # s = puntgrootte
plt.title("Aardbevingen (laatste 24 uur)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()