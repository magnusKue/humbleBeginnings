from math import *
from tkinter import colorchooser, filedialog
import pygame, sys, random, time, pygame_gui
from tkinter import *
from pygame.locals import *
from tileProjClasses import *
from uiClass import *

# Pygame
clock = pygame.time.Clock()
success, failures = pygame.init()
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEWHEEL, MOUSEBUTTONUP, MOUSEBUTTONDOWN])
print(f"successes: {success}\nfailures: {failures}")


rootSize = [800, 600]
root = pygame.display.set_mode(rootSize, RESIZABLE)
pygame.display.set_caption("Maple")
# pragma Variables
running = True
project = None # loaded project


# Test project
TestProject = True
if TestProject:
	project = Project()
	project.tileRes = 16
	project.layers = [Layer("Layer: " + str(i)) for i in range(100)]
	project.layers[0].content.append(Chunk(Vec2(0,0),16))	
	project.layers[0].content[0].fill()

	if True: # Tiles
		add1 = staticTile()
		add1.name = "wall"
		add1.sprite = "wall.png"
		project.tileTypes["h001"] = add1
		project.tilesurfaces["h001"] = pygame.image.load("tiles/"+add1.sprite).convert_alpha()

		add1 = staticTile()
		add1.name = "chest"
		add1.sprite = "chest.png"
		project.tileTypes["h002"] = add1
		project.tilesurfaces["h002"] = pygame.image.load("tiles/"+add1.sprite).convert_alpha()

		add1 = staticTile()
		add1.name = "bomb"
		add1.sprite = "bomb.png"
		project.tileTypes["h003"] = add1
		project.tilesurfaces["h003"] = pygame.image.load("tiles/"+add1.sprite).convert_alpha()

		add1 = staticTile()
		add1.name = "wall ladder"
		add1.sprite = "wallLadder.png"
		project.tileTypes["h004"] = add1
		project.tilesurfaces["h004"] = pygame.image.load("tiles/"+add1.sprite).convert_alpha()

		##############
		add1 = staticObject()
		add1.name = "tree"
		add1.sprite = "tree.png"
		project.objectTypes["001"] = add1

	for x in ["Fluid", "Ice"]:
		project.collisionTypes.append(x)
	print(project.collisionTypes)

#debugger = debug()
ui = UI(project, rootSize)
###### functions ##################


if __name__ == "__main__":
	while running:
		deltatime = clock.tick(60) / 1000

		#debugger.debug(int(clock.get_fps()))
		mousePos = pygame.mouse.get_pos()


		# main loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:				
				if event.key == K_ESCAPE:
					running = False
			if event.type == pygame.VIDEORESIZE:
				ui.manager.set_window_resolution(event.size)
				rootSize = event.size
				ui = UI(project, rootSize)		
			ui.manager.process_events(event)
			ui.handleEvents(event, project)
		ui.manager.update(deltatime)
		root.fill(ui.manager.ui_theme.get_colour('dark_bg'))




		ui.manager.draw_ui(root)
		#debugger.renderDebug()
		pygame.display.flip()
	pygame.quit()
	sys.exit()