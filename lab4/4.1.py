import pygame as pg
import numpy as np
import random as rn
pg.init()

FPS = 30
screen = pg.display.set_mode((1200, 700))

#COLORS:
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def click(event,x,y,r):
    #Main function
    #checks if you clicked on any balls, delets the balls you clicked, sets the delay before the next ball appears, counts points
    global points
    for i in range(10):
        if((np.power((event.pos[0] - x[i]), 2) + np.power((event.pos[1] - y[i]), 2)) <= (np.power(r[i], 2))):
            points = points + 1											#counting points
			
            pg.draw.circle(screen, (0,0,0), (x[i],y[i]), r[i], 0)		#deleting a ball
			
            x[i] = rn.randint(100,700)									#creating parameters of a new ball
            y[i] = rn.randint(150,500)
            r[i] = rn.randint(30,50)
            vx[i] = rn.randint(-10,10)
            vy[i] = rn.randint(-10,10)
            color[i] = COLORS[rn.randint(0, 5)]
			
            zaderzka[i] = 60											#delaying of a new ball spawning


def tablichka(score):
    #Main function
    #Draws a score
    
    #s - object of pygame.Surface
    s = pg.Surface((1200, 90), pg.SRCALPHA)
    
    myfont = pg.font.SysFont('arial', 60)
    textsurface = myfont.render(score, False, (0, 0, 0))
    pg.draw.rect(s,GREEN,(0,0,1200,90),0)
    u = myfont.size(score)
    s.blit(textsurface,(int((1200 - u[0])/2),0))
    screen.blit(s, (0,0))

clock = pg.time.Clock()
finished = False

global points			
points = 0				#score
x = [0]*10				#x coordinate
y = [0]*10				#y coordinate
r = [0]*10				#radius
vx = [0]*10				#x velocity
vy = [0]*10				#y velocity
color = [0]*10			#color
zaderzka = [0]*10   	#delaying

for i in range(10):						#creating ball's parameters
    x[i] = rn.randint(100,700)
    y[i] = rn.randint(150,500)
    r[i] = rn.randint(30,50)
    vx[i] = rn.randint(-15,15)
    vy[i] = rn.randint(-15,15)
    color[i] = COLORS[rn.randint(0, 5)]

while not finished:
    clock.tick(FPS)
	
    for i in range(10):
        if(zaderzka[i] == 0):
            pg.draw.circle(screen, color[i], (x[i], y[i]), r[i])
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            click(event,x,y,r)
    pg.display.update()
    screen.fill(BLACK)
	
    for i in range(10):								#movement and bounce of balls
        if(zaderzka[i] == 0):
            x[i] += vx[i]
            y[i] += vy[i]
            if(x[i] > 1200 - r[i]):
                vx[i] = rn.randint(-15,0)
                vy[i] = rn.randint(-15,15)
            if(x[i] < r[i]):
                vx[i] = rn.randint(0,15)
                vy[i] = rn.randint(-15,15)
            if(y[i] > 700 - r[i]):
                vy[i] = rn.randint(-15,0)
                vx[i] = rn.randint(-15,15)
            if(y[i] < (r[i]+90)):
                vy[i] = rn.randint(0,15)
                vx[i] = rn.randint(-15,15)
        else:
            zaderzka[i] -= 1
	
    tablichka('Your points are: ' + str(points))  	#showing score
print("Your points are ",points)
pg.quit()