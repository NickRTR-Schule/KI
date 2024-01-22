### Author: Nick Reutlinger
### Date: 22.01.2024
### Version: 1.0
### Flappy Bird mit KI

import pygame as pg
import sys
import random

### Screen ###
pg.init()
width = 1000
heigth = 700
screen = pg.display.set_mode((width, heigth))
FPS = 60
FPSCLOCK = pg.time.Clock()
### Bird ###
birdPosX = width/5
birdPosY = heigth/4
birdRadius = 20
time = 0

while(1):
    ''' EVENTS '''
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            pg.quit()
            sys.exit()
        if (event.type == pg.KEYDOWN): 
            if (event.key == pg.K_SPACE):
                birdPosY -= 100
                time = 0

    ''' HINTERGRUND '''
    screen.fill([111,111,255])

    ''' BIRD '''
    pg.draw.circle(screen, [255,255,0], [birdPosX, birdPosY], birdRadius)
    time += 0.25
    birdPosY += time**2
    
    ''' ZEITEN '''
    FPSCLOCK.tick(FPS)
    pg.display.update()