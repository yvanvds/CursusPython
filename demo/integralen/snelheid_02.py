import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return 12 + 4 * np.sin(0.6 * t) + 2 * np.sin(2.2 * t)

T = 20          # totale tijd (s)
n = 10          # aantal rechthoeken
dt = T / n

t = np.linspace(0, T, 400)

plt.figure()
plt.plot(t, f(t), label="snelheid")

afstand = 0.0

# rechthoeken tekenen (linkerpunt)
for i in range(n):
    start = i * dt
    plt.plot(
        [start, start, start + dt, start + dt, start],
        [0, f(start), f(start), 0, 0]
    )

    afstand += f(start) * dt # hoogte * breedte

plt.xlabel("tijd (s)")
plt.ylabel("snelheid (m/s)")
plt.title("Afstand benaderen met rechthoeken")
plt.grid(True)
plt.show()

print(f"Benaderde afstand: {afstand:.2f} m")
