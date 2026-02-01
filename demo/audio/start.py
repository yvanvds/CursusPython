import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 6, 300)

y1 = 0.5 * x**2 - 4*x + 3
y2 = 1 * x**2 - 4*x + 3

plt.plot(x, y1)
plt.plot(x, y2)
plt.legend(["x²", "x² - 4x + 3"])
plt.grid()
plt.show()