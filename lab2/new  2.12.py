import turtle
import numpy as np
def poluokruznost(r):
    a= 2*r*np.sin(2.5*np.pi/180)
    for i in range(36):
        turtle.forward(a)
        turtle.right(5)
    turtle.forward(a)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.speed(10)
turtle.shape('turtle')
turtle.left(90)
for j in range(4):
    poluokruznost(40)
    poluokruznost(10)
poluokruznost(40)
