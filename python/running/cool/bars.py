
import pygame,random,time
from pygame.locals import *
from collections import deque


success, failures = pygame.init()


screen = pygame.display.set_mode((800,0)) 

x= 0
running = True
direc=True
l = deque(["O"])
for x in range(130):
    l.append(" ")
while running:
    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            running = False
    name=""
    for x in l:
        name +=x
    print(name)
    pygame.display.set_caption(str(name))
    time.sleep(0.01)
    if l[len(l)-1] == "O":
        direc=False
    elif l[0]  == "O":
        direc=True

    if direc:
        l.rotate(1)
    else: l.rotate(-1)
    
