import pygame as pg

def oblako(x,y):
	pg.draw.circle(screen, (255,255,255), (x,y), 15, 0)
	pg.draw.circle(screen, (0,0,0), (x,y), 15, 1)
def clouds(x,y):
	for i in range(2):
		oblako(x+20*i,y)
		oblako(x-15+20*i,y+15)
	oblako(x-15+20*2,y+15)
	oblako(x+20*2,y)
	oblako(x-15+20*3,y+15)
def sun(x,y):
	pg.draw.circle(screen, (255,255,0), (x, y), 35, 0)
def fon():
	pg.draw.rect(screen, (220,220,255), (0,0,600,180), 0)
	pg.draw.rect(screen, (0,0,255), (0,180,600,100), 0)
	pg.draw.rect(screen, (255,255,0), (0,280,600,120), 0)
def umbrella(x,y):
	zont = pg.Surface((125,125),pg.SRCALPHA)
	pg.draw.polygon(zont, (200,150,100,200), [(60,0), (65,0), (125,30), (0,30)], 0)
	pg.draw.rect(zont, (200,150,100,255), (60, 0, 5, 125))
	for i in range(4):
		pg.draw.line(zont, (0,0,0), (60,0), (0 + 15*i,30), 1)
	for i in range(4):
		pg.draw.line(zont, (0,0,0), (65,0), (65 + 15*(i+1),30), 1)
	screen.blit(zont, (x,y))
def best_ship(x,y):
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
	screen.blit(ship, (x,y))
	
	
pg.init()

FPS = 30
screen = pg.display.set_mode((600, 400), pg.SRCALPHA)

fon()
clouds(150,50)
sun(530,50)
umbrella(30,240)
best_ship(300,80)

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()