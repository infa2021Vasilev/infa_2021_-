import pygame as pg
import numpy as np
import random as rn

player = input()                                                                    #Reading Player's name

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

class Ball:                                                                            #Class of ball-target
    def __init__(self):                                                                #Creating parameters of ball
        self.x = rn.randint(100,700)
        self.y = rn.randint(150,700)
        self.vx = rn.randint(-15,15)
        self.vy = rn.randint(-15,15)
        self.r = rn.randint(30,50)
        self.color = COLORS[rn.randint(0, 5)]
        self.zaderzka = 0
    def draw(self):                                                                    #method that draws a ball
        if(self.zaderzka == 0):
            pg.draw.circle(screen, self.color, (self.x, self.y), self.r, 0)
    def move(self):                                                                    #method that makes ball move
        if(self.zaderzka == 0):
            if(self.x > 1200 - self.r):
                self.vx = rn.randint(-15,0)
                self.vy = rn.randint(-15,15)
            if(self.x < self.r):
                self.vx = rn.randint(0,15)
                self.vy = rn.randint(-15,15)
            if(self.y > 700 - self.r):
                self.vy = rn.randint(-15,0)
                self.vx = rn.randint(-15,15)
            if(self.y < self.r + 90):
                self.vy = rn.randint(0,15)
                self.vx = rn.randint(-15,15)
            self.x += self.vx
            self.y += self.vy
        else:
            self.zaderzka -= 1
    def collision(self, Balls, i):                                                    #method that checking if Balls collided and pushes them
        for j in range(i,10):
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
            
class Square:                                                                                          #Class of Square-target            
    def __init__(self):                                                                                #Creating parameters of Square
        self.x = rn.randint(100,700)
        self.y = rn.randint(150,700)
        self.vx = 10
        self.vy = 10
        self.r = 20
        self.color = COLORS[rn.randint(0, 5)]
        self.zaderzka = 60
    def draw(self):                                                                                    #method that draws a square
        if(self.zaderzka == 0):
            pg.draw.rect(screen, self.color, (self.x - self.r, self.y - self.r, self.r, self.r), 0)
    def move(self):                                                                                    #method that makes square move
        if(self.zaderzka == 0):
            if(self.x > 1200 - self.r):
                self.vx = -1*np.abs(self.vx)
            if(self.x < self.r):
                self.vx = np.abs(self.vx)
            if(self.y > 700 - self.r):
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
    def collision(self, Squaress, Balls, i):                                                        #method that checking if Balls and Squares collided and pushes them
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
        for j in range(10):
            if(((np.power(Squaress[i].x - Balls[j].x,2) + np.power(Squaress[i].y - Balls[j].y,2)) < np.power(Squaress[i].r + Balls[j].r,2)) 
                 and (Squaress[i].zaderzka == 0) 
                 and (Balls[j].zaderzka == 0)):
                sin = (Squaress[i].y - Balls[j].y)/(int(np.power(np.power(Squaress[i].x - Balls[j].x,2) + np.power(Squaress[i].y - Balls[j].y,2), 1/2)))
                cos = (Squaress[i].x - Balls[j].x)/(int(np.power(np.power(Squaress[i].x - Balls[j].x,2) + np.power(Squaress[i].y - Balls[j].y,2), 1/2)))
                vi = int(np.power(np.power(Squaress[i].vx, 2) + np.power(Squaress[i].vy, 2), 1/2))
                Squaress[i].vx = vi*cos
                Squaress[i].vy = vi*sin
            
            
