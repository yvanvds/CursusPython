import scipy.integrate as sci
import numpy as np

def f(t):
    return 12 + 4*np.sin(0.6*t) + 2*np.sin(2.2*t)

afstand, fout = sci.quad(f, 0, 20)

print(f"Exacte afstand (met scipy.quad): {afstand:.2f} m")
print(f"Geschatte fout: {fout:.2e} m")