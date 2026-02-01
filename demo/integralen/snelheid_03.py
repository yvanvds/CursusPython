
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return 12 + 4 * np.sin(0.6 * t) + 2 * np.sin(2.2 * t)

T = 20          # totale tijd (s)
n = 20          # aantal trapezia
dt = T / n

t = np.linspace(0, T, 400)

plt.figure()
plt.plot(t, f(t), label="snelheid")

afstand = 0.0

# trapezia tekenen
for i in range(n):
    start = i * dt
    einde = (i + 1) * dt

    h_start = f(start)
    h_einde = f(einde)

    # trapezium omtrek tekenen: linksonder -> linksboven -> rechtsboven -> rechtsonder -> terug
    plt.plot(
        [start, start, einde, einde, start],
        [0,     h_start, h_einde, 0,     0]
    )

    # oppervlakte trapezium = gemiddelde hoogte * breedte
    afstand += (h_start + h_einde) / 2 * dt

plt.xlabel("tijd (s)")
plt.ylabel("snelheid (m/s)")
plt.title("Afstand benaderen met trapezia")
plt.grid(True)
plt.show()

print(f"Benaderde afstand: {afstand:.2f} m")