def click(event,Balls,Squaress):
    #Main function
    #checks if you clicked on any balls and squares, delets the balls and squares you clicked, sets the delay before the next balls and squares appear, counts points
    global points
    for i in range(10):
        if((np.power((event.pos[0] - Balls[i].x), 2) + np.power((event.pos[1] - Balls[i].y), 2)) <= (np.power(Balls[i].r, 2))):
            points = points + 1                                                         #counting points
            
            pg.draw.circle(screen, (0,0,0), (Balls[i].x, Balls[i].y), Balls[i].r, 0)    #deleting a ball
            
            Balls[i].x = rn.randint(100,700)                                            #creating parameters of a new ball
            Balls[i].y = rn.randint(150,500)
            Balls[i].r = rn.randint(30,50)
            Balls[i].vx = rn.randint(-15,15)
            Balls[i].vy = rn.randint(-15,15)
            Balls[i].color = COLORS[rn.randint(0, 5)]
            
            Balls[i].zaderzka = 60                                                      #delaying of a new ball spawning
    for i in range(3):
        if((np.power((event.pos[0] - Squaress[i].x), 2) + np.power((event.pos[1] - Squaress[i].y), 2)) <= (np.power(Squaress[i].r, 2))):
            points = points + 5                                                                                                                 #counting points
            
            pg.draw.circle(screen, (0,0,0), (Squaress[i].x - Squaress[i].r, Squaress[i].y - Squaress[i].r), Squaress[i].r + 10, 0)              #deleting a Squaress
            
            Squaress[i].x = rn.randint(100,700)                                                                                                 #creating parameters of a new Squaress
            Squaress[i].y = rn.randint(150,500)
            Squaress[i].r = 20
            Squaress[i].vx = 10
            Squaress[i].vy = 10
            Squaress[i].color = COLORS[rn.randint(0, 5)]
            
            Squaress[i].zaderzka = 180                                                                                                          #delaying of a new Squaress spawning


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

global points                                                    #score
points = 0                
time = 0
Balls = list()
Squaress = list()
for i in range (10):
    Balls.append(Ball())
for i in range (3):
    Squaress.append(Square())


while not finished:
    clock.tick(FPS)
    
    for i in range(10):                                            #implementation of the game
        Balls[i].draw()
    for i in range (3):
        Squaress[i].draw()
    for event in pg.event.get():
        if ((event.type == pg.QUIT) or (time >= 900)):
            finished = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            click(event, Balls, Squaress)
    pg.display.update()
    screen.fill(BLACK)
    for i in range(10):
        Balls[i].collision(Balls, i)
        Balls[i].move()
    for i in range(3): 
        Squaress[i].collision(Squaress, Balls, i)
        Squaress[i].move()
        
    tablichka('Your points are: ' + str(points))                  #showing score
    time += 1

s = pg.Surface((1200, 700), pg.SRCALPHA)                                                #Game over screen
    
myfont1 = pg.font.SysFont('arial', 150)
myfont2 = pg.font.SysFont('arial', 60)
textsurface1 = myfont1.render('GAME OVER!', False, (0, 0, 0))
textsurface2 = myfont2.render('Your points are: ' + str(points), False, (0, 0, 0))
pg.draw.rect(s,GREEN,(0,0,1200,700),0)
u1 = myfont1.size('GAME OVER!')
u2 = myfont2.size('Your points are: ' + str(points))
s.blit(textsurface1,(int((1200 - u1[0])/2),0))
s.blit(textsurface2,(int((1200 - u2[0])/2),350))
screen.blit(s, (0,0))
pg.display.update()

with open('Leaderboard.txt') as file:                                                    #Recording the result in the leaderboard
    inp = open('Leaderboard.txt', 'r')
    board = inp.read()
    out = open('Leaderboard.txt', 'w')
    board = board + '\n' + str(points) + ' : ' + player
    board = board.split('\n')
    for i in range(len(board)):
        board[i] = board[i].split(' : ')
        board[i][0] = int(board[i][0])
    board = sorted(board, reverse = True)
    for i in range(len(board)):
        board[i][0] = str(board[i][0])
        board[i] = ' : '.join(board[i])
    board = '\n'.join(board)
    out.write(board)
    
finished = False
while not finished:                                                                        #waiting for closing the game
    clock.tick(FPS)
    
    for event in pg.event.get():
        if ((event.type == pg.QUIT)):
            finished = True
print("Your points are ",points,'\n')
print(board)
pg.quit()