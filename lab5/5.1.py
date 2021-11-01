# -*- coding: utf-8 -*-
import math
import random as rn
import numpy as np
import pygame


FPS = 30
# COLORS
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREY = (125,125,125)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=90, y=450):
        #Constructor of the ball class

        #Args:
        #x - the initial horizontal position of the ball
        #y - the initial vertial position of the ball
        #vx - the initial horizontal velocity of the ball
        #vy - the initial vertical velocity of the ball
        #r - radius of the ball
        #time - the time after which the ball will disappear (3 seconds)
        #color - color, obviously
        #live - when this parameter turns to zero, the ball is removed
        
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = BLACK
        self.time = 90
        self.live = 1

    def move(self):
        #Move the ball after a unit of time has passed.

        #The method describes the movement of the ball in one frame of redrawing. That is, it updates the values

        #self.x and self.y taking into account the speeds of self.vx and self.vy, the force of gravity acting on the ball,
        #and walls at the edges of the window (window size 800x600).
        if(self.x > 800 - self.r):
            self.vx = -1*np.abs(self.vx)
        if(self.x < self.r):
            self.vx = np.abs(self.vx)
        if(self.y > 600 - self.r):
            self.vy += 2
            self.vy = 0.5*np.abs(self.vy)
            self.vy = int(self.vy)
            self.y -= self.vy
            self.vx *= 0.5
            self.vx = int(self.vx)
        if(self.y < self.r + 90):
            self.vy += 2
            self.vy = -0.5*np.abs(self.vy)
            self.vy = int(self.vy)
            self.y -= self.vy
            self.vx *= 0.5
            self.vx = int(self.vx)
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 2
        self.vy = int(self.vy)
        self.vx = int(self.vx)
        self.time -= 1
        

    def draw(self):
        #Draws a ball
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj, i):
        #The function checks whether this object collides with the target described in the obj object.

        #Args:
        #  obj: The object with which the collision is checked.
        #Returns:
        #  Returns True if the ball and the object collide. Otherwise returns False. And also turning live into zero.
        if(((self.x - obj.x)*(self.x - obj.x) + (self.y - obj.y)*(self.y - obj.y)) <= (self.r + obj.r)*(self.r + obj.r) and obj.zaderzka == 0):
            self.live = 0
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        #Constructor of the ball class
        
        #Args:
        #screen - pygame.display object
        #puska - pygame.surface object
        #f2_power - how strong will the cannon fire
        #f2_on - if it is '1', cannon is charging
        #an - 
        #color - color, again :-)
        
        self.screen = screen
        self.puska = pygame.Surface((360,360),pygame.SRCALPHA)
        self.f2_power = 10
        self.f2_on = 0
        self.an = 0
        self.color = GREY

    def fire2_start(self, event):
        #starts cannon's charging
        #occurs when the mouse button is down.
        
        self.f2_on = 1
        self.color = RED

    def fire2_end(self, event):
        #ball shot.

        #occurs when the mouse button is released.
        #the initial values of the ball velocity components vx and vy depend on the mouse position and f2_power. 
        #returns the cannon to its initial state.
        
        global balls
        new_ball = Ball(self.screen)
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.an *= -1
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        self.color = GREY

    def targetting(self, event):
        #Aiming. Depends on the mouse position.
        
        self.an = math.atan2(-1*(event.pos[1]-450), (event.pos[0]-90))
        

    def draw(self, screen):
        #draws a cannon and rotating it
        
        self.puska = pygame.Surface((360,360),pygame.SRCALPHA)
        pygame.draw.polygon(self.puska, self.color, [(90 + int(5*np.cos(self.an + 1.57)),
                                                      90 - int(5*np.sin(self.an + 1.57))),
                                                      
                                                     (90 + int(5*np.cos(self.an - 1.57)),
                                                      90 - int(5*np.sin(self.an - 1.57))),
                                                      
                                                     (90 + int(np.power((30+self.f2_power/2)*(30+self.f2_power/2)+5*5, 0.5)*np.cos(self.an - 5/(30+self.f2_power/2))),
                                                      90 - int(np.power((30+self.f2_power/2)*(30+self.f2_power/2)+5*5, 0.5)*np.sin(self.an - 5/(30+self.f2_power/2)))),
                                                      
                                                     (90 + int(np.power((30+self.f2_power/2)*(30+self.f2_power/2)+5*5, 0.5)*np.cos(self.an + 5/(30+self.f2_power/2))),
                                                      90 - int(np.power((30+self.f2_power/2)*(30+self.f2_power/2)+5*5, 0.5)*np.sin(self.an + 5/(30+self.f2_power/2))))])
        screen.blit(self.puska, (0, 360))

    def power_up(self):
        #cannon's charging
        if self.f2_on:
            if self.f2_power < 70:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        #Constructor of Target's class
        
        #Args:
        #x - the initial horizontal position of the target
        #y - the initial vertial position of the target
        #vx - the initial horizontal velocity of the target
        #vy - the initial vertical velocity of the target
        #r - radius of the target
        #color - color, yes, again :D
        #zaderzka - delaying before next target spawning
        
        self.x = rn.randint(600, 780)
        self.y = rn.randint(300, 550)
        self.r = rn.randint(15, 50)
        self.vx = rn.randint(-15,15)
        self.vy = rn.randint(-15,15)
        self.color = rn.choice(GAME_COLORS)
        self.zaderzka = 0

    def new_target(self):
        #Initialising of a new target
        
        self.x = rn.randint(600, 780)
        self.y = rn.randint(300, 550)
        self.r = rn.randint(15, 50)
        self.vx = rn.randint(-15,15)
        self.vy = rn.randint(-15,15)
        self.color = rn.choice(GAME_COLORS)
        self.zaderzka = 60

    def hit(self):
        #Collision with a ball
        
        global points
        points += 1

    def draw(self, screen):
        #draws a target
        
        if(self.zaderzka == 0):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
    def move(self):             
        #makes target move
    
        if(self.zaderzka == 0):
            if(self.x > 800 - self.r):
                self.vx = rn.randint(-15,0)
                self.vy = rn.randint(-15,15)
            if(self.x < self.r):
                self.vx = rn.randint(0,15)
                self.vy = rn.randint(-15,15)
            if(self.y > 600 - self.r):
                self.vy = rn.randint(-15,0)
                self.vx = rn.randint(-15,15)
            if(self.y < self.r + 90):
                self.vy = rn.randint(0,15)
                self.vx = rn.randint(-15,15)
            self.x += self.vx
            self.y += self.vy
        else:
            self.zaderzka -= 1
    def collision(self, Balls, i):  
        # checks if balls collided and pushes them
        
        for j in range(i,5):
            if((i != j) and ((np.power(Balls[i].x - Balls[j].x,2) + np.power(Balls[i].y - Balls[j].y,2)) < np.power(Balls[i].r + Balls[j].r,2)) 
                              and (Balls[j].zaderzka == 0) 
                              and (Balls[i].zaderzka == 0)):
                sin = (Balls[i].y - Balls[j].y)/int(np.power(np.power(Balls[i].x - Balls[j].x,2) + np.power(Balls[i].y - Balls[j].y,2), 1/2))
                cos = (Balls[i].x - Balls[j].x)/int(np.power(np.power(Balls[i].x - Balls[j].x,2) + np.power(Balls[i].y - Balls[j].y,2), 1/2))
                vj = int(np.power(np.power(Balls[j].vx, 2) + np.power(Balls[j].vy, 2), 1/2))
                vi = int(np.power(np.power(Balls[i].vx, 2) + np.power(Balls[i].vy, 2), 1/2))
                Balls[i].vx = vj*cos
                Balls[i].vy = vj*sin
                Balls[j].vx = -1*vi*cos
                Balls[j].vy = -1*vi*sin

