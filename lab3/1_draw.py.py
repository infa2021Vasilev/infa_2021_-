import pygame as pg

pg.init()

FPS = 30
screen = pg.display.set_mode((400, 400))

screen.fill((180,180,180))
pg.draw.circle(screen, (255, 255, 0), (200, 200), 100)
pg.draw.circle(screen, (255, 0, 0), (150, 175), 25, 0)
pg.draw.circle(screen, (0, 0, 0), (150, 175), 25, 2)
pg.draw.circle(screen, (0, 0, 0), (150, 175), 5, 0)
pg.draw.circle(screen, (255, 0, 0), (250, 175), 20, 0)
pg.draw.circle(screen, (0, 0, 0), (250, 175), 20, 2)
pg.draw.circle(screen, (0, 0, 0), (250, 175), 5, 0)
pg.draw.rect(screen, (0, 0, 0), (150, 250, 100, 20))
pg.draw.line(screen, (0,0,0), (175,175), (125,125), 20)
pg.draw.line(screen, (0,0,0), (225,175), (275,125), 20)
pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()