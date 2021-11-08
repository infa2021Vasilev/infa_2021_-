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

class Hole: 
    def __init__(self, screen: pygame.Surface, x: int, y: int):
        #Constructor of a Hole class
        
        #Args:
        #x - the initial horizontal position of the hole
        #y - the initial vertial position of the hole
        #vx - the initial horizontal velocity of the hole
        #vy - the initial vertical velocity of the hole
        #r - radius of the hole
        #time - the time after which the hole will disappear (3 seconds)
        #color - color
        #live - when this parameter turns to zero, the ball is removed
        #hit - when this parameter is 1 hole begins expanding (till radius becomes 200)
        #recharging - the time required to prepare a new hole for the shot
        
        self.screen = screen
        self.x = x + 90
        self.y = y + 90
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = BLACK
        self.live = 1
        self.hit = 0
        self.recharging = 0
    def move(self):
        #Move the hole after a unit of time has passed.

        #The method describes the movement of the hole and it's expanding in one frame of redrawing. That is, it updates the values
        
        if((self.x > 715) or (self.x < 85) or (self.y > 600 - self.r) or (self.y < self.r + 90) or (self.hit == 1)):
            self.vy *= 0
            self.vx *= 0
            self.hit = 1
        if self.hit == 1:
            self.r += 5
        if self.r >= 200:
            self.live = 0
        self.x += self.vx
        self.y -= self.vy
        
    def draw(self):
        #Draws a hole
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        #The function checks whether this hole collides with the object described in the obj object.

        #Args:
        #  obj: The object with which the collision is checked.
        #Returns:
        #  Returns True if the hole and the object collide. Otherwise returns False. And also turning hit into 1.
        
        if(((self.x - obj.x)*(self.x - obj.x) + (self.y - obj.y)*(self.y - obj.y)) <= (self.r + obj.r)*(self.r + obj.r) and obj.zaderzka == 0):
            self.hit = 1
            return True
        else:
            return False
        
