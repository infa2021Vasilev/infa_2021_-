import turtle
import numpy as np
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.speed(0)
turtle.shape('turtle')
a = ((1 + 5/180)*np.sin(2*np.pi/180))
b = ((1+5/180)*np.cos(2*np.pi/180)-(1 + 5/180))
turtle.left(np.arctan(a/b)*180/np.pi)
for i in range(36000):
 a = ((1 + 5/180*(i+1))*np.sin(2*np.pi/180))
 b = ((1+5/180*(i+1))*np.cos(2*np.pi/180)-(1 + 5/180*i))
 turtle.forward(np.power(a*a + b*b,0.5))
 turtle.left(2)
