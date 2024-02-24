from asyncio.subprocess import SubprocessStreamProtocol

import pygame, random
from pygame.locals import *

class window:
    def __init__(self, size=(400,300), position=[0,0], caption="window"):
        self.position = position;
        self.size = size;
        self.caption = caption;
        self.surface = pygame.Surface(self.size)

        self.surface.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    
    def update(self):
        pass

    print("initiated")

class windowManager:
    def __init__(self):
        self.windows = []
        self.snap = None
        self.snapOffset = [0,0]
        self.windowBorderHeight = 30
    
    def manage(self, mousePos, mouse, monitor_size, screen, taskbarHeight):
        collidingWithMouse = []
        
        for index in range(len(self.windows)):
            item = self.windows[index]
            if mousePos[0] > item.position[0] and mousePos[0] < item.position[0] + item.size[0]:
                if mousePos[1] > item.position[1]-self.windowBorderHeight and mousePos[1] < item.position[1]:
                    collidingWithMouse.append(index)

            screen.blit(item.surface, item.position)
            pygame.draw.rect(screen, (255,255,255), (item.position[0], item.position[1]-self.windowBorderHeight, item.size[0], self.windowBorderHeight) )

            if self.snap == None:
                item.position[1] = clamp(item.position[1], self.windowBorderHeight, monitor_size[1]-item.size[1]-taskbarHeight)

        
        if collidingWithMouse != []:
            if mouse == "down":
                print("rearanged")
                foreWin = collidingWithMouse[0]
                self.windows = movetoend(self.windows, foreWin)
                self.snap = len(self.windows)-1
                self.snapOffset[0] = self.windows[foreWin].position[0] - mousePos[0]
                self.snapOffset[1] = self.windows[foreWin].position[1] - mousePos[1]

        if self.snap != None:
            self.windows[self.snap].position[0] = mousePos[0] + self.snapOffset[0]
            self.windows[self.snap].position[1] = mousePos[1] + self.snapOffset[1]

class link:
    def __init__(self, icon, window, typ=1):
        self.icon = icon
        self.window = window
        self.type = typ

class taskbar:
    def __init__(self):
        self.height = 45
        self.links = []
    
    def manage(self, mousePos, mouse, monitor_size, screen, windowManager):
        pygame.draw.rect(screen, (240,240,240), (0, monitor_size[1]-self.height, monitor_size[0], monitor_size[1]))

        for index in range(len(self.links)):
            link = self.links[index]
            screen.blit(link.icon, ((40+10) * index + 2, monitor_size[1]-self.height + 2) )

            if mousePos[0] > ((40+10) * index + 2) and mousePos[0] < ((40+10) * index + 42):
                if mousePos[1] > monitor_size[1]-self.height and mousePos[1] < monitor_size[1]:
                    if mouse == "down" and link.type == 1:
                        windowManager.windows.append(link.window)

def movetoend(wlist, index):
    wlist.append(wlist.pop(index)) 
    return wlist

def clamp(value, min, max):
    ret = value
    if ret < min:
        ret = min
    elif ret > max:
        ret = max
    return ret