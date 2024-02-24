import pygame,sys,random
from pygame.locals import *

clock =  pygame.time.Clock()

success, failures = pygame.init()
print(f'Success: {success}, failures: {failures}')

pygame.display.set_caption('path')

WINDOW_SIZE = (600,800)
screen = pygame.display.set_mode(WINDOW_SIZE)
scale = 20
display = pygame.Surface((WINDOW_SIZE[0]/scale,WINDOW_SIZE[1]/scale))
running = True
gamemap = []
for x in range(int(WINDOW_SIZE[1]/scale)):
    line = []
    for x in range(int(WINDOW_SIZE[0]/scale)):
        line.append("0")
    gamemap.append(line)





while running:
    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            running = False

    if True:    #"drawing"
        mx,my = pygame.mouse.get_pos()
        print(mx)
        click = pygame.mouse.get_pressed()
        print(click)
        if click[0]:
            gamemap[int(my/scale)][int(mx/scale)] = "1"

    for line in range(len(gamemap)-1,-1,-1): #"rendering"
        for pixel in range(len(gamemap[0])):
            if gamemap[line][pixel] == "1":
                pygame.draw.rect(display, (100,100,100), pygame.Rect(pixel, line, 1, 1))
            if gamemap[line][pixel] == "2":
                pygame.draw.rect(display, (100,240,100), pygame.Rect(pixel, line, 1, 1))
                
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    display.fill((30,30,30))
    pygame.display.update()
    deltatime = clock.tick(60)