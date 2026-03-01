import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 1) data ophalen
url = "http://api.open-notify.org/iss-now.json"
data = requests.get(url).json()

lat_str = data["iss_position"]["latitude"]
lon_str = data["iss_position"]["longitude"]

lat = float(lat_str)
lon = float(lon_str)

# 2) kaart tonen
img = mpimg.imread("world.png")
plt.figure(figsize=(10, 5))
plt.imshow(img, extent=[-180, 180, -90, 90])
plt.xlim(-180, 180)
plt.ylim(-90, 90)

# 3) punt toevoegen
plt.scatter(lon, lat, color="red", s=100, label="ISS")
plt.title("ISS positie (1 meting)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.show()