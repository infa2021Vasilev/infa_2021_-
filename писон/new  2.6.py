import turtle

turtle.shape('turtle')
turtle.goto(0,0)
for i in range(11):
 turtle.forward(50)
 turtle.stamp()
 turtle.right(180)
 turtle.forward(50)
 turtle.right(180+360/11)
