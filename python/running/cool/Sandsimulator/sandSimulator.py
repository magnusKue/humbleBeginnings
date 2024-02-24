import pygame, sys, random

clock = pygame.time.Clock()
from pygame.locals import *
success, failures = pygame.init()
print(f'Success: {success}, failures: {failures}')
pygame.display.set_caption('Sand simualtion')
# programIcon = pygame.image.load('icon.png')
# pygame.display.set_icon(programIcon)

WINDOW_SIZE = (600,800)
screen = pygame.display.set_mode(WINDOW_SIZE) 
scale = 6
display = pygame.Surface((WINDOW_SIZE[0]/scale,WINDOW_SIZE[1]/scale))

spawners = []
colors = {1:(194, 178, 128),2:(0, 178, 128),3:(0,255,255),4:(60,60,60), 0:(60,60,60)}
bg = (105,105,105)

p2 = [[1,0],[0,1],[1,1],[2,1],[1,2]]
p3 = [[1,0],[2,0],[0,1],[1,1],[2,1],[3,1],[0,2],[1,2],[2,2],[3,2],[1,3],[2,3]]

konstantflow = True
emptyGround = False

xl = int(600/scale)
yl = int(800/scale)
_map = []
placemode = 1
showGround = False
pensize = 1
simulating = True
slowMotion = False
maxFps = 50000000
FPS = maxFps
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

running = True

