#imports
import pygame, sys, time, random
from pygame.locals import *
#setup pygame
pygame.init()
mainClock = pygame.time.Clock()
#setup window
WINDOWHEIGHT = 600
WINDOWWIDTH = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('red <3 yellow')
#movement
moveLeft = False
moveRight = False
moveUp = False
moveDown = True

MOVESPEED = 1
#colors
RED = (255, 0, 0)
TURQUOISE = (0, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
#variables
basicFont = pygame.font.SysFont(None, 28)
COINSIZE = 25
SQUARE = True
player = pygame.Rect(525,25,45,45)
materials = []
LEVEL = 1
number=0
#generate coins
for m in range(35):
    materials.append(pygame.Rect(random.randint(55, WINDOWWIDTH - 80 - COINSIZE), random.randint(0, WINDOWHEIGHT - COINSIZE), COINSIZE, COINSIZE))
star = pygame.Rect(0,275,40,40)
CIRCLE=True
#events
while SQUARE==True:
    while CIRCLE==True:
        time.sleep(1)
        if number==1:
            text = basicFont.render('You have won once now, press "P" to play!', True, BLACK, YELLOW)
        if number==0:
            text = basicFont.render('You have not won any in a row, press "P" to play!', True, BLACK, YELLOW)
        if number>1:
            text = basicFont.render('You have won ' + str(number) + ' times in a row, press "P" to play!', True, BLACK, YELLOW)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery
        for spikes in materials[:]:
            materials.remove(spikes)
        for event in pygame.event.get():
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()
            if event.type == KEYDOWN:
                if event.key == ord("p"):
                    player = pygame.Rect(525,25,45,45)
                    moveLeft = False
                    moveRight = False
                    moveUp = False
                    moveDown = True
                    for m in range(35):
                        materials.append(pygame.Rect(random.randint(55, WINDOWWIDTH - 80 - COINSIZE), random.randint(0, WINDOWHEIGHT - COINSIZE), COINSIZE, COINSIZE))
                    CIRCLE=False
        windowSurface.fill(TURQUOISE)
        pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

        windowSurface.blit(text, textRect)

        pygame.display.update()
        mainClock.tick(150)
    for event in pygame.event.get():
        if event.type == QUIT:
              pygame.quit()
              sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                moveUp = False
                moveDown = False
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveUp = False
                moveDown = False
                moveRight = True
                moveLeft = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = True
                moveDown = False
                moveRight = False
                moveLeft = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
                moveRight = False
                moveLeft = False
    #window drawing current
    windowSurface.fill(GRAY)
    pygame.draw.rect(windowSurface, RED, player)
    pygame.draw.rect(windowSurface, YELLOW, star)
    #getting killed
    for spikes in materials[:]:
        if player.colliderect(spikes):
            number=0
            CIRCLE=True
    if player.colliderect(star):
        number=number+1
        CIRCLE=True
    if player.top <= 0:
        number=0
        CIRCLE=True
    if player.bottom >=600:
        number=0
        CIRCLE=True
    if player.left <= 0:
        number=0
        CIRCLE=True
    if player.right >=600:
        number=0
        CIRCLE=True
    # draw the food
    for m in range(len(materials)):
        pygame.draw.rect(windowSurface, BLACK, materials[m])
    #movement
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.bottom += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
    #display
    pygame.display.update()
    mainClock.tick(150)
