import numpy as np

def trapezium(f, a, b, n):
    # jouw code hier
    oppervlakte = 0.0

    dt = (b - a) / n
    for i in range(n):
        start = a + i * dt
        einde = a + (i + 1) * dt

        h_start = f(start)
        h_einde = f(einde)

        # oppervlakte trapezium = gemiddelde hoogte * breedte
        oppervlakte += (h_start + h_einde) / 2 * dt
    return oppervlakte

def f(t):
    return 12 + 4*np.sin(0.6*t) + 2*np.sin(2.2*t)

print(trapezium(f, 0, 20, 5))
print(trapezium(f, 0, 20, 10))
print(trapezium(f, 0, 20, 100))