while running:
    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
            	running = False
            if event.key == K_t:
            	konstantflow = not konstantflow
            if event.key == K_SPACE:
            	simulating = not simulating
            if event.key == K_z:
            	emptyGround = not emptyGround
            elif event.key == K_1:
            	placemode = 1
            elif event.key == K_2:
            	placemode = 2
            elif event.key == K_3:
            	placemode = 3
            elif event.key == K_4:
            	placemode = 4
            elif event.key == K_0:
            	placemode = 0  
            elif event.key == K_w:
            	slowMotion = not slowMotion
            elif event.key == K_r:
            	showGround = not showGround
            elif event.key == K_f:
            	mx,my =pygame.mouse.get_pos()
            	mx=mx/scale
            	my=my/scale
            	replace = simMap.getPixel(int(mx),int(my))
            	color = placemode
            	for line in range(int(yl)-1, -1, -1):
            		for x in range(0, len(simMap.map[line])):
            			px = simMap.getPixel(x, line)
            			if px == replace : #and not replace == 0
            				simMap.setPixel(x,line,color)
            elif event.key == K_q:
            	if pensize < 3:
            		pensize += 1
            	else:
            		pensize = 1
            elif event.key == K_c:
            	mx,my = pygame.mouse.get_pos()
            	mx = mx/scale
            	my = my/scale
            	#print(spawners)
            	for i in range( len(spawners) - 1, -1, -1) :
            		if spawners[i][0] >= mx -5 and spawners[i][0] <= mx +5:
            			if spawners[i][1] >= my -5 and spawners[i][1] <= my +5:
            				garbageCollection = spawners.pop(i)
            elif event.key == K_e:
            	spawners = []
            	for y in range(int(yl+1)):
            		for x in range(int(xl+1)):
            			simMap.setPixel(x,y,0)

    display.fill(bg)
    if slowMotion:
    	FPS = 4
    else:
    	FPS = maxFps
    mx,my = pygame.mouse.get_pos()
    mx = mx/scale
    my =my/scale
    #print(mx,my)
    click = pygame.mouse.get_pressed()
    if mx > 0 and mx < 600/scale-1 and my > 0 and my < 800/scale-50:
    	if click[0]:
    		if pensize == 1:
    			simMap.setPixel(int(mx),int(my),placemode)
    		if pensize == 2:
    			for coords in p2:
    				if random.randint(0,1) == 0 or konstantflow:
    					simMap.setPixel(int(coords[0]+mx-1),int(coords[1]+my-1),placemode)
    		elif pensize == 3:
    			for coords in p3:
    				if random.randint(0,1) == 0 or konstantflow:
    					simMap.setPixel(int(coords[0]+mx-1),int(coords[1]+my-1),placemode)
    	if click[1]:
    		if placemode in [1,2,3]:
    			if pensize == 1:
    				spawners.append([int(mx),int(my),placemode])
    			if pensize == 2:
    				for coords in p2:
    					spawners.append([int(coords[0]+mx-1),int(coords[1]+my-1),placemode])
    			if pensize == 3:
    				for coords in p3:
    					spawners.append([int(coords[0]+mx-1),int(coords[1]+my-1),placemode])
    ###
    for line in range(int(yl)-1, -1, -1):
    	for x in range(0, len(_map[line])):
    		px = simMap.getPixel(x, line)

    		if px == 1:
    			nextone = simMap.getPixel(x,line+1)
    			if x >= 1:
    				nextleft = simMap.getPixel(x-1,line+1)
    			else: 
    				nextleft = 1
    			if x <= 600/scale-1:	
    				nextright = simMap.getPixel(x+1,line+1)
    			else: 
    				nextright = 1
    			rect = pygame.Rect(x, line, 1, 1)
    			pygame.draw.rect(display, colors[1], rect)
    			### action ###
    			if line < 600/scale-1 and simulating:
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
    			if x >= 1:   
    				nextleft = simMap.getPixel(x-1,line+1)
    			else: 
    				nextleft = 1
    			if x <= 600/scale-1:	
    				nextright = simMap.getPixel(x+1,line+1)
    			else: 
    				nextright = 1
    			if x >= 2:
    				jnLeft = simMap.getPixel(x-2,line+1)
    			else: jnLeft = 1
    			if x <= 600/scale-2:
    				jnRight = simMap.getPixel(x+2,line+1)
    			else:
    				jnRight = 1

    			rect = pygame.Rect(x, line, 1, 1)
    			pygame.draw.rect(display, colors[2], rect)
    			### action ###
    			if line < 600/scale-1 and simulating:
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
    					else:
    						if jnLeft == 0:
    							simMap.setPixel(x-2,line+1,2)
    							simMap.setPixel(x,line,0)
    						elif jnRight == 0:
    							simMap.setPixel(x+2,line+1,2)
    							simMap.setPixel(x,line,0)


    						
    		if px == 3:
    			#print(f"processing pixel {x} : {line} with next {x} : {line+1} being type {simMap.getPixel(x,line+1)}")
    			nextone = simMap.getPixel(x,line+1)

    			if x >= 1:   nextleft = simMap.getPixel(x-1,line+1)
    			else: nextleft = 1
    			if x <= 600/scale-1:	nextright = simMap.getPixel(x+1,line+1)
    			else: nextright = 1

    			if x >= 2:   left = simMap.getPixel(x-2,line+1)
    			else: left = 1
    			if x <= 600/scale-2:	right = simMap.getPixel(x+2,line+1)
    			else: right = 1

    			if x >= 2:   nleft = simMap.getPixel(x-2,line+1)
    			else: nleft = 1
    			if x <= 600/scale-2:	nright = simMap.getPixel(x+2,line+1)
    			else: nright = 1

    			if x >= 3:   nnleft = simMap.getPixel(x-3,line+1)
    			else: nnleft = 1
    			if x <= 600/scale-3:	nnright = simMap.getPixel(x+3,line+1)
    			else: nnright = 1

    			rect = pygame.Rect(x, line, 1, 1)
    			pygame.draw.rect(display, colors[3], rect)
    			### action ###
    			if line < 600/scale-1 and simulating:
    				#print(simMap.getPixel(line+1,x) )
    				if nextone == 0:
    					simMap.setPixel(x,line,0)
    					simMap.setPixel(x,line+1,3)
    				else:
    					if nextleft == 0:
    						simMap.setPixel(x, line, 0)
    						simMap.setPixel(x-1, line+1, 3)
    					elif nextright == 0:
    						simMap.setPixel(x, line, 0)
    						simMap.setPixel(x+1, line+1, 3)
    					else:
    						if nleft == 0:
    							simMap.setPixel(x, line, 0)
    							simMap.setPixel(x-2, line+1, 3)
    						elif nright == 0:
    							simMap.setPixel(x, line, 0)
    							simMap.setPixel(x+2, line+1, 3)
    						else:
    							if nnleft == 0:
    								simMap.setPixel(x, line, 0)
    								simMap.setPixel(x-3, line+1, 3)
    							elif nnright == 0:
    								simMap.setPixel(x, line, 0)
    								simMap.setPixel(x+3, line+1, 3)
    							else:
    								if left == 0:
    									simMap.setPixel(x,line,0)
    									simMap.setPixel(x-1,line,3)
    								elif right == 0:
    									simMap.setPixel(x,line,0)
    									simMap.setPixel(x+1,line,3)
    		if px == 4:
    			rect = pygame.Rect(x, line, 1, 1)
    			pygame.draw.rect(display, colors[4], rect)

    rect = pygame.Rect(1, 1, 60/scale, 60/scale)
    pygame.draw.rect(display, colors[placemode], rect)

    rect = pygame.Rect(1, 1, 1, 1)
    pygame.draw.rect(display, bg, rect)
    rect = pygame.Rect(1, 60/scale,1,1)
    pygame.draw.rect(display, bg, rect)
    rect = pygame.Rect(60/scale, 1,1,1)
    pygame.draw.rect(display, bg, rect)
    rect = pygame.Rect(60/scale, 60/scale,1,1)
    pygame.draw.rect(display, bg, rect)

    
    if pensize == 1:
    	rect = pygame.Rect(xl-3, 2,1,1)
    	pygame.draw.rect(display, (70,70,70), rect)

    elif pensize == 2:
    	for coords in p2:
    		rect = pygame.Rect(coords[0]+xl-4,coords[1]+1,1,1)
    		pygame.draw.rect(display,(70,70,70), rect)
    elif pensize == 3:
    	for coords in p3:
    		rect = pygame.Rect(coords[0]+xl-5,coords[1]+1,1,1)
    		pygame.draw.rect(display,(70,70,70), rect)

    for spawner in spawners:
    	simMap.setPixel(int(spawner[0]),int(spawner[1]),int(spawner[2]))
    ###	
    if showGround:	col = (40,40,40)
    else:	col = bg
    if not emptyGround:
    	rect = pygame.Rect(0, 100, 100000, 10000)
    elif emptyGround:
    	rect = pygame.Rect(0, 100-1, 100000, 10000)

    pygame.draw.rect(display, col, rect)

    if emptyGround:
    	for x in range(xl):
    		simMap.setPixel(x,99,0)
    #print(simMap.map[100])

    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    deltatime = clock.tick(FPS)


pygame.quit()