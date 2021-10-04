import pygame as pg
import numpy as np

def oblako(x,y, square):
	pg.draw.circle(square, (255,255,255), (x,y), 15, 0)
	pg.draw.circle(square, (0,0,0), (x,y), 15, 1)
def clouds(x,y,a,b):
	kusok_neba = pg.Surface((200,100),pg.SRCALPHA)
	for i in range(2):
		oblako(10+20*(i+1),15,kusok_neba)
		oblako(-5+20*(i+1),30,kusok_neba)
	oblako(-5+20*3,30,kusok_neba)
	oblako(10+20*3,15,kusok_neba)
	oblako(-5+20*4,30,kusok_neba)
	kusok_neba = pg.transform.smoothscale(kusok_neba, (int(200*a), int(100*b)))
	screen.blit(kusok_neba, (x,y))
def sun(x,y):
	solnce = pg.Surface((120,120),pg.SRCALPHA)
	pg.draw.circle(solnce, (255,255,0), (60, 60), 50, 0)
	for i in range(60):
		pg.draw.polygon(solnce, (255,255,0), [(int(60 + 60*np.cos(np.pi/24*i)),int(60 - 60*np.sin(np.pi/24*i))),
											  (int(60 + 50*np.cos(np.pi/24*i+np.pi/48)),int(60 - 50*np.sin(np.pi/24*i+np.pi/48))),
											  (int(60 + 50*np.cos(np.pi/24*i-np.pi/48)),int(60 - 50*np.sin(np.pi/24*i-np.pi/48)))
											 ])
	screen.blit(solnce,(x,y))
def fon():
	pg.draw.rect(screen, (220,220,255), (0,0,600,180), 0)
	pg.draw.rect(screen, (0,0,255), (0,180,600,100), 0)
	pg.draw.rect(screen, (255,255,0), (0,280,600,120), 0)
	for i in range(5):
		pg.draw.circle(screen, (255,255,0), (30+120*i,320), 50)
		pg.draw.circle(screen, (0,0,255), (90+120*i,240), 50)
def umbrella(x,y,a,b):
	zont = pg.Surface((125,125),pg.SRCALPHA)
	pg.draw.polygon(zont, (200,150,100,200), [(60,0), (65,0), (125,30), (0,30)], 0)
	pg.draw.rect(zont, (200,150,100,255), (60, 0, 5, 125))
	for i in range(4):
		pg.draw.line(zont, (0,0,0), (60,0), (0 + 15*i,30), 1)
	for i in range(4):
		pg.draw.line(zont, (0,0,0), (65,0), (65 + 15*(i+1),30), 1)
	zont = pg.transform.smoothscale(zont, (int(125*a), int(125*b)))
	screen.blit(zont, (x,y))
def best_ship(x,y,a,b):
	ship = pg.Surface((300,200),pg.SRCALPHA)
	pg.draw.circle(ship, (190,25,0), (30,130), 30, 0)
	pg.draw.rect(ship, (140,25,0,0), (0,100, 60, 30))
	pg.draw.rect(ship, (190,25,0), (30,130, 150, 30))
	pg.draw.polygon(ship, (190,25,0), [(180,130), (180, 159), (250,130)], 0)
	pg.draw.line(ship, (0,0,0), (30,130), (30, 160))
	pg.draw.line(ship, (0,0,0), (180,130), (180, 160))
	pg.draw.circle(ship, (255,255,255), (195,142), 9, 0)
	pg.draw.circle(ship, (0,0,0), (195,142), 9, 3)
	pg.draw.rect(ship, (0,0,0), (90, 30, 5, 100), 0)
	pg.draw.polygon(ship, (190,216,153), [(95,30), (110,80), (95,130), (155,80)])
	pg.draw.polygon(ship, (0,0,0), [(95,30), (110,80), (95,130), (155,80)], 1)
	pg.draw.line(ship, (0,0,0), (110,80), (155, 80), 1)
	ship = pg.transform.smoothscale(ship, (int(300*a), int(200*b)))
	screen.blit(ship, (x,y))
	
	
pg.init()

FPS = 30
screen = pg.display.set_mode((600, 400), pg.SRCALPHA)

fon()
clouds(100,40,1,1)
clouds(220,20,1.7,1.7)
clouds(40,100,1.7,1)
sun(470,30)
umbrella(30,250,1,1)
umbrella(180,270,0.4,0.7)
best_ship(300,80,1,1)
best_ship(150,130,0.5,0.5)

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()