import random as rn
import turtle


number_of_turtles = 20
steps_of_time_number = 1000


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
i = 0
x = [0]*20
y = [0]*20
vx = [0]*20
vy = [0]*20
for unit in pool:
    unit.penup()
    unit.speed(50)
    x[i] = rn.randint(-200, 200)
    y[i] = rn.randint(-200, 200)
    vx[i] = rn.random()*20*rn.randint(-1, 1)
    vy[i] = rn.random()*20*rn.randint(-1, 1)
    unit.goto(x[i], y[i])
    i += 1


for i in range(steps_of_time_number):
    j = 0
    for unit in pool:
        x[j] = x[j] + vx[j]
        y[j] = y[j] + vy[j]
        unit.goto(x[j],y[j])
        if x[j] > 300 or x[j] < -300:
            vx[j] = -1*vx[j]
        if y[j] > 300 or y[j] < -300:
            vy[j] = -1*vy[j]
        j = j + 1
    