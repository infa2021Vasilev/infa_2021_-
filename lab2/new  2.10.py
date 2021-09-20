import turtle
import numpy as np
def okruznost(l):
    for i in range(240):
        turtle.forward(1)
        turtle.left(1.5*l)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.speed(10)
turtle.shape('turtle')
for j in range(4):
    okruznost(1)
    okruznost(-1)
    turtle.left(180/4)
	