class Ball:
    def __init__(self, screen: pygame.Surface, x: int, y: int):
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
        self.x = x + 90
        self.y = y + 90
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
        
        if(self.x > 715 - self.r):
            self.vx = -1*np.abs(self.vx)
        if(self.x < 85 + self.r):
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
    def __init__(self, screen: pygame.Surface, x: int):
        #Constructor of the Gun class
        
        #Args:
        #screen - pygame.display object
        #puska - pygame.surface object
        #fire_power - how strong will the cannon fire
        #fire_on - if it is '1', cannon is charging
        #an - angle
        #color - color, again :-)
        #up/down - movement up and down
        #po_chas/protiv_chas - rotating of the gun
        #type - is type of projectile (-1 - balls, 1 - hole)
        #stan - time during which gun is disable
        
        self.x = x
        self.y = 420
        self.r = 20
        self.screen = screen
        self.puska = pygame.Surface((360,360),pygame.SRCALPHA)
        self.fire_power = 10
        self.fire_on = 0
        self.an = np.pi/2
        self.up = 0
        self.down = 0
        self.po_chas = 0
        self.protiv_chas = 0
        self.type = -1
        self.color = GREY
        self.stan = 0

    def fire_start(self, event: pygame.event, i: int):
    
        #starts cannon's charging
        #occurs when the shoot-button is down.
        
        if (self.type == -1 and len(balls[i]) < 3 and self.an != np.pi/2 and self.stan == 0):
            self.fire_on = 1
            self.color = RED
        elif (self.type == 1 and hole[i].recharging == 0 and self.an != np.pi/2 and self.stan == 0):
            self.fire_on = 1
            self.color = RED
           
    def fire_end(self, event: pygame.event, i: int):
        #ball or hole shot.

        #occurs when the shoot-button is released.
        #the initial values of the ball/hole velocity components vx and vy depend on the angle and fire_power. 
        #returns the cannon to its initial state.
        
        global balls
        if (self.type == -1 and len(balls[i]) < 3 and self.an != np.pi/2 and self.stan == 0):
            new_ball = Ball(self.screen, self.x, self.y)
            self.an *= -1
            new_ball.vx = self.fire_power * math.cos(self.an)
            new_ball.vy = - self.fire_power * math.sin(self.an)
            self.an *= -1
            balls[i].append(new_ball)
            self.fire_on = 0
            self.fire_power = 10
            self.color = GREY
        elif (self.type == 1 and hole[i].recharging == 0 and self.an != np.pi/2 and self.stan == 0):
            new_hole = Hole(self.screen, self.x, self.y)
            self.an *= -1
            new_hole.vx = self.fire_power * math.cos(self.an)/2
            new_hole.vy = - self.fire_power * math.sin(self.an)/2
            self.an *= -1
            hole[i] = new_hole
            self.fire_on = 0
            self.fire_power = 10
            self.color = GREY
            hole[i].recharging = 300
    
    def targetting_po_start(self, event: pygame.event):
        #starting rotating
        
        self.po_chas = 1
    def targetting_protiv_start(self, event: pygame.event):
        #starting rotating
        
        self.protiv_chas = 1
    def targetting_po_stop(self, event: pygame.event):
        #stop rotating
        
        self.po_chas = 0
    def targetting_protiv_stop(self, event: pygame.event):
        #stop rotating
        
        self.protiv_chas = 0
    
    def targetting(self, i: int):
        #calculates the angle and bounds it for the corresponding cannon
        
        if i == 1 and self.stan == 0:
            if self.po_chas == 1 and self.an > -np.pi/2 + np.pi/18:
                self.an -= 10*np.pi/180
            if self.protiv_chas == 1 and self.an < np.pi/2 - np.pi/18:
                self.an += 10*np.pi/180
        if i == 2 and self.stan == 0:
            if self.po_chas == 1 and self.an > np.pi/2 + np.pi/9:
                self.an -= 10*np.pi/180
            if self.protiv_chas == 1 and self.an < 3*np.pi/2 - np.pi/9:
                self.an += 10*np.pi/180

    def draw(self, screen):
        #draws a cannon and rotating it
        
        self.puska = pygame.Surface((180,180),pygame.SRCALPHA)
        pygame.draw.rect(self.puska, (50,50,50), (80,65,20,50))
        if self.stan != 0:
            pygame.draw.rect(self.puska, (0,0,150), (80,65,20,50))
            self.fire_power = 10
            self.fire_on = 0
            self.up = 0
            self.down = 0
            self.stan -= 1
        pygame.draw.polygon(self.puska, self.color, [(90 + int(5*np.cos(self.an + 1.57)),
                                                      90 - int(5*np.sin(self.an + 1.57))),
                                                      
                                                     (90 + int(5*np.cos(self.an - 1.57)),
                                                      90 - int(5*np.sin(self.an - 1.57))),
                                                      
                                                     (90 + int(np.power((30+self.fire_power/2)*(30+self.fire_power/2)+5*5, 0.5)*np.cos(self.an - 5/(30+self.fire_power/2))),
                                                      90 - int(np.power((30+self.fire_power/2)*(30+self.fire_power/2)+5*5, 0.5)*np.sin(self.an - 5/(30+self.fire_power/2)))),
                                                      
                                                     (90 + int(np.power((30+self.fire_power/2)*(30+self.fire_power/2)+5*5, 0.5)*np.cos(self.an + 5/(30+self.fire_power/2))),
                                                      90 - int(np.power((30+self.fire_power/2)*(30+self.fire_power/2)+5*5, 0.5)*np.sin(self.an + 5/(30+self.fire_power/2))))])
        screen.blit(self.puska, (self.x, self.y))
        
    def up_start(self):
        if self.stan == 0:
            self.up = 1
    
    def up_stop(self):
        self.up = 0
        
    def down_start(self):
        if self.stan == 0:
            self.down = 1
        
    def down_stop(self):
        self.down = 0
        
    def move(self):
        if self.up == 1:
            if self.y > 100:
                self.y -= 5
        if self.down == 1:
            if self.y < 420:
                self.y += 5
        
    def power_up(self):
        #cannon's charging
        
        if self.fire_on:
            if self.fire_power < 70:
                self.fire_power += 1
            self.color = RED
        else:
            self.color = GREY
            
    def strike(self, obj, i):
        #checking the gun for damage
        
        if(((self.x + 90 - obj.x)*(self.x + 90 - obj.x) + (self.y + 90 - obj.y)*(self.y + 90 - obj.y)) <= (obj.r + self.r)*(obj.r + self.r)):
            self.stan = 90
            if(i == -1):
                obj.live = 0
            if(i == 1):
                obj.hit = 1
            return True
        else:
            return False


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
        
        self.x = rn.randint(200, 600)
        self.y = rn.randint(200, 550)
        self.r = rn.randint(15, 50)
        self.vx = rn.randint(-15,15)
        self.vy = rn.randint(-15,15)
        self.color = rn.choice(GAME_COLORS)
        self.zaderzka = 0

    def new_target(self):
        #Initialising of a new target
        
        self.x = rn.randint(200, 600)
        self.y = rn.randint(200, 550)
        self.r = rn.randint(15, 50)
        self.vx = rn.randint(-15,15)
        self.vy = rn.randint(-15,15)
        self.color = rn.choice(GAME_COLORS)
        self.zaderzka = 60

    def hit(self, k):
        #Collision with a ball
        
        global points
        points[k] += 1

    def draw(self, screen):
        #draws a target
        
        if(self.zaderzka == 0):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
    def move(self):             
        #makes target move
    
        if(self.zaderzka == 0):
            if(self.x > 715 - self.r):
                self.vx = rn.randint(-15,0)
                self.vy = rn.randint(-15,15)
            if(self.x < 85 + self.r):
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
    def collision(self, balls1, i):  
        # checks if balls1 collided and pushes them
        
        for j in range(i,5):
            if((i != j) and ((np.power(balls1[i].x - balls1[j].x,2) + np.power(balls1[i].y - balls1[j].y,2)) < np.power(balls1[i].r + balls1[j].r,2)) 
                              and (balls1[j].zaderzka == 0) 
                              and (balls1[i].zaderzka == 0)):
                sin = (balls1[i].y - balls1[j].y)/int(np.power(np.power(balls1[i].x - balls1[j].x,2) + np.power(balls1[i].y - balls1[j].y,2), 1/2))
                cos = (balls1[i].x - balls1[j].x)/int(np.power(np.power(balls1[i].x - balls1[j].x,2) + np.power(balls1[i].y - balls1[j].y,2), 1/2))
                vj = int(np.power(np.power(balls1[j].vx, 2) + np.power(balls1[j].vy, 2), 1/2))
                vi = int(np.power(np.power(balls1[i].vx, 2) + np.power(balls1[i].vy, 2), 1/2))
                balls1[i].vx = vj*cos
                balls1[i].vy = vj*sin
                balls1[j].vx = -1*vi*cos
                balls1[j].vy = -1*vi*sin
                
