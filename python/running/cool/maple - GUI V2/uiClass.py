import pygame, pygame_gui
from tileProjClasses import *
class UI:
	def __init__(self, project, rootSize) -> None:

		self.manager = manager = pygame_gui.UIManager(rootSize)

		self.tilesPanelRect = pygame.Rect(50, 50, int(rootSize[0] * 1/5), int(rootSize[1] * 3/5))
		self.tilesPanelRect.bottomright = (-0, -0)

		self.tilesPanel = pygame_gui.elements.UIPanel(self.tilesPanelRect,
									#starting_layer_height=4,
									manager=manager,
									container=manager.get_root_container(),
									anchors={'left': 'right',
											'right': 'right',
											'top': 'bottom',
											'bottom': 'bottom'})

		self.scenePanelRect = pygame.Rect(50, 50, int(rootSize[0] * 1/5), int(rootSize[1] * 2/5))
		self.scenePanelRect.topright = (0, 0)

		self.scenePanel = pygame_gui.elements.UIPanel(self.scenePanelRect,
									#starting_layer_height=4,
									manager=manager,
									container=manager.get_root_container(),
									anchors={'left': 'right',
											'right': 'right',
											'top': 'top',
											'bottom': 'top'})




		## TILES PANEL

		self.button_layout_rect = pygame.Rect(0, 0, self.tilesPanel.get_container().get_rect().width-18, 20)
		self.button_layout_rect.topleft = (10, 10)

		self.b1 = pygame_gui.elements.UIButton(relative_rect=self.button_layout_rect,
				text='test', manager=manager,
				container=self.tilesPanel.get_container(),
				anchors={'left': 'left',
						'right': 'left',
						'top': 'top',
						'bottom': 'top'})
						#,"right_target" : self.tilesPanel.get_abs_rect().right

		b2 = pygame_gui.elements.UIButton(relative_rect=self.button_layout_rect,
				text='test 2', manager=manager,
				container=self.tilesPanel.get_container(),
				anchors={'left': 'left',
						'right': 'left',
						'top': 'top',
						'bottom': 'top',
						'top_target' : self.b1})

		## SCENE PANEL

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
				item_list = ["Layer: " + str(i) for i in range(3)],
				manager=self.manager, allow_multi_select=False,
				allow_double_clicks=True, container=self.scenePanel)
		self.sceneHirachy.set_item_list([str(i.name) for i in project.layers])

		## ADD LAYER WINDOW

		self.addLayerWindow = pygame_gui.windows.UIMessageWindow(pygame.rect.Rect(200,200,200,300), html_message=" ", manager=self.manager, window_title="title")
		self.addLayerWindow.set_minimum_dimensions((250,300))
		self.addLayerWindow.hide()

		button_layout_rect = pygame.Rect(0, 0, 170, 40)
		button_layout_rect.topleft = (10, 10)

		self.addLayerWindowInputField = pygame_gui.elements.UITextEntryLine(button_layout_rect, self.manager, self.addLayerWindow.get_container())
		self.addLayerWindowInputField.set_text("input name")
		
	def handleEvents(self, event, project):
		if event.type in [pygame_gui.UI_BUTTON_DOUBLE_CLICKED, pygame_gui.UI_BUTTON_PRESSED]:
			if event.ui_element == self.removeLayerButton:
				for selected in self.sceneHirachy.get_multi_selection():
					for layer in project.layers:
						if str(layer.name) == str(selected):
							project.layers.remove(layer)
				self.sceneHirachy.set_item_list([str(i.name) for i in project.layers])

			if event.ui_element == self.addLayerButton:
				self.addLayerWindow.show()
				#project.layers.append(Layer(f"Layer: {len(project.layers)+1}"))
				#self.sceneHirachy.set_item_list([str(i.name) for i in project.layers])

