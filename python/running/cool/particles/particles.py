import pygame, random,math
pygame.init() 
mapsize = [10,10]
scr = pygame.display.set_mode((1000,1000))  
pygame.display.set_caption('mapper')
done = False
rects=[]
global mode
mode = False

def clamp(val, minv, maxv):
	if val <= minv:
		val = minv
	if val >= maxv:
		val = maxv

	return val

class Block:
	def __init__(self, x, y, speed):
		self.x = x
		self.y = y
		self.sp = speed
		self.velx = 0
		self.vely = 0

	def update(self, x, y):
		dirx = x - self.x
		diry = y - self.y

		self.velx += dirx*self.sp      #.0001
		self.vely += diry*self.sp

		if self.velx < 0:
			self.velx +=.01
		else:
			self.velx -=.01

		self.x += self.velx
		self.y += self.vely

	def render(self,shiftx, shifty):
		dist = int(clamp(math.sqrt((500-self.x)**2+(500-self.y)**2)/2, 0, 255))
		if mode == True:
			pygame.draw.rect(scr,(random.randint(0,dist),random.randint(0,dist),random.randint(0,dist)),  pygame.Rect(self.x-10-(shiftx*.02),self.y-10-(shifty*.02),20,20))
		else: 
			pygame.draw.rect(scr,(dist,0,0),  pygame.Rect(self.x-10-(shiftx*.2),self.y-10-(shifty*.2),20,20))

def rand():
	x = random.randint(1,100)
	return float(x/10000)


for x in range(10000):
	rects.append(Block(random.randint(0,1000),random.randint(0,1000),rand()))

while not done:
	scr.fill((100,100,100))

	mx, my = pygame.mouse.get_pos()

	for item in rects:
		item.update(500, 500)
		item.render(mx-500, my-500)
	
	print(rand())

	if False:
		if random.randint(0,100)==2 and len(rects)<10000:
			for x in range(1, len(rects)+2):
				rects.append(Block(random.randint(0,1000),random.randint(0,1000),rand()))
	pygame.draw.rect(scr,(244,244,244),pygame.Rect(500-10-((mx-500)*.2),      500-10-((my-500)*.2),20,20))
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True
	pygame.display.flip()



