from pygame.display import toggle_fullscreen
from UEngine02v import *
from classes import *
import pygame, sys, os, random, math

clock = pygame.time.Clock()

from pygame.locals import *

success, failures = pygame.init()
print(f'Success: {success}, failures: {failures}')

### USERVARIABLES ###

fullscreen = False
windowedWindowSize = 1.5 #monitor size / this = size

### fUNCTIONS ###

def loadMap():
    map1 = []
    mapFile = open("maps/map.txt", 'r')
    for line in mapFile:
        map1.append(line.replace('\n','').split())
    return map1
    #bonfires = map_.bonfires

### DISPLAY ###

pygame.display.set_caption('John Darksouls\'s adventure')

monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
if not fullscreen:
    zoom = 3
    print("not using Fullscreen")
    windowSize = (int(monitor_size[0]/windowedWindowSize),int(monitor_size[1]/windowedWindowSize))
    screen = pygame.display.set_mode(windowSize,pygame.NOFRAME) 
else:
    zoom = 4
    print("using Fullscreen")
    windowSize = (int(monitor_size[0]),int(monitor_size[1]))
    screen = pygame.display.set_mode(windowSize,pygame.FULLSCREEN) 

canvas = pygame.Surface((windowSize[0]/zoom,windowSize[1]/zoom)) 
running = True
print("---\nmonitor: ",monitor_size, "\nwindow: ", windowSize, "\ncanvas: ", [canvas.get_width(), canvas.get_height()], "\n---\n")
### init ###
FPS = 60;

john = john()
john.maxStamina = 500;
john.maxHP = 2000
john.position = Vec((windowSize[0] /zoom )/2  ,(windowSize[1] /zoom) /2)
john.position.printV()
tilesize = 16


map1 =loadMap()
#print(map1)

cameraOffset = Vec(0,0)
cameraOffsetGoal = Vec(0,0)
gamemap = map1

while running:
    canvas.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == K_LEFT:
                cameraOffset.x -= 15
            if event.key == K_RIGHT:
                cameraOffset.x += 15
            if event.key == K_UP:
                cameraOffset.y -= 15
            if event.key == K_DOWN:
                cameraOffset.y += 15


#       Physics         #
    
#       RENDERING       #
    #TILEMAP

    y = 0
    for layer in gamemap:
        x = 0
        #if not y*16 < player_rect.y- renderDistance * 16 and not y*16 > player_rect.y+ renderDistance * 16:
        for tile in layer[0]:
            #if not x*16 < player_rect.x- renderDistance * 16 and not x*16 > player_rect.x+ renderDistance * 16:
            if tile == '1':
                pygame.draw.rect(canvas, (0,0,255), pygame.Rect(x*tilesize-cameraOffset.x, y*tilesize-cameraOffset.y, tilesize, tilesize))
            if tile == '2':
                pygame.draw.rect(canvas, (0,255,0), pygame.Rect(x*tilesize-cameraOffset.x, y*tilesize-cameraOffset.y, tilesize, tilesize))            
            x += 1
        y += 1

    #PLAYER:
    pygame.draw.rect(canvas, (0,140,0), pygame.Rect(john.position.x-(0.5*tilesize), john.position.y-(0.5*tilesize), tilesize, tilesize))

#       DISPLAY         #
    screen.blit(pygame.transform.scale(canvas, windowSize),(0,0))
    pygame.display.update()
    deltatime = clock.tick(60)

#TODO: save
