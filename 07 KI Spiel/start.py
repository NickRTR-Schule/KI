### Author: Nick Reutlinger
### Date: 22.01.2024
### Version: 1.0
### Flappy Bird mit KI

import pygame as pg
import sys
import random

''' Variablen '''
screenWidth = 1000
screenHeight = 700
FPS = 60
FPSCLOCK = pg.time.Clock()

''' Bird '''
birdPosX = screenWidth/5
birdPosY = screenHeight/4
birdWidth = 50
birdHeight = 35

''' Pipe '''
pipeWidth = 50
pipeHeight = 500
pipeGap = 200

# Pipe 1
pipe1UppPosX = screenWidth/2
pipe1UppPosY = random.randint(-pipeHeight, 0)
pipe1LowPosX = pipe1UppPosX
pipe1LowPosY = pipe1UppPosY + pipeHeight + pipeGap

# Pipe 2
pipe2UppPosX = screenWidth
pipe2UppPosY = random.randint(-pipeHeight, 0)
pipe2LowPosX = pipe2UppPosX
pipe2LowPosY = pipe2UppPosY + pipeHeight + pipeGap

# Text
white = [255, 255, 255]
fontSizeSmall = 20

''' Game '''
time = 0
points = 0
active = 0
gameOver = 0
generation = 1
rekord = 0
alive = 1

pg.init()
screen = pg.display.set_mode((screenWidth, screenHeight))

''' Funktionen  '''
def printText(text, pos, size, color):
    font = pg.font.SysFont(None, size)
    screen.blit(font.render(text, True, color), pos)

''' Images '''
baseHeight = 50
fb = pg.image.load('extra/fb.png')
fb = pg.transform.scale(fb, (birdWidth, birdHeight))

base = pg.image.load('extra/base.png')
base = pg.transform.scale(base, (screenWidth, baseHeight))

pipeUpp = pg.image.load('extra/pipeUpp.png')
pipeUpp = pg.transform.scale(pipeUpp, (pipeWidth, pipeHeight))

pipeLow = pg.image.load('extra/pipeLow.png')
pipeLow = pg.transform.scale(pipeLow, (pipeWidth, pipeHeight))

bg = pg.image.load('extra/background.png')
bg = pg.transform.scale(bg, (screenWidth, screenHeight))

while(1):
    ''' EVENTS '''
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            pg.quit()
            sys.exit()
        if (event.type == pg.KEYDOWN): 
            if (event.key == pg.K_SPACE and gameOver == 0):
                birdPosY -= 150
                if (birdPosY < 0):
                    birdPosY = 0
                    gameOver = 1 
                time = 0
            elif (event.key == pg.K_SPACE and gameOver == 1):
                birdPosY = screenHeight/4
                pipe1UppPosX = screenWidth/2
                pipe2UppPosX = screenWidth
                rekord = max(rekord, points)
                points = 0
                time = 0
                generation += 1
                gameOver = 0

    ''' HINTERGRUND '''
    screen.blit(bg, (0,0))

    if (gameOver == 0):
        ''' PIPE 1'''
        pipe1UppPosX -= 5
        pipe1LowPosX = pipe1UppPosX
        if (pipe1UppPosX < -pipeWidth):
            pipe1UppPosX = screenWidth
            pipe1UppPosY = random.randint(-pipeHeight, 0)
            pipe1LowPosY = pipe1UppPosY + pipeHeight + pipeGap

        ''' PIPE 2'''
        pipe2UppPosX -= 5
        pipe2LowPosX = pipe2UppPosX
        if (pipe2UppPosX < -pipeWidth):
            pipe2UppPosX = screenWidth
            pipe2UppPosY = random.randint(-pipeHeight, 0)
            pipe2LowPosY = pipe2UppPosY + pipeHeight + pipeGap

        time += 0.1
        birdPosY += time**2

    # Pipe 1
    screen.blit(pipeUpp, (pipe1UppPosX, pipe1UppPosY))
    screen.blit(pipeLow, (pipe1LowPosX, pipe1LowPosY))

    # Pipe 2
    screen.blit(pipeUpp, (pipe2UppPosX, pipe2UppPosY))
    screen.blit(pipeLow, (pipe2LowPosX, pipe2LowPosY))

    ''' BIRD '''
    screen.blit(fb, (birdPosX, birdPosY))

    ''' BASE '''
    screen.blit(base, (0, screenHeight - baseHeight))

    ''' COLLISION '''
    # Pipe 1
    # Add a point if the bird passes the pipe in the gap without colliding
    if (birdPosX + birdWidth >= pipe1UppPosX and birdPosX <= pipe1UppPosX + pipeWidth):
        if active == 0:
            if(birdPosY > pipe1UppPosY + pipeHeight and birdPosY < pipe1LowPosY):
                points += 1
                active = 1
            else:
                gameOver = 1

    # Pipe 2
    if (birdPosX + birdWidth >= pipe2UppPosX and birdPosX <= pipe2UppPosX + pipeWidth):
        if active == 0:
            if (birdPosY > pipe2UppPosY + pipeHeight and birdPosY < pipe2LowPosY):
                points += 1
                active = 1
            else:
                gameOver = 1

    if (pipe1UppPosX < 0 or pipe2UppPosX < 0):
        active = 0

    ''' Collision Wall '''
    if (birdPosY > screenHeight - baseHeight - birdHeight):
        gameOver = 1

    ''' Text '''
    printText('Flappy Bird', (400, 20), 40, [0,0,0])
    printText('Generation: ' + str(generation), (20, 10), fontSizeSmall, white)
    printText('Rekord: ' + str(rekord), (20, 30), fontSizeSmall, white)
    printText('Punkte: ' + str(points), (20, 50), fontSizeSmall, white)
    printText('Anzahl: ' + str(alive), (20, 70), fontSizeSmall, white)
    if (gameOver == 1):
        printText('Game Over', (300, 300), 80, [0,0,0])

    ''' ZEITEN '''
    FPSCLOCK.tick(FPS)
    pg.display.update()