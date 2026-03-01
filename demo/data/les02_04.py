import matplotlib.pyplot as plt
# extra matplotlib import voor afbeeldingen
import matplotlib.image as mpimg

# laad de afbeelding
img = mpimg.imread("world.png")

plt.figure(figsize=(10, 5))
plt.imshow(img, extent=[-180, 180, -90, 90])  # longitude/latitude bereik
plt.xlim(-180, 180)
plt.ylim(-90, 90)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Wereldkaart als achtergrond")
plt.show()