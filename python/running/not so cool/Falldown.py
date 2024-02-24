import pygame
import sys
import random

positionsX = list()
positionsY = list()
y = 300
x = 10
speed = 4
tx, ty = 40, 80
enemySize = 60
clock = pygame.time.Clock()
spawnchance = 35
enemySpeed = 3
collisionlist = list()

pygame.init()
screen = pygame.display.set_mode([600, 600])
runcheck = True

def gameover():
	print("Debug:>>>Gameover")
	sys.exit()

def deleteEnemysBehindGap():
	for enemy in range(len(positionsY)-1):
		if positionsX[enemy]< -enemySpeed:
			
			del positionsX[enemy]
			del positionsY[enemy]


def spawn():
	enemyX, enemyY = 600+10, random.randint(10, 600-10-enemySize)
	positionsX.append(enemyX)
	positionsY.append(enemyY)
	#print("Enemy spawned at",enemyX,enemyY)

def moveTargets():
	for enemy in range(0, len(positionsY)):
		positionsX[enemy] -= enemySpeed
		pygame.draw.rect(screen, (255, 0, 0), (positionsX[enemy]-50, positionsY[enemy], enemySize, enemySize))

def pointCollisionTest(edgeX, edgeY):
	px1, px2, py1, py2  =  x, x+tx, y, y+ty
	if edgeX > px1 and edgeX < px2 and edgeY > py1 and edgeY < py2:
		return True
	else:
		return False

def checkCollision():
	for enemy in range(0, len(positionsY)):
		del collisionlist[:]
		px1, px2, py1, py2  =  x, x+tx, y, y+ty
		ex1, ex2, ey1, ey2  =  positionsX[enemy], positionsX[enemy]+enemySize, positionsY[enemy], positionsY[enemy]+enemySize
		collisionlist.append(pointCollisionTest(ex1, ey1))
		collisionlist.append(pointCollisionTest(ex1, ey2))
		collisionlist.append(pointCollisionTest(ex2, ey1))
		collisionlist.append(pointCollisionTest(ex2, ey2))
		print("Debug:>>>",collisionlist)
		for item in collisionlist:
			if item == True:
				gameover()
		

while runcheck:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP] and y>10:
		y-=speed
	if pressed[pygame.K_DOWN] and y<600-(10+ty):
		y+=speed
	
	pygame.draw.rect(screen, (255, 255, 0), (10,y,tx, ty))
	pygame.display.update()
	clock.tick(60)
	screen.fill((0,0,0))

	if random.randint(1, spawnchance) == 1:
		spawn()
	moveTargets()
	checkCollision()
	deleteEnemysBehindGap()
