import pygame
class Debug:
	def __init__(self):
		self.pos = (5,5)
		self.content = []
		self.font = pygame.font.SysFont(pygame.font.get_fonts()[0], 20)

	def debug(self, info):
		self.content.append(str(info))

	def renderDebug(self):
		surf = pygame.display.get_surface()
		for index, item in enumerate(self.content):
			if type(item) == pygame.Vector2:
				item = str("(" + item.x + " : " + item.y + ")")
			itemText = self.font.render(item, 2, (200,200,200))
			pygame.draw.rect(surf, (0,0,0), pygame.Rect((4, index*itemText.get_height()), (itemText.get_width(), itemText.get_height())))
			surf.blit(itemText, (4, index*itemText.get_height()))
		self.content = []