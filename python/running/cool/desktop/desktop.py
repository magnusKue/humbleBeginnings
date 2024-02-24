'''
Projekt: Desktop
Ersteller: Magnus Küderli

Beschreibung: Spiel das auf einem klassischen desktop stattfindet, auf dem komische dinge passieren
und der spieler muss die ursache dessen finden.

Fragen:
Virus / übernatürliches

'''


import pygame, sys, random, time
from pygame.locals import *

import winC
# Pygame

clock = pygame.time.Clock()
success, failures = pygame.init()
print(f"successes: {success}\nfailures: {failures}")

pygame.display.set_caption('John Darksouls\'s adventure')
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
s = 1
screen = pygame.display.set_mode((int(monitor_size[0]/s), int(monitor_size[1]/s)), pygame.NOFRAME)

# Variables

FPS = 60;
state = 0; # 0=test, 1=Boot, 2=desktop, 3=cutscene
running = True
mousePos = [0,0];
mouse = "up"
# Objects

winManager = winC.windowManager()
taskBar = winC.taskbar()

it1 = winC.window((500, 700), [0,0], "Jobs")
#(content)
icon1 = pygame.Surface((40,40))
icon1.fill((250,250,250))
pygame.draw.rect(icon1, (10,10,10), (1,1,19,19))
pygame.draw.rect(icon1, (10,10,10), (21,1,19,19))
pygame.draw.rect(icon1, (10,10,10), (1,21,19,19))
pygame.draw.rect(icon1, (10,10,10), (21,21,19,19))
link1 = winC.link(icon1, it1, 1)

taskBar.links.append(link1)


it1 = winC.window((300, 400), [0,0], "Cock")
#(content)
icon1 = pygame.Surface((40,40))
icon1.fill((250,250,250))
pygame.draw.rect(icon1, (120,120,120), (10,1,20,20))
pygame.draw.rect(icon1, (120,120,120), (5,20,30,20))
link1 = winC.link(icon1, it1, 0)
taskBar.links.append(link1)


# Funktions

# Gameloop

while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_q:
                win = winC.window((random.randint(200,400),random.randint(200,400)), [random.randint(0,monitor_size[0]),random.randint(0,monitor_size[1])], random.choice(["#","+","ß","0","9","8","7","6","5","4","3","2","1","m","n","b","v","c","x","y","q","w","e","r","t","z","u","i","o","p","ü","ä","ö","l","k","j","h","g","f","d","a",]) )
                pygame.draw.rect(win.surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (50,50,100,100))
                winManager.windows.append(win)

                
        #Mouse
        if event.type == pygame.MOUSEBUTTONDOWN and mouse == "static":
            mouse = "down"
        elif event.type == pygame.MOUSEBUTTONUP and mouse == "static":
            mouse = "up"
            winManager.snap = None
            winManager.snapOffset = [0,0]
        else: mouse = "static"


    # GAME- general
    mousePos = pygame.mouse.get_pos()

    # GAME - states 
    print(winManager.windows)
    if state == 0: # TEST
        winManager.manage(mousePos, mouse, monitor_size, screen, taskBar.height)
        taskBar.manage(mousePos, mouse, monitor_size, screen, winManager)
    elif state == 1:
        for window in winManager.windows:
            pass

    #print("\n\n")
    pygame.display.update()
    deltatime = clock.tick(FPS)
pygame.quit()