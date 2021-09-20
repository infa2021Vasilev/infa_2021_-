import turtle

turtle.shape('turtle')
turtle.goto(0,0)
x = 0
y = 0
for i in range(10):
 turtle.pendown()
 for j in range(4):
  turtle.forward(10+10*i)
  turtle.right(90)
 turtle.penup()
 x -= 5
 y += 5
 turtle.goto(x,y)
