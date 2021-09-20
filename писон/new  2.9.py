import turtle
import numpy as np
def n_ugolnik(n):
    turtle.left((180*(n-2)/n)/2)
    for i in range(n):
        turtle.left(180-(180*(n-2)/n))
        turtle.forward(2*(10*np.power(3,0.5)+10*(n-3))*np.sin(np.pi/n))
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.speed(10)
turtle.shape('turtle')
for j in range(3,13):
    turtle.pendown()
    n_ugolnik(j)
    turtle.right((180*(j-2)/j)/2)
    turtle.penup()
    turtle.forward(10)
