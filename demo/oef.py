
import numpy as np 
import matplotlib.pyplot as plt 

def f(x): 
    return x**3 - 4*x + 1 

a = 0
b = 4 

x = np.linspace(a, b, 400) 
y = f(x) 

plt.plot(x, y) 
plt.axhline(0) 
plt.grid() 

for i in range(10): 
    m = (a + b) / 2 
    if f(a) * f(m) < 0: 
        b = m 
    else: 
        a = m 
    plt.axvline(m, color='red', linestyle='--') 
    plt.pause(1)    

plt.show() 