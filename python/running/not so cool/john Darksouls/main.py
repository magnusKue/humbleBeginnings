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

def toScreenspaceX(value):
    return value - cameraOffset.x
    
def toScreenspaceY(value):
    return value - cameraOffset.y
    

### DISPLAY ###

pygame.display.set_caption('John Darksouls\'s adventure')

monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
if not fullscreen:
    zoom = 2
    print("not using Fullscreen")
    windowSize = (int(monitor_size[0]/windowedWindowSize),int(monitor_size[1]/windowedWindowSize))
    screen = pygame.display.set_mode(windowSize,pygame.NOFRAME) 
else:
    zoom = 3
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

enemys = []

movingH = 0
movingV = 0

map1 =loadMap()
#print(map1)

cameraOffset = Vec(0,0)
cameraOffsetGoal = Vec(0,0)
gamemap = map1



enemys.append(enemy())

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
                movingH = -1
            if event.key == K_RIGHT:
                movingH = 1
            if event.key == K_UP:
                movingV = -1
            if event.key == K_DOWN:
                movingV = 1

        if event.type == KEYUP:
            if event.key == K_LEFT:
                movingH = 0
            if event.key == K_RIGHT:
                movingH = 0
            if event.key == K_UP:
                movingV = 0
            if event.key == K_DOWN:
                movingV = 0

#       Physics         #

#JOHN            
    john.velocity.y += movingV * .2
    john.velocity.x += movingH * .2
    #john.velocity.normalize()
    john.position = addVec(john.position, john.velocity)
    john.velocity.x *= john.friction
    john.velocity.y *= john.friction

#CAMERA
    cameraOffsetGoal.x =  john.position.x - canvas.get_width()/2
    cameraOffsetGoal.y =  john.position.y - canvas.get_height()/2

    cameraOffset.x += ((cameraOffsetGoal.x - cameraOffset.x))/40
    cameraOffset.y += ((cameraOffsetGoal.y - cameraOffset.y))/40
    #true_scroll[1] += (player_rect.y-true_scroll[1]-monitor_size[1]/zoom/2)/20

    #cameraMovementDirection = getDirectionVec(cameraOffset, cameraOffsetGoal)
    #cameraMovementDirection.printV()
    #cameraOffset.x +=  cameraOffsetGoal.x * 0.1
    
#       RENDERING       #
    #TILEMAP

    '''y = 0
    for layer in gamemap:
        x = 0
        #if not y*16 < player_rect.y- renderDistance * 16 and not y*16 > player_rect.y+ renderDistance * 16:
        for tile in layer[0]:
            #if not x*16 < player_rect.x- renderDistance * 16 and not x*16 > player_rect.x+ renderDistance * 16:
            if tile == '1':
                pygame.draw.rect(canvas, (0,0,255), pygame.Rect(toScreenspaceX(x*tilesize), toScreenspaceY(y*tilesize), tilesize, tilesize))
            if tile == '2':
                pygame.draw.rect(canvas, (0,255,0), pygame.Rect(toScreenspaceX(x*tilesize), toScreenspaceY(y*tilesize), tilesize, tilesize))            
            x += 1
        y += 1'''
    for x in range(200): #TODO: finish
        pygame.draw.rect(canvas, (0,0,255), pygame.Rect(toScreenspaceX(x*tilesize), toScreenspaceY((math.sin(2*x)+math.sin(.5*x)+math.sin(.1*x))*tilesize), tilesize, tilesize))

    #PLAYER:
    pygame.draw.rect(canvas, (0,140,0), pygame.Rect(toScreenspaceX(john.position.x-(0.5*tilesize)), toScreenspaceY(john.position.y-(0.5*tilesize)) , tilesize, tilesize))
    

    #ENEMYS
    for each in enemys:
        if each.targetPlayer: colorA = (0,255,0)
        else: colorA = (140,0,0)
        pygame.draw.rect(canvas, colorA, pygame.Rect(toScreenspaceX(each.position.x-(0.5*tilesize)), toScreenspaceY(each.position.y-(0.5*tilesize)) , tilesize, tilesize))
        if getDistance(john.position, each.position) <= 200:
            each.targetPlayer = True
        if each.targetPlayer:
            dire = getDirectionVec(each.position, john.position)
            if not dire.getLength() <= 30:
                each.position = addVec(each.position, mulVec(dire, Vec(0.01, 0.01)))

#       DISPLAY         #
    screen.blit(pygame.transform.scale(canvas, windowSize),(0,0))
    pygame.display.update()
    deltatime = clock.tick(FPS)

#TODO: save
