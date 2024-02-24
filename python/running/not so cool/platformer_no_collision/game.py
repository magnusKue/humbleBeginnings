import pygame
from UEngine import *
from pygame.locals import *

success, failures = pygame.init()
print(f'Success: {success}, failures: {failures}')
### GAME VARIABLES ###

# ingame
fov = 6

# display
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
windowSize = (int(monitor_size[0]/fov),int(monitor_size[1]/fov))

screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
display = pygame.Surface((windowSize[0],windowSize[1]))

# other
terminated = False
clock = pygame.time.Clock()

#input
leftkey = K_a
rightkey = K_d
upkey = K_w
downkey = K_s

while not terminated:
	screen.fill((255,255,255))
	display.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == leftkey:
				terminated = True

			if event.key == K_ESCAPE:
				terminated = True

		elif event.type == KEYUP:
			if event.key == leftkey:
				pass

		elif event.type == QUIT:
			terminated = True
	pygame.draw.circle(display, (100,100,100), (windowSize[0]/2,windowSize[1]/2),3, 0)


	screen.blit(pygame.transform.scale(display,monitor_size),(0,0))
	pygame.display.update()
	deltatime = clock.tick(60)

pygame.quit()

