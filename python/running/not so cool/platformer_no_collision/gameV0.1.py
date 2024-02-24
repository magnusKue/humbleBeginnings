import pygame
from UEngine import *
from pygame.locals import *

success, failures = pygame.init()
print(f'Success: {success}, failures: {failures}')
### GAME VARIABLES ###

# ingame
fov = 4
scroll = Vec2(0,0)
gamePause = False
friction = .94
gravity = .01

# display
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
windowSize = (int(monitor_size[0]/fov),int(monitor_size[1]/fov))

screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
display = pygame.Surface((windowSize[0],windowSize[1]))

# other
terminated = False
clock = pygame.time.Clock()

# map
tilelistPaths = {
			1: "mapData/tiles/dirt.png",
			2: "mapData/tiles/grass.png"}

tilelist ={}
for key in tilelistPaths:
	tilelist[key] = pygame.image.load(tilelistPaths[key])

gameMap = Map(16, tilelist)
mapPath = "mapData\\map"
playerPos = gameMap.load(mapPath)

#input
leftkey = K_a
rightkey = K_d
upkey = K_w
downkey = K_s

moving = {
	"right":False,
	"left":False,
	"up":False,
	"down":False
}

class Player:
	def __init__(self, path, pos, size, speed):
		self.sprite = pygame.image.load(path)
		self.position = pos
		self.velocity = vecZERO
		self.inventory = []
		self.size = size
		self.speed = speed

	def update(self):
		self.position = addVec(self.position, self.velocity)

	def render(self, scroll):
		display.blit(self.sprite, (self.position.x-scroll.x, self.position.y-scroll.y))

player = Player("player.png", playerPos, Vec2(8,8), .1)

while not terminated:
	screen.fill((255,255,255))
	display.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == leftkey:
				moving["left"] = True
			if event.key == rightkey:
				moving["right"]=True
			if event.key == upkey:
				moving["up"]=True
			if event.key == downkey:
				moving["down"]=True
			if event.key == K_p:
				gamePause = not gamePause
			if event.key == K_ESCAPE:
				terminated = True

		elif event.type == KEYUP:
			if event.key == leftkey:
				moving["left"] = False
			if event.key == rightkey:
				moving["right"]=False
			if event.key == upkey:
				moving["up"]=False
			if event.key == downkey:
				moving["down"]=False

		elif event.type == QUIT:
			terminated = True

	tileList, tileSize, tileTypes = gameMap.getRenderingInfo()
	### PHYSICS ###
	col = False
	playerrec = rect(player.position, player.size)
	for tile in tileList:
		tilerec = rect(tile.position, Vec2(16, 16))
		if rectCol(playerrec, tilerec) and tile.tileType != "0":
			col= True
		pygame.draw.rect(display, (255,0,0), pygame.Rect(player.position.x/7, player.position.y/7, 8/7, 8/7))
		print(tile.tileType)
		if tile.tileType != "0":
			pygame.draw.rect(display, (0,0,255), pygame.Rect(tile.position.x/7, tile.position.y/7, 16/7, 16/7))

	if not gamePause:
		if moving["left"]:
			player.velocity.x -= player.speed
		elif moving["right"]:
			player.velocity.x += player.speed
		player.velocity.x *= friction
		player.velocity.y += .01

		if not col:
			player.update()


	### RENDERING ###
	## map
	for tile in tileList:
		if not int(tile.tileType) == 0:
			display.blit(tileTypes[int(tile.tileType)],(tile.position.x-scroll.x,tile.position.y-scroll.y))
	
	## other
	player.render(scroll)
	if col:
		pygame.draw.circle(display, (100,100,100), (windowSize[0]/2,windowSize[1]/2),3, 0)


	scroll = Vec2(player.position.x - windowSize[0]/2 + (player.size.x/2), player.position.y - windowSize[1]/2 + (player.size.y/2))
	screen.blit(pygame.transform.scale(display,monitor_size),(0,0))
	pygame.display.update()
	deltatime = clock.tick(60)

pygame.quit()

