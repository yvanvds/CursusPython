import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return np.sin(100*x)

x = np.linspace(-0.1, 0.1, 400)

plt.figure()
plt.plot(x, f(x), label="f(x)")
plt.axhline(0, color="black")
plt.grid()
plt.legend()

def helling(f, x, h=1e-4):
    return (f(x + h) - f(x)) / h

def raaklijn(x, x0, m):
    return m * (x - x0) + f(x0)

x0 = 0.1   # startwaarde

for i in range(5):
    m = helling(f, x0)
    y_tangent = raaklijn(x, x0, m)
    plt.plot(x, y_tangent, "--", alpha=0.7)
    plt.scatter([x0], [f(x0)], color="red")
    plt.title(f"Newton-iteratie {i}")
    plt.pause(2)
    x0 = x0 - f(x0) / m

plt.show()

print(f"De benadering van de nul is x = {x0}")