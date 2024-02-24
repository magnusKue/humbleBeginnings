import pygame
from pygame.locals import *
from settingsAndGeneralFunctions import *
pygame.init()

class Player:
    def __init__(self):
        self.position = [0,0]
        self.velocity = [0,0]
        self.direction = [0,0]
        self.acceleration = 0.3
        self.friction = .5
        self.maxSpeed = 4
        self.Bullettype = None

        self.gapToEdges = 5
        self.hitbox = [30, 30]
        self.sprites = {"idle":[], "runningVertcial":[]}
        self.hp = 5
        self.speed = 3

        self.walkingA = False
        self.walkingW = False
        self.walkingS = False
        self.walkingD = False

    def update(self, debugger):
        self.updateVelocity()
        self.clampVelocity()
        self.move()
        debugger.debug(f"position: {self.position}")
        debugger.debug(f"velocity: {self.velocity}")

    def updateVelocity(self):
        if self.walkingA:
            self.direction[0] = -1
            self.velocity[0] -= self.speed * self.acceleration
        elif self.walkingD:
            self.direction[0] = 1
            self.velocity[0] += self.speed * self.acceleration
        else:
            self.direction[0] = 0

        if self.walkingW:
            self.direction[1] = -1
            self.velocity[1] -= self.speed * self.acceleration
        elif self.walkingS:
            self.direction[1] = 1
            self.velocity[1] += self.speed * self.acceleration
        else:
            self.direction[1] = 0

        if self.velocity[0] < 0:
            self.velocity[0] = clamp(self.velocity[0] + self.friction, -999, 0) 
        elif self.velocity[0] > 0:
            self.velocity[0] = clamp(self.velocity[0] - self.friction, 0, 999)

        if self.velocity[1] < 0:
            self.velocity[1] = clamp(self.velocity[1] + self.friction, -999, 0)
        elif self.velocity[1] > 0:
            self.velocity[1] = clamp(self.velocity[1] - self.friction, 0, 999)
        


        self.velocity[1]

    def clampVelocity(self):
        self.velocity[0] = clamp(self.velocity[0], -self.maxSpeed, self.maxSpeed)
        self.velocity[1] = clamp(self.velocity[1], -self.maxSpeed, self.maxSpeed)

    def move(self):
        self.position[0] = clamp(self.position[0] + self.velocity[0], self.gapToEdges, gameWindowSize[0]-self.hitbox[0]-self.gapToEdges)
        self.position[1] = clamp(self.position[1] + self.velocity[1], self.gapToEdges, gameWindowSize[1]-self.hitbox[1]-self.gapToEdges)

    def render(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(self.position[0], self.position[1], self.hitbox[0], self.hitbox[1]))