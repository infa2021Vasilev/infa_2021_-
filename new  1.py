import numpy as np
x = [1,10,1000]
y = np.log((1/(np.exp(np.sin(x)+1)))/(5/4 + 1/np.power(x,(1/5))))/np.log(1 + np.power(x,2))
print(y)