class Square:                                                                                          #Class of Square-target            
    def __init__(self):                                                                                #Creating parameters of Square
        self.x = rn.randint(100,500)
        self.y = rn.randint(150,500)
        self.vx = 10
        self.vy = 10
        self.r = 20
        self.color = GAME_COLORS[rn.randint(0, 5)]
        self.zaderzka = 60
    def draw(self, screen):                                                                                    #method that draws a square
        if(self.zaderzka == 0):
            pygame.draw.rect(screen, self.color, (self.x - self.r/2, self.y - self.r/2, self.r, self.r), 0)
    def move(self):                                                                                    #method that makes square move
        if(self.zaderzka == 0):
            if(self.x > 715 - self.r):
                self.vx = -1*np.abs(self.vx)
            if(self.x < 85 + self.r):
                self.vx = np.abs(self.vx)
            if(self.y > 600 - self.r):
                self.vy = -1*np.abs(self.vy)
            if(self.y < self.r + 90):
                self.vy = np.abs(self.vy)
            if(self.vx > 20):
                self.vx -= 1
            if(self.vx < -20):
                self.vx += 1
            self.x += self.vx
            self.y += self.vy
            self.vy += 2
        else:
            self.zaderzka -= 1
            
    def new_target(self):
        #Initialising of a new target
        
        self.x = rn.randint(100,500)
        self.y = rn.randint(150,500)
        self.vx = 10
        self.vy = 10
        self.r = 20
        self.color = GAME_COLORS[rn.randint(0, 5)]
        self.zaderzka = 60
            
    def hit(self, k):
        #Collision with a ball
        
        global points
        points[k] += 2
        
    def collision(self, Squaress, balls1, i):                                                        #method that checking if balls1 and Squares collided and pushes them
        for j in range(i,3):
            if((i != j) and ((np.power(Squaress[i].x - Squaress[j].x,2) + np.power(Squaress[i].y - Squaress[j].y,2)) < np.power(Squaress[i].r + Squaress[j].r,2)) 
                              and (Squaress[j].zaderzka == 0) 
                              and (Squaress[i].zaderzka == 0)):
                sin = (Squaress[i].y - Squaress[j].y)/(int(np.power(np.power(Squaress[i].x - Squaress[j].x,2) + np.power(Squaress[i].y - Squaress[j].y,2), 1/2)))
                cos = (Squaress[i].x - Squaress[j].x)/(int(np.power(np.power(Squaress[i].x - Squaress[j].x,2) + np.power(Squaress[i].y - Squaress[j].y,2), 1/2)))
                vj = int(np.power(np.power(Squaress[j].vx, 2) + np.power(Squaress[j].vy, 2), 1/2))
                vi = int(np.power(np.power(Squaress[i].vx, 2) + np.power(Squaress[i].vy, 2), 1/2))
                Squaress[i].vx = vi*cos
                Squaress[i].vy = vi*sin
                Squaress[j].vx = -1*vj*cos
                Squaress[j].vy = -1*vj*sin
        for j in range(5):
            if(((np.power(Squaress[i].x - balls1[j].x,2) + np.power(Squaress[i].y - balls1[j].y,2)) < np.power(Squaress[i].r + balls1[j].r,2)) 
                 and (Squaress[i].zaderzka == 0) 
                 and (balls1[j].zaderzka == 0)):
                sin = (Squaress[i].y - balls1[j].y)/(int(np.power(np.power(Squaress[i].x - balls1[j].x,2) + np.power(Squaress[i].y - balls1[j].y,2), 1/2)))
                cos = (Squaress[i].x - balls1[j].x)/(int(np.power(np.power(Squaress[i].x - balls1[j].x,2) + np.power(Squaress[i].y - balls1[j].y,2), 1/2)))
                vi = int(np.power(np.power(Squaress[i].vx, 2) + np.power(Squaress[i].vy, 2), 1/2))
                Squaress[i].vx = vi*cos
                Squaress[i].vy = vi*sin
                
