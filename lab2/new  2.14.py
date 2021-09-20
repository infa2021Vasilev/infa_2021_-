import turtle
import numpy as np
def zvezda(n):
    for i in range(n):
	    turtle.forward(150)
	    turtle.right(180-180/n)
turtle.shape('turtle')
zvezda(5)
turtle.penup()
turtle.goto(180,0)
turtle.pendown()
zvezda(11)

	
