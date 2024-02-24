import pygame, sys, random

clock = pygame.time.Clock()
from pygame.locals import *
success, failures = pygame.init()
print(f'Success: {success}, failures: {failures}')
pygame.display.set_caption('Sand simualtion')

WINDOW_SIZE = (600,800)
screen = pygame.display.set_mode(WINDOW_SIZE) 

display = pygame.Surface((600/10,800/10))

xl = int(600/10)
yl = int(800/10)
_map = []

class map:

	def __init__(self, size):
		self.size = size
		self.map=[]

	def setPixel(self, x, y, col):
		self.map[y][x] = col

	def getPixel(self, x,y):
		return self.map[y][x]

	def printMap(self):
		for line in self.map:
			for x in line:
				print(x,end="")
			pass
		print("\n")

	def getMap(self):
		return self.map


simMap = map([60,80])

for y in range(int(yl+1)):
	line = []
	for x in range(int(xl+1)):
		line.append(0);
	_map.append(line)

simMap.map = _map
simMap.setPixel(50,3,1)
simMap.setPixel(50,29,1)
simMap.setPixel(50,30,1)
#simMap.printMap()


while True:
    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_d:
                moving_right = True
            if event.key == K_a:
                moving_left = True
    display.fill((105,105,105))

    mx,my = pygame.mouse.get_pos()
    mx = mx/10
    my =my/10
    #print(mx,my)
    click = pygame.mouse.get_pressed()
    if mx > 0 and mx < 59 and my > 0 and my < 80:
    	if click[0]:
    		simMap.setPixel(int(mx),int(my),1)
    	if click[2]:
    		simMap.setPixel(int(mx),int(my),2)
    	if click[1]:
    		simMap.setPixel(int(mx),int(my),3)

    ###
    for line in range(int(yl)-1, -1, -1): #line 79-0

    	for x in range(0, len(_map[line])): 	#char 0-59

    		px = simMap.getPixel(x, line)

    		if px == 1:
    			#print(f"processing pixel {x} : {line} with next {x} : {line+1} being type {simMap.getPixel(x,line+1)}")
    			nextone = simMap.getPixel(x,line+1)
    			if x >= 1:   nextleft = simMap.getPixel(x-1,line+1)
    			else: nextleft = 1
    			if x <= 60-1:	nextright = simMap.getPixel(x+1,line+1)
    			else: nextright = 1


    			rect = pygame.Rect(x, line, 1, 1)
    			pygame.draw.rect(display, (194, 178, 128), rect)
    			### action ###
    			if line < 60-1:
    				#print(simMap.getPixel(line+1,x) )
    				if nextone == 0:
    					simMap.setPixel(x,line,0)
    					simMap.setPixel(x,line+1,1)
    				elif nextone == 3:
    					simMap.setPixel(x,line,0)
    					simMap.setPixel(x,line+1,3)
    				else:
    					if nextleft == 0:
    						simMap.setPixel(x-1, line+1, 1)
    						simMap.setPixel(x, line, 0)
    					elif nextright == 0:
    						simMap.setPixel(x+1, line+1, 1)
    						simMap.setPixel(x, line, 0)
    		if px == 2:
    			#print(f"processing pixel {x} : {line} with next {x} : {line+1} being type {simMap.getPixel(x,line+1)}")
    			nextone = simMap.getPixel(x,line+1)
    			if x >= 1:   nextleft = simMap.getPixel(x-1,line+1)
    			else: nextleft = 1
    			if x <= 60-1:	nextright = simMap.getPixel(x+1,line+1)
    			else: nextright = 1


    			rect = pygame.Rect(x, line, 1, 1)
    			pygame.draw.rect(display, (0, 178, 128), rect)
    			### action ###
    			if line < 60-1:
    				#print(simMap.getPixel(line+1,x) )
    				if nextone == 0:
    					simMap.setPixel(x,line,0)
    					simMap.setPixel(x,line+1,2)
    				else:
    					if nextleft == 0:
    						simMap.setPixel(x-1, line+1, 2)
    						simMap.setPixel(x, line, 0)
    					elif nextright == 0:
    						simMap.setPixel(x+1, line+1, 2)
    						simMap.setPixel(x, line, 0)
    		if px == 3:
    			#print(f"processing pixel {x} : {line} with next {x} : {line+1} being type {simMap.getPixel(x,line+1)}")
    			nextone = simMap.getPixel(x,line+1)
    			if x >= 1:   nextleft = simMap.getPixel(x-1,line+1)
    			else: nextleft = 1
    			if x <= 60-1:	nextright = simMap.getPixel(x+1,line+1)
    			else: nextright = 1
    			if x >= 1:   nleft = simMap.getPixel(x-1,line)
    			else: nleft = 1
    			if x <= 60-1:	nright = simMap.getPixel(x+1,line)
    			else: nright = 1

    			rect = pygame.Rect(x, line, 1, 1)
    			pygame.draw.rect(display, (0,255,255), rect)
    			### action ###
    			if line < 60-1:
    				#print(simMap.getPixel(line+1,x) )
    				if nextone == 0:
    					simMap.setPixel(x,line,0)
    					simMap.setPixel(x,line+1,3)
    				else:
    					if nextleft == 0:
    						simMap.setPixel(x-1, line+1, 3)
    						simMap.setPixel(x, line, 0)
    					elif nextright == 0:
    						simMap.setPixel(x+1, line+1, 3)
    						simMap.setPixel(x, line, 0)
    					else:
    						if nleft == 0:
    							simMap.setPixel(x-1, line, 3)
    							simMap.setPixel(x, line, 0)
    						if nright == 0:
    							simMap.setPixel(x+1, line, 3)
    							simMap.setPixel(x, line, 0)
    ###			
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    deltatime = clock.tick(240)