class Rocket:
    def __init__(self, screen: pygame.Surface, x: int, y: int):
        # Constructor of a rocket class:
        
        #Args:
        #x,y - coordinates
        #v - velocity
        #r - radius of hitbox
        
        self.x = x
        self.y = y
        self.v = int((rn.randint(-1,0) + 0.5)*20)
        self.r = np.abs(self.v)
        self.screen = screen
    def move(self):
        #rocket movement
        
        self.x += self.v
    def draw(self):
        #draws a rocket
        
        pygame.draw.polygon(self.screen, (50,50,255), [(self.x, self.y - self.v), (self.x, self.y + self.v), (self.x + 2*self.v, self.y)])

def tablichka(score: str, a: int, b: int, size: int, x: int, y: int):
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
    screen.blit(s, (x,y))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

Rockets = list()

global hole
hole = [Hole(screen,0,0),Hole(screen,0,0)]
hole[0].live = 0
hole[1].live = 0

global balls
balls1 = list()
balls2 = list()
balls = [balls1, balls2]
Squaress = list()

for i in range (3):
    Squaress.append(Square())
targets = [0]*5
for i in range(5):
    targets[i] = Target()
    
global points
points = [0, 0]
restarting = 0
clock = pygame.time.Clock()
gun1 = Gun(screen, 0)
gun2 = Gun(screen, 620)
target = Target()
time = 1200
finished = False

