import random
from settingsAndGeneralFunctions import *
import pygame
from pygame.locals import *

pygame.init()
class Enemy:
    def __init__(self):
        self.value = None
        self.hp = None
        self.position = [random.randint(0,gameWindowSize[0]),random.randint(0,gameWindowSize[1])]
        self.speed = None
        self.type = None
        self.targetOffset = None
        self.offsetVecLength = None
    
    def update(self, target):
        self.move(target)

    def move(self, target):
        vecToTarget = [(target[0] + self.targetOffset[0])-self.position[0], (target[1] + self.targetOffset[1])-self.position[1]]
        scaledVecToTarget = scale(normalize(vecToTarget), self.speed)
        self.position[1] += scaledVecToTarget[1]
        self.position[0] += scaledVecToTarget[0]

    def render(self, surface):
        pygame.draw.rect(surface, (255,0,0), Rect(self.position[0], self.position[1], 30, 30))

class Bottle(Enemy):
    def __init__(self):
        super().__init__()
        self.value = 3
        self.speed = random.randint(2,4)
        self.type = "Bottle"





class Bullet:
    def __init__(self):
        self.damage = None
        self.position = [0,0]
        self.hitbox = [40,40]

class StandartBullet(Bullet):
    def __init__(self):
        super().__init__()
        self.damage = 1
        self.direction = [0,0]
        self.speed = 3
        self.hitbox = [10,10]
        
    def update(self):
        self.move()

    def move(self):
        self.position += scale(normalize(self.direction), self.speed)
    
    def render(self, surface):
        pygame.draw.rect(surface, (0,0,255), Rect(self.position[0], self.position[1], self.hitbox[0], self.hitbox[1]))