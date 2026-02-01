import numpy as np

def f(t):
    return 12 + 4 * np.sin(0.6 * t) + 2 * np.sin(2.2 * t)

t = np.linspace(0, 20, 400)
v = f(t)

afstand = np.trapezoid(v, t)
print(f"Exacte afstand (met numpy.trapezoid): {afstand:.2f} m")