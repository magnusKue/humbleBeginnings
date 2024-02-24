import pygame
from pygame.locals import *
import random
from arena import Arena
from enemy import Bottle, StandartBullet
from player import Player
from settingsAndGeneralFunctions import *
import copy

window = None
running = True
gameState = 1
arena = None

pygame.init()



# Display
pygame.display.set_caption('Teapot')
monitorSize = (pygame.display.Info().current_w, pygame.display.Info().current_h)
window = pygame.display.set_mode(monitorSize, RESIZABLE)

# Surface to draw on
screen = pygame.Surface(gameWindowSize)

# preload surfaces
spriteBg = pygame.image.load("art/placeholderBg.png").convert()


# classes
class Debug:
	def __init__(self):
		self.pos = (5,5)
		self.content = []
		self.font = pygame.font.Font(None, 22)

	def debug(self, info):
		self.content.append(str(info))

	def renderDebug(self):
		surf = pygame.display.get_surface()
		for index, item in enumerate(self.content):
			itemText = self.font.render(item, 2, (200,200,200))
			pygame.draw.rect(surf, (0,0,0), pygame.Rect((4, index*itemText.get_height()), (itemText.get_width(), itemText.get_height())))
			surf.blit(itemText, (4, index*itemText.get_height()))
		self.content = []



allEnemys = [Bottle()]
debugger = Debug()
player = Player()
player.Bullettype = StandartBullet()
clock = pygame.time.Clock()

# Gameloop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False   
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_m:
                gameState = 0
            elif event.key == K_g:
                gameState = 1
            elif event.key == K_r:
                arena.enemys.pop(0)
            elif event.key == K_q:
                arena.enemys[0].position = [random.randint(0,gameWindowSize[0]),random.randint(0,gameWindowSize[1])]

            if event.key == K_a:
                player.walkingA = True
            if event.key == K_d:
                player.walkingD = True
            if event.key == K_w:
                player.walkingW = True
            if event.key == K_s:
                player.walkingS = True

        if event.type == KEYUP:
            if event.key == K_a:
                player.walkingA = False
            if event.key == K_d:
                player.walkingD = False
            if event.key == K_w:
                player.walkingW = False
            if event.key == K_s:
                player.walkingS = False

        if event.type == MOUSEBUTTONDOWN:
            newBullet = copy.deepcopy(player.Bullettype)
            newBullet.direction = player.direction
            newBullet.position = [player.position[0], player.position[1]]
            arena.bullets.append(player.Bullettype)

    window.fill((0,0,0))
    screen.fill((255,0,0))
    debugger.debug(clock.get_fps())
    # # # # # LOGIC # # # # # # # # # # # # # # # # # 

    if gameState == 0: # 0 == Menue
        print("main menu")

    elif gameState == 1: # 1 == init first Round
        arena = Arena()
        arena.round = 1
        gameState = 2

    elif gameState == 2: # 2 == ingame
        # physics

        # logic

        # update bullet list
        for bullet in arena.bullets:
            bullet.update()

        # update enemy lists
        arena.handleEnemyCount(allEnemys, gameWindowSize)
        for enemy in arena.enemys:
            enemy.update(player.position)
        
        # update player
        player.update(debugger)
        pass

    elif gameState == 3: # 3 == change round
        pass

    # # # # # RENDERING # # # # # # # # # # # # # # #
    if not gameState:
        debugger.debug("Main Menu")
    else:
        debugger.debug("In game")
        #render background
        screen.blit(pygame.transform.scale(spriteBg, gameWindowSize), (0,0))
        for enemy in arena.enemys:
            enemy.render(screen)

    for bullet in arena.bullets:
        bullet.render(screen)
    # render player

    player.render(screen)


    debugger.debug(arena.enemys)
    debugger.debug(arena.enemyQueue)

    debugger.renderDebug()
    window.blit(screen, ( (monitorSize[0]-gameWindowSize[0])/2 , (monitorSize[1]-gameWindowSize[1])/2 ))
    ms = clock.tick(60)
    pygame.display.update()

pygame.quit()