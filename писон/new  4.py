import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
y = input()
with plt.xkcd():
   plt.plot(x, eval(y))
   plt.xlabel(r'$x$')
   plt.ylabel(r'$f(x)$')
   plt.grid(True)
   plt.show()