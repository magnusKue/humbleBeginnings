import pygame, sys
from pygame.locals import *
from SETTINGS import *
from classes import Brick

success, failure = pygame.init()
print(f"{success} successes, {failure} failures")

root = pygame.display.set_mode((WINX, WINY))
pygame.display.set_caption("Breakers")


running = True
levelBricks = []

brickWidth = WINX/10
brickHeight = 20

bricksSpace = WINY * .5
minLineGap = 20

def exit():
    pygame.quit()
    sys.exit()

def generateBricks(lines):
    resBricks = []
    for iterator, content in enumerate(lines):
        for brick in range(content):
            posX = int((WINX / content +1) * (brick+1))
            posY = int((bricksSpace / len(lines)) * iterator + minLineGap)
            resBricks.append(Brick(pygame.Vector2(posX, posY)))
    return resBricks

def drawBricks(bricks):
    for brick in bricks:
        pygame.draw.rect(root, (255,0,0), (brick.pos.x, brick.pos.y, brickWidth, brickHeight))

levelBricks = generateBricks([1,2,3,4,5,8])

while running:
    root.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    drawBricks(levelBricks)
    pygame.display.flip()
