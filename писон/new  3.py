import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, np.log((x*x+1)*np.exp(-np.abs(x)/10))/np.log(1 + np.tan(1/(1 + np.power(np.sin(x),2)))))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()