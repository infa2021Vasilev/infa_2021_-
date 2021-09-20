import turtle
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.speed(10)
turtle.shape('turtle')
for i in range(40):
 turtle.forward(10+5*i)
 turtle.right(90)
