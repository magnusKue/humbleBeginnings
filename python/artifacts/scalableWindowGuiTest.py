import pygame, pygame_gui
from pygame.locals import *

pygame.init()

rootSize = [800, 600]
root = pygame.display.set_mode(rootSize, RESIZABLE)
pygame.display.set_caption("testings")

running = True
clock = pygame.time.Clock()

class UI:
	def __init__(self) -> None:
		self.manager = manager = pygame_gui.UIManager(rootSize)

		self.tilesPanelRect = pygame.Rect(50, 50, int(rootSize[0] * 1/5), int(rootSize[1] * 3/5))
		self.tilesPanelRect.bottomright = (-0, -0)

		self.tilesPanel = pygame_gui.elements.UIPanel(self.tilesPanelRect,
									# starting_layer_height=4,
									manager=manager,
									container=manager.get_root_container(),
									anchors={'left': 'right',
											'right': 'right',
											'top': 'bottom',
											'bottom': 'bottom'})

		self.scenePanelRect = pygame.Rect(50, 50, int(rootSize[0] * 1/5), int(rootSize[1] * 2/5))
		self.scenePanelRect.topright = (0, 0)

		self.scenePanel = pygame_gui.elements.UIPanel(self.scenePanelRect,
									# starting_layer_height=4,
									manager=manager,
									container=manager.get_root_container(),
									anchors={'left': 'right',
											'right': 'right',
											'top': 'top',
											'bottom': 'top'})




		## TILES

		self.button_layout_rect = pygame.Rect(0, 0, self.tilesPanel.get_container().get_rect().width-18, 20)
		self.button_layout_rect.topleft = (10, 10)

		self.b1 = pygame_gui.elements.UIButton(relative_rect=self.button_layout_rect,
				text='test', manager=manager,
				container=self.tilesPanel.get_container(),
				anchors={'left': 'left',
						'right': 'left',
						'top': 'top',
						'bottom': 'top',
						"right_target" : self.tilesPanel.get_abs_rect().right})

		b2 = pygame_gui.elements.UIButton(relative_rect=self.button_layout_rect,
				text='test 2', manager=manager,
				container=self.tilesPanel.get_container(),
				anchors={'left': 'left',
						'right': 'left',
						'top': 'top',
						'bottom': 'top',
						'top_target' : self.b1})

		## SCENE
		self.button_layout_rect = pygame.Rect(0, 0, 40, 20)
		self.button_layout_rect.topright = (-2, 2)

		self.addLayerButton = pygame_gui.elements.UIButton(relative_rect=self.button_layout_rect,
				text='+', manager=manager,
				container=self.scenePanel.get_container(),
				anchors={'left': 'right',
						'right': 'right',
						'top': 'top',
						'bottom': 'top'})

		self.removeLayerButton = pygame_gui.elements.UIButton(relative_rect=self.button_layout_rect,
				text='-', manager=manager,
				container=self.scenePanel.get_container(),
				anchors={'left': 'right',
						'right': 'right',
						'top': 'top',
						'bottom': 'top',
						"right_target" : self.addLayerButton})

		self.sceneHirachy = pygame_gui.elements.UISelectionList(pygame.rect.Rect(0,25,self.scenePanel.get_abs_rect().width-6,self.scenePanel.get_abs_rect().height-31),
				item_list = ["Layer: " + str(i) for i in range(100)],
				manager=self.manager, allow_multi_select=True,
				allow_double_clicks=True, container=self.scenePanel)

ui = UI()

while running:
	deltatime = clock.tick(60) / 1000

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.VIDEORESIZE:
			ui.manager.set_window_resolution(event.size)
			rootSize = event.size
			ui = UI()
		ui.manager.process_events(event)
		
	ui.manager.update(deltatime)
	root.fill(ui.manager.ui_theme.get_colour('dark_bg'))
	ui.manager.draw_ui(root)

	pygame.display.flip()
pygame.quit()