while not finished:
    #The game itself:
    #Designed for two players, each player plays for a cannon that rides on rails on the wall,
    #the goal of the game is to score more points than the opponent in 1 minute. to earn points,
    #you need to hit targets: balls - 1 point, squares - 2 points; two types of projectiles are used for this:
    #balls flying in the field of gravity, black holes expanding and destroying everything they reach. 
	#Black holes are much more powerful than balls, so they can only be fired once every 10 seconds.
    #Targets can fire missiles, they fly at a constant speed, ignoring everything around them except guns.
    #Enemy cannon shells and missiles can stun the cannon for 3 seconds when hit. At the end of the game, 
    #a window pops up with a message about the victory of one of the players or a draw. 
    #When the restart button is pressed, the game is updated
    
    #Gun control:
    #w,s/up,down - move up and down (1/2 player)
    #a,D/left,right - turn clockwise and counterclockwise (1/2) player
    #Space/right shift - projectile shot, if the player shoots more powerfully (1/2 player)
    #1/2 - switching types of projectiles (1/2 player)
    
    screen.fill(WHITE)
    for i in range(5):
        targets[i].draw(screen)
    for i in range(3):
        Squaress[i].draw(screen)
    for b1 in balls1:
        b1.draw()
    for b2 in balls2:
        b2.draw()
    for r in Rockets:
        r.move()
        r.draw()
    l = 0    
    for i in range(len(Rockets)):
        if (Rockets[i - l].x > 695 or Rockets[i - l].x < 105):
            del Rockets[i - l]
            l += 1
    pygame.draw.rect(screen, (100,100,0), (0,0,95,600))
    pygame.draw.rect(screen, (100,100,0), (705,0,95,600))
    pygame.draw.rect(screen, (0,0,0), (85,165,10,370))
    pygame.draw.rect(screen, (0,0,0), (705,165,10,370))
    for i in range(len(hole)):
        if hole[i].live == 1:
            hole[i].draw()
        if hole[i].recharging != 0:
            tablichka('recharging',50,30,10,20 + i*710, 100)
            hole[i].recharging -= 1
    clock.tick(FPS)
    time -= 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] <= 180 and event.pos[1] <= 90):           #Checks if you clicked botton 'restart'
                for i in range(5):
                    targets[i].new_target()
                for i in range(3):
                    Squaress[i].new_target()
                for i in range(2):
                    del balls[i][0:len(balls[i])]
                    hole[i].live = 0
                    points[i] = 0
                    hole[i].recharging = 0
                del Rockets[0:len(Rockets)]
                gun1.y = 420
                gun1.fire_power = 10
                gun1.color = GREY
                gun1.an = np.pi/2
                gun1.fire_on = 0
                gun1.stan = 0
                gun2.y = 420
                gun2.fire_power = 10
                gun2.color = GREY
                gun2.an = np.pi/2
                gun2.fire_on = 0
                gun2.stan = 0
                
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                gun1.type *= -1
            if event.key == pygame.K_2:
                gun2.type *= -1
        
            if event.key == pygame.K_SPACE:
                gun1.fire_start(event, 0)
            if event.key == pygame.K_RSHIFT:
                gun2.fire_start(event, 1)
                
            if event.key == pygame.K_d:
                gun1.targetting_po_start(event)
            if event.key == pygame.K_RIGHT:
                gun2.targetting_po_start(event)
            if event.key == pygame.K_a:
                gun1.targetting_protiv_start(event)
            if event.key == pygame.K_LEFT:
                gun2.targetting_protiv_start(event)
            
            if event.key == pygame.K_w:
                gun1.up_start()
            if event.key == pygame.K_s:
                gun1.down_start()
            if event.key == pygame.K_UP:
                gun2.up_start()
            if event.key == pygame.K_DOWN:
                gun2.down_start()
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                gun1.fire_end(event, 0)
            if event.key == pygame.K_RSHIFT:
                gun2.fire_end(event, 1)
        
            if event.key == pygame.K_d:
                gun1.targetting_po_stop(event)
            if event.key == pygame.K_RIGHT:
                gun2.targetting_po_stop(event)
            if event.key == pygame.K_a:
                gun1.targetting_protiv_stop(event)
            if event.key == pygame.K_LEFT:
                gun2.targetting_protiv_stop(event)
        
            if event.key == pygame.K_w:
                gun1.up_stop()
            if event.key == pygame.K_s:
                gun1.down_stop()
            if event.key == pygame.K_UP:
                gun2.up_stop()
            if event.key == pygame.K_DOWN:
                gun2.down_stop()
                
    gun1.targetting(1)
    gun2.targetting(2)
    gun1.move()
    gun2.move()
    gun1.draw(screen)
    gun2.draw(screen)
    
    for i in range(5):
        if targets[i].zaderzka == 0:
            targets[i].move()
            random = rn.randint(0,150)
            if random == 1:
                Rockets.append(Rocket(screen, targets[i].x, targets[i].y))
            targets[i].collision(targets, i)
        else:
            targets[i].zaderzka -= 1
            
    for i in range(3):
        Squaress[i].move()
        Squaress[i].collision(Squaress, targets, i)
    for k in range(2):
        for i in range(len(balls[k])):
            balls[k][i].move()
            for j in range (5):
                if (balls[k][i].hittest(targets[j], i)):
                    targets[j].hit(k)
                    targets[j].new_target()
            for j in range (3):
                if (balls[k][i].hittest(Squaress[j], i)):
                    Squaress[j].hit(k)
                    Squaress[j].new_target()
        if hole[k].live == 1:
            hole[k].move()
            for j in range (5):
                if (hole[k].hittest(targets[j])):
                    targets[j].hit(k)
                    targets[j].new_target()
            for j in range (3):
                if (hole[k].hittest(Squaress[j])):
                    Squaress[j].hit(k)
                    Squaress[j].new_target()
                    
    if hole[1].live == 1:
        gun1.strike(hole[1],1)
    for i in range(len(balls[1])):
        gun1.strike(balls[1][i],-1)
    if hole[0].live == 1:
        gun2.strike(hole[0],1)
    for i in range(len(balls[0])):
        gun2.strike(balls[0][i],-1)
    for i in range(len(Rockets)):
        gun1.strike(Rockets[i],2)
        gun2.strike(Rockets[i],2)
        
    for k in range(2):
        l = 0    
        for i in range(len(balls[k])):
            if (balls[k][i - l].time == 0 or balls[k][i - l].live == 0):
                del balls[k][i - l]
                l += 1
    gun1.power_up()
    gun2.power_up()
    tablichka('P1 score: ' + str(points[0]) + '   P2 score: ' + str(points[1]), 620, 90, 50, 180, 0)
    tablichka('RESTART', 180, 90, 40, 0, 0)
    pygame.display.update()
    
    #final screen with restart button
    while time == 0:
        clock.tick(FPS)
        pygame.draw.rect(screen, BLACK, (0,90,800,510),0)
        if points[0] > points[1]:
            tablichka('Player 1 won!', 800, 510, 100, 0, 90)
        elif points[0] < points[1]:
            tablichka('Player 2 won!', 800, 510, 100, 0, 90)
        else:
            tablichka('There is no winner!', 800, 510, 100, 0, 90)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                time = 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] <= 180 and event.pos[1] <= 90):           #Checks if you clicked botton 'restart'
                    for i in range(5):
                        targets[i].new_target()
                    for i in range(3):
                        Squaress[i].new_target()
                    for i in range(2):
                        del balls[i][0:len(balls[i])]
                        hole[i].live = 0
                        points[i] = 0
                        hole[i].recharging = 0
                    del Rockets[0:len(Rockets)]
                    gun1.y = 420
                    gun1.fire_power = 10
                    gun1.color = GREY
                    gun1.an = np.pi/2
                    gun1.fire_on = 0
                    gun1.stan = 0
                    gun1.up = 0
                    gun1.down = 0
                    gun2.y = 420
                    gun2.fire_power = 10
                    gun2.color = GREY
                    gun2.an = np.pi/2
                    gun2.fire_on = 0
                    gun2.stan = 0
                    gun2.up = 0
                    gun2.down = 0
                    time = 1200

pygame.quit()