def tablichka(score, a, b, size):
    #Draws a score and 'restart' botton
    
    #s - object of pygame.Surface
    s = pygame.Surface((a, b), pygame.SRCALPHA)
    
    myfont = pygame.font.SysFont('arial', size)
    textsurface = myfont.render(score, False, (0, 0, 0))
    pygame.draw.rect(s,GREEN,(0,0,a,b),0)
    pygame.draw.rect(s,BLACK,(0,0,a,b),1)
    u = myfont.size(score)
    s.blit(textsurface,(int((a - u[0])/2),int((b - u[1])/2)))
    s = pygame.transform.smoothscale(s, (a, b))
    screen.blit(s, (0,0))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

balls = []
targets = [0]*5
for i in range(5):
    targets[i] = Target()
global points
points = 0
restarting = 0
clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    for i in range(5):
        targets[i].draw(screen)
    for b in balls:
        b.draw()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] <= 180 and event.pos[1] <= 90):           #Checks if you clicked botton 'restart'
                del balls[0:len(balls)]
                for i in range(5):
                    targets[i].hit()
                    targets[i].new_target()
                points = 0
                restarting = 1
            else:
                gun.fire2_start(event)
        elif (event.type == pygame.MOUSEBUTTONUP):
            if (restarting == 0):
                gun.fire2_end(event)
            else:
                restarting = 0
        elif event.type == pygame.MOUSEMOTION:
            puska = gun.targetting(event)
    gun.draw(screen)
    for i in range(5):
        targets[i].move()
        targets[i].collision(targets, i)
    for i in range(len(balls)):
        balls[i].move()
        for j in range (5):
            if (balls[i].hittest(targets[j], i)):
                targets[j].live = False
                targets[j].hit()
                targets[j].new_target()
    l = 0
    for i in range(len(balls)):
        if (balls[i - l].time == 0 or balls[i - l].live == 0):
            del balls[i - l]
            l += 1
    gun.power_up()
    tablichka('Your points are: ' + str(points), 800, 90, 60)
    tablichka('RESTART', 180, 90, 40)
    pygame.display.update()

pygame.quit()
