import numpy as np
import matplotlib.pyplot as plt
def ver(x):
 s = 0
 for i in range(1, 1000):
  s += np.power(1/2,i)*np.cos(np.power(3,i)*np.pi*x)
 return s
x = np.arange(-1, 1.01, 0.0001)
plt.plot(x, ver(x))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()