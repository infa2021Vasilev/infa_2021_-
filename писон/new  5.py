import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
p, v = np.polyfit(x, y, deg=1, cov=True)
p1, v1 = np.polyfit(x, y, deg=2, cov=True)
p_f1 = np.poly1d(p)
p_f2 = np.poly1d(p1)
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, p_f1(x), x, p_f2(x))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()