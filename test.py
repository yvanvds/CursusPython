import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 300)

#   * $ f(x)=x^3 $
#   * $ f(x)=\sin(x) $
#   * $ f(x)=e^x $

y = x**3
y2 = np.sin(x)
y3 = np.exp(x)

plt.plot(x, y, label="x^3")
plt.plot(x, y2, label="sin(x)")
#plt.plot(x, y3, label="exp(x)")
plt.legend()
plt.grid(True)
plt.show()