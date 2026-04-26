import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Instellingen
# ----------------------------
breedte = 600
hoogte = 400
max_iter = 20

x_min, x_max = -2.2, 1.0
y_min, y_max = -1.2, 1.2

# ----------------------------
# Complex vlak maken
# ----------------------------
x = np.linspace(x_min, x_max, breedte)
y = np.linspace(y_min, y_max, hoogte)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y

Z = np.zeros_like(C)

# Hierin bewaren we wanneer een punt ontsnapt
uitkomst = np.full(C.shape, max_iter, dtype=int)

# Masker: welke punten zijn nog actief?
actief = np.ones(C.shape, dtype=bool)

# ----------------------------
# Figuur voorbereiden
# ----------------------------
plt.ion()
fig, ax = plt.subplots(figsize=(8, 5))

img = ax.imshow(
    uitkomst,
    extent=(x_min, x_max, y_min, y_max),
    cmap="viridis",
    origin="lower",
    vmin=0,
    vmax=max_iter
)

ax.set_title("Mandelbrot – iteratie 0")
ax.set_xlabel("Re")
ax.set_ylabel("Im")

plt.show(block=False)

# ----------------------------
# Iteraties
# ----------------------------
for i in range(max_iter):
    # Enkel actieve punten verder berekenen
    Z[actief] = Z[actief] ** 2 + C[actief]

    # Punten die nu ontsnappen
    ontsnapt = (np.abs(Z) > 2) & actief

    # Bewaar bij welke iteratie ze ontsnapten
    uitkomst[ontsnapt] = i

    # Deze punten hoeven we niet meer te berekenen
    actief[ontsnapt] = False

    # Beeld verversen
    img.set_data(uitkomst)
    ax.set_title(f"Mandelbrot – iteratie {i + 1}")
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.3)

plt.ioff()
plt.show()