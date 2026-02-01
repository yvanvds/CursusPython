import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return 12 + 4 * np.sin(0.6 * t) + 2 * np.sin(2.2 * t)

# tijd in seconden
t = np.linspace(0, 20, 400)

# snelheid in m/s (bewust wat grillig)
v = f(t)    

plt.figure()
plt.plot(t, v)
plt.xlabel("tijd (s)")
plt.ylabel("snelheid (m/s)")
plt.title("Snelheid van een voertuig in functie van de tijd")
plt.fill_between(t, 0, v, alpha=0.2)
plt.grid(True)
plt.show()
