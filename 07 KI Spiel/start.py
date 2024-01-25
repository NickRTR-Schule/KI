### Author: Nick Reutlinger
### Date: 22.01.2024
### Version: 1.0
### Flappy Bird mit KI

import pygame as pg
import sys
import random

''' Funktionen  '''

def printText(text, pos, size, color):
    font = pg.font.SysFont(None, size)
    screen.blit(font.render(text, True, color), pos)

### Screen ###
pg.init()
width = 1000
height = 700
screen = pg.display.set_mode((width, height))
FPS = 60
FPSCLOCK = pg.time.Clock()
### Bird ###
birdPosX = width/5
birdPosY = height/4
birdRadius = 20
time = 0
### Pipe ###
pipeWidth = 50
pipeHeight = 500
pipeGap = 200
points = 0

# Pipe 1
pipe1UppPosX = width/2
pipe1UppPosY = random.randint(-pipeHeight, 0)
pipe1LowPosX = pipe1UppPosX
pipe1LowPosY = pipe1UppPosY + pipeHeight + pipeGap

# Pipe 2
pipe2UppPosX = width
pipe2UppPosY = random.randint(-pipeHeight, 0)
pipe2LowPosX = pipe2UppPosX
pipe2LowPosY = pipe2UppPosY + pipeHeight + pipeGap

active = 0
gameOver = 0

while(1):
    ''' EVENTS '''
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            pg.quit()
            sys.exit()
        if (event.type == pg.KEYDOWN): 
            if (event.key == pg.K_SPACE):
                birdPosY -= 150
                time = 0

    ''' HINTERGRUND '''
    screen.fill([255,255,255])

    if (gameOver == 0):
        ''' PIPE 1'''
        pipe1UppPosX -= 10
        pipe1LowPosX = pipe1UppPosX
        if (pipe1UppPosX < -pipeWidth):
            pipe1UppPosX = width
            pipe1UppPosY = random.randint(-pipeHeight, 0)
            pipe1LowPosY = pipe1UppPosY + pipeHeight + pipeGap

        ''' PIPE 2'''
        pipe2UppPosX -= 10
        pipe2LowPosX = pipe2UppPosX
        if (pipe2UppPosX < -pipeWidth):
            pipe2UppPosX = width
            pipe2UppPosY = random.randint(-pipeHeight, 0)
            pipe2LowPosY = pipe2UppPosY + pipeHeight + pipeGap

        # Pipe 1
        pg.draw.rect(screen, [0,255,0], [pipe1UppPosX, pipe1UppPosY, pipeWidth, pipeHeight])
        pg.draw.rect(screen, [0,255,0], [pipe1LowPosX, pipe1LowPosY, pipeWidth, pipeHeight])

        # Pipe 2
        pg.draw.rect(screen, [0,255,0], [pipe2UppPosX, pipe2UppPosY, pipeWidth, pipeHeight])
        pg.draw.rect(screen, [0,255,0], [pipe2LowPosX, pipe2LowPosY, pipeWidth, pipeHeight])

        ''' BIRD '''
        pg.draw.circle(screen, [255,255,0], [birdPosX, birdPosY], birdRadius)
        time += 0.1
        birdPosY += time**2

    ''' KOLLISION '''
    # Pipe 1
    # Add a point if the bird passes the pipe in the gap without colliding
    if (birdPosX >= pipe1UppPosX and birdPosX <= pipe1UppPosX + pipeWidth):
        if active == 0:
            if(birdPosY > pipe1UppPosY + pipeHeight and birdPosY < pipe1LowPosY):
                points += 1
                active = 1
            else:
                gameOver = 1

    # Pipe 2
    if (birdPosX >= pipe2UppPosX and birdPosX <= pipe2UppPosX + pipeWidth):
        if active == 0:
            if (birdPosY > pipe2UppPosY + pipeHeight and birdPosY < pipe2LowPosY):
                points += 1
                active = 1
            else:
                gameOver = 1

    if (pipe1UppPosX < 0 or pipe2UppPosX < 0):
        active = 0

    ''' Text '''
    printText('Flappy Bird', (400, 20), 40, [0,0,0])
    printText('Punkte: ' + str(points), (20, 50), 25, [255, 255, 0])
    if (gameOver == 1):
        printText('Game Over', (400, 300), 40, [0,0,0])

    ''' ZEITEN '''
    FPSCLOCK.tick(FPS)
    pg.display.update()