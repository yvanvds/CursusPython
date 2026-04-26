import numpy as np
import matplotlib.pyplot as plt
 
def f(x): 
    return x**2 - 5*x + 4 

 

def helling(f, x, h=1e-4): 
    return (f(x + h) - f(x)) / h 

 

def raaklijn(x, x0, m): 
     return m * (x - x0) + f(x0) 

 

x = np.linspace(-1, 6, 400) 

 

plt.plot(x, f(x), label="f(x)") 

plt.axhline(0) 

plt.grid() 

plt.legend() 

 

x0 = 4.5 

 

for i in range(4): 
    m = helling(f, x0) 

    y_tangent = raaklijn(x, x0, m) 

 

    plt.plot(x, y_tangent, "--", alpha=0.7) 

    plt.scatter([x0], [f(x0)], color="red") 

    plt.pause(2) 

 

    x0 = x0 - f(x0) / m 

 

plt.show() 

 

print("Benadering van nul:", x0) 