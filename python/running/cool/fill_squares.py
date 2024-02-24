import pygame, sys, time
from pygame.locals import *

success, failures = pygame.init()
clock = pygame.time.Clock()
print(f'Success: {success}, failures: {failures}') #pygame check thingy

pygame.display.set_caption('root Window')#window caption
monitor_size = (pygame.display.Info().current_w, pygame.display.Info().current_h) #monitor size
WINDOW_SIZE = (monitor_size[0],monitor_size[1]) #window size
screen = pygame.display.set_mode(WINDOW_SIZE,pygame.FULLSCREEN) # initiate the window
display = pygame.Surface((WINDOW_SIZE[0],WINDOW_SIZE[1])) # used as the surface for rendering, is scaled

maps = [
[[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]],

[[1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,0,0,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0]]
]
mapsize = 12 #height i dont remember why

gameRunning = True

zoom = 70 #wanted zoom
trueZoom = 3 #actual zoom
zoomClampLevels = [10,90]
player = [1,1]
offset = [200,0]
offsetVariabel = [0,0]
margin = [int(WINDOW_SIZE[0]/2-mapsize*trueZoom/2),int(WINDOW_SIZE[1]/2-mapsize*trueZoom/2)]

level = 0
game_map = maps[level]
### functions ###
def clamp(val, min=None, max=None):
	if min:
		if val < min: 
			val = min
	if max:
		if val > max: 
			val = max
	return val

### gameloop ###
while gameRunning:
	offset[0] = WINDOW_SIZE[0]/2 - (player[0]*trueZoom+margin[0]+(trueZoom/2)) # x -determins neeeded offset to center the player
	offset[1] = WINDOW_SIZE[1]/2 - (player[1]*trueZoom+margin[1]+(trueZoom/2)) # y
	offsetVariabel[0] += 0.15 * (offset[0]-offsetVariabel[0])
	offsetVariabel[1] += 0.15 * (offset[1]-offsetVariabel[1])
	
	display.fill((0,0,0)) # clear screen
	zoom = clamp(zoom, min=zoomClampLevels[0], max=zoomClampLevels[1]) # clamp zoom to stop the player from zooming in/out to far

	if trueZoom != zoom: # animate shown zoom to move towards wanted zoom
		if trueZoom < zoom:
			trueZoom += 1
		else: trueZoom -= 1

	margin = [int(WINDOW_SIZE[0]/2-mapsize*trueZoom/2),int(WINDOW_SIZE[1]/2-mapsize*trueZoom/2)] #calculate margin (gap between left screen and playfield not using offset)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:

			#zoom events
			if event.key == K_UP:
				zoom+=5
				margin = [int(WINDOW_SIZE[0]/2-mapsize*trueZoom/2),int(WINDOW_SIZE[1]/2-mapsize*trueZoom/2)]
			if event.key == K_DOWN:
				zoom-=5
				margin = [int(WINDOW_SIZE[0]/2-mapsize*trueZoom/2),int(WINDOW_SIZE[1]/2-mapsize*trueZoom/2)]

			#movement (checks if keys are pressed and if the target block is walkable)
			if event.key == K_w and game_map[player[1]-1][player[0]]==0:
				game_map[player[1]][player[0]] = 2 
				player[1] -= 1
			if event.key == K_s and game_map[player[1]+1][player[0]]==0:
				game_map[player[1]][player[0]] = 2
				player[1] += 1
			if event.key == K_a and game_map[player[1]][player[0]-1]==0:
				game_map[player[1]][player[0]] = 2
				player[0] -= 1
			if event.key == K_d and game_map[player[1]][player[0]+1]==0:
				game_map[player[1]][player[0]] = 2
				player[0] += 1
			
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
	fieldCleared = True
	for line in range(len(game_map)): # line = y
		for element in range(len(game_map[line])): # element = x
			if game_map[line][element]==0:
				if not line == player[1] and not element == player[0]:
					fieldCleared = False
			if line == player[1] and element == player[0]:
				color = (255,0,0)
			elif game_map[line][element]==1:
				color = (0,100,0)
			elif game_map[line][element]==2:
				color = (255,100,20)
			else:
				color = (100,100,100)
			#draw tile:
			pygame.draw.rect(display, color, pygame.Rect(offsetVariabel[0]+margin[0]+element*trueZoom, offsetVariabel[1]+margin[1]+line*trueZoom, trueZoom-1, trueZoom-1))
	
	print(player)
	if fieldCleared:
		level+=1
		game_map = maps[level]
	screen.fill((0,0,0))
	screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
	pygame.display.update()
	clock.tick(60)