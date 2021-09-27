import turtle as tl
import numpy as np
import random as rn

tl.shape('turtle')
for i in range (50):
	tl.forward(rn.randint(1,30))
	tl.right(rn.randint(-180,180))