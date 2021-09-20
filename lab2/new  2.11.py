import turtle
import numpy as np
def okruznost(l,r):
    a= 2*r*np.sin(0.5*np.pi/180)
    for i in range(360):
        turtle.forward(a)
        turtle.left(l)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.speed(10)
turtle.shape('turtle')
turtle.left(90)
for j in range(5):
    okruznost(1,40+5*j)
    okruznost(-1,40+5*j)
	
