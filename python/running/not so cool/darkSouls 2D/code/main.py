import pygame, sys
from pygame.locals import *
from SETTINGS import *
from classes import *
from ObjectsAndEntities import *
from debug import Debug


clock = pygame.time.Clock()
success, failures = pygame.init()

root = pygame.display.set_mode((int(WINDOW_SIZE.x), int(WINDOW_SIZE.y)),0,32)


# Tilemanager
tileManager = TileManager()
tileManager.size = pygame.Vector2(16,16)

dirt = pygame.image.load("sorce/dirt.png").convert()
grass = pygame.image.load("sorce/grass.png").convert()

tileManager.tileTypes[0] = tileManager.air
tileManager.tileTypes[1] = TileType("dirt", dirt)
tileManager.tileTypes[2] = TileType("grass", grass)

# player
player = Player()
player.sprite = pygame.image.load("sorce\player.png").convert_alpha()
player.hitbox = player.sprite.get_rect()

# gamemap
gameMap = Map()
gameMap.load(MAPDATA, tileManager)

# camera
cam = Camera()
cam.zoom = 3
cam.mode = CameraModes.lockOnTarget
cam.target = player

# debugger
debugger = Debug()


def exit():
    pygame.quit()
    sys.exit()

def main():
    while True:
        debugger.debug(str(int(clock.get_fps())))
        root.fill((146,244,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_PLUS:
                    cam.zoom =  cam.zoom + 1
                    cam.snapToTarget(player)
                elif event.key == pygame.K_MINUS:
                    cam.zoom = max(1, cam.zoom - 1)
                    cam.snapToTarget(player)

        
        debugger.debug(cam.worldToCam(Vector2(1,1)))

        cam.update()
        #gameMap.render(root, tileManager, cam) # // TODO: Replace scaler with camera
        gameMap.render(root, tileManager, cam)
        player.update(root, cam, gameMap.tiles, tileManager)
        debugger.debug(player.velocity)
        debugger.renderDebug()
        pygame.display.update()
        clock.tick(FPS)

main()