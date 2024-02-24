import pygame, pygame_gui, time
from pygame.locals import *

pygame.init()

root = pygame.display.set_mode((800,600), RESIZABLE)
running = True
manager = pygame_gui.UIManager((800, 600), 'data/themes/quick_theme.json')
clock = pygame.time.Clock()


def initConsole():
    horst = pygame_gui.windows.UIConsoleWindow(rect=pygame.rect.Rect((50, 50), (700, 500)), manager=manager, window_title="cocksole")
    horst.add_output_line_to_log("Type your command in the text field below",True, False, True)
    horst.set_log_prefix("$~ ")
    return horst

panel = pygame_gui.elements.UIPanel(pygame.Rect(50, 50, 200, 300),
                             manager=manager)

button = pygame_gui.elements.UIButton(pygame.Rect(10, 10, 174, 30), 'Panel Button',
                 manager=manager,
                 container=panel)

console_window = initConsole()
while running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                pygame.quit()
            elif event.key == K_n:
                console_window.kill()
                console_window = initConsole()
                print(manager.get_window_stack())
        
        if event.type == pygame_gui.UI_CONSOLE_COMMAND_ENTERED:
            if event.command == "cock":
                time.sleep(.1)
                console_window.add_output_line_to_log("yes, cock",True, False, True)
            elif event.command == "exit":
                console_window.hide() #clear_log()
        manager.process_events(event)
    
    manager.update(time_delta)
    root.fill(manager.ui_theme.get_colour('dark_bg'))
    manager.draw_ui(root)
    pygame.display.update()