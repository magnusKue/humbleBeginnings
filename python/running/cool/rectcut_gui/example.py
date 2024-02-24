import pygame
from pygame.locals import *

from rectcut import *

running = True
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("rectCut demo")

ui = rectcutManager((600,600))
ui.rectLayout.cutRight("base", 200, "right")
ui.rectLayout.cutBottom("right", 100, "bottom")
ui.rectLayout.cutTop("base", 60, "top")
ui.rectLayout.cutLeft("top", 100, "topLeft")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    ui.render(window)
    pygame.display.flip()
