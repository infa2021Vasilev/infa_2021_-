import turtle as tl
import numpy as np

def shag (d):
	if (d == 1):
		tl.pendown()
	tl.forward(30)
	tl.penup()

def diag (p):
	if (p == 1):
		tl.pendown()
	tl.forward(30*np.power(2,0.5))
	tl.penup()

def cifra(c):
	tl.left(180)
	shag(c[0])
	tl.left(90)
	shag(c[1])
	tl.left(135)
	diag(c[2])
	tl.right(135)
	shag(c[3])
	tl.right(90)
	shag(c[4])
	tl.left(90)
	shag(c[5])
	tl.left(135)
	diag(c[6])
	tl.right(135)
	shag(c[7])
	tl.right(90)
	shag(c[8])
	tl.left(180)
	tl.forward(30)
	tl.left(90)
	tl.forward(60)
	tl.right(90)
	tl.forward(60)

tl.penup()
tl.goto(-200,30)
tl.shape('turtle')
a = [
	(1,1,0,1,0,1,0,1,1),
	(0,0,1,1,0,0,0,1,0),
	(1,0,0,1,0,0,1,0,1),
	(1,0,1,0,1,0,1,0,0),
	(0,1,0,1,1,0,0,1,0),
	(1,1,0,0,1,0,0,1,1),
	(0,0,1,0,1,1,0,1,1),
	(1,0,1,0,0,1,0,0,0),
	(1,1,0,1,1,1,0,1,1),
	(1,1,0,1,1,0,1,0,0),
    ]
b = [1,4,1,7,0,0]
for i in range(6):
	cifra(a[b[i]])