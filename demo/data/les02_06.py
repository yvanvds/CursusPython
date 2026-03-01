import requests
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Interactieve modus inschakelen
plt.ion()

# 1) Figuur en kaart één keer maken
img = mpimg.imread("world.png")

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(img, extent=[-180, 180, -90, 90])
ax.set_xlim(-180, 180)
ax.set_ylim(-90, 90)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title("Live ISS positie")

# 2) Eerste punt aanmaken (start op 0,0)
point = ax.scatter(0, 0, color="red", s=100)

url = "http://api.open-notify.org/iss-now.json"

while True:
    # Nieuwe data ophalen
    data = requests.get(url).json()

    lat = float(data["iss_position"]["latitude"])
    lon = float(data["iss_position"]["longitude"])

    # Puntpositie aanpassen
    point.set_offsets([lon, lat])

    # Figuur verversen
    plt.pause(0.1)

    # 5 seconden wachten
    time.sleep(5)