from pygame import *
import pygame, os
from enum import Enum
from SETTINGS import *
from functions import *

class Transform:
    def __init__(self, pos):
        self.position = pos

class CameraModes(Enum):
    lockOnTarget = 1
    free = 2


class Camera:
    def __init__(self):
        self.freeCamSpeed = 10
        self.speed = .05
        self.zoom = 2
        self.position = pygame.Vector2(0,0)
        self.interpolatedPosition = pygame.Vector2(0,0)
        self.mode = CameraModes.lockOnTarget
        self.target = None

    def update(self):
        if self.mode == CameraModes.lockOnTarget:
            self.position = self.target.position * self.zoom - (.5 * WINDOW_SIZE) + (.5 * pygame.Vector2(self.target.hitbox.width * self.zoom, self.target.hitbox.height * self.zoom))

        elif self.mode == CameraModes.free:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.position.y-=self.freeCamSpeed
            elif keys[pygame.K_s]:
                self.position.y+=self.freeCamSpeed
            if keys[pygame.K_a]:
                self.position.x-=self.freeCamSpeed
            elif keys[pygame.K_d]:
                self.position.x+=self.freeCamSpeed
        
        heading = self.position - self.interpolatedPosition
        self.interpolatedPosition += heading * self.speed
        
    def snapToTarget(self, target):
        self.interpolatedPosition = self.target.position * self.zoom - (.5 * WINDOW_SIZE) + (.5 * pygame.Vector2(self.target.hitbox.width * self.zoom, self.target.hitbox.height * self.zoom))
        
    def worldToCam(self, position):
        return  Vector2((position.x * self.zoom) - self.interpolatedPosition.x, (position.y * self.zoom) - self.interpolatedPosition.y)

        

class TileType:
    def __init__(self, name, tileType): 
        # key in tilemanager -> id
        self.name = name # name for debugging etc
        self.image = tileType # sprite

class SubTile:
    def __init__(self, ttype, position):
        self.type = ttype # TileType index
        self.position = position # Vector2

class TileManager:
    def __init__(self, size = pygame.Vector2(16,16)):
        self.tileTypes = {}
        self.air = 12930256
        self.tileSize = size

class Map:
    def __init__(self):
        self.mapData = []
        self.tiles = []

    def load(self, mapData, tileManager):
        self.mapData = mapData
        for y, line in enumerate(mapData):
            for x, tile in enumerate(line):
                if not tileManager.tileTypes[tile] == tileManager.air:
                    self.tiles.append(SubTile(tile, pygame.Vector2(x, y)))

    def render(self, surface, tileManager, cam):
        for tile in self.tiles:
            ttype = tileManager.tileTypes[tile.type] 
            #ttype => tiletype
            #tile => subtile
            scaledImageSize = pygame.Vector2(int(tileManager.tileSize.x*cam.zoom), int(tileManager.tileSize.y*cam.zoom))
            position = cam.worldToCam(pygame.Vector2(tile.position.x * tileManager.tileSize.x, tile.position.y * tileManager.tileSize.y))
            #pygame.Vector2(int(tile.position.x*tileManager.tileSize.x*cam.zoom - int(cam.interpolatedPosition.x)), int(tile.position.y*tileManager.tileSize.y*cam.zoom - int(cam.interpolatedPosition.y)))
            scaledTile = pygame.transform.scale(ttype.image, (int(scaledImageSize.x), int(scaledImageSize.y)))
            surface.blit(scaledTile, (int(position.x), int(position.y)))
            if DEBUG_MAP:
                surface.blit(ttype.image, (tile.position.x*tileManager.tileSize.x, tile.position.y*tileManager.tileSize.y))

