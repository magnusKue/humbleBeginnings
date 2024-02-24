import pygame, random, math
pygame.init() 
scr = pygame.display.set_mode((1000,1000))  
pygame.display.set_caption('mapper')
done = False
t = 0
val = 0
def clamp(val, minv, maxv):
	if val <= minv:
		val = minv
	if val >= maxv:
		val = maxv	

	return val
length = 8
while not done:
	scr.fill((100,100,100))

	mx, my = pygame.mouse.get_pos()

	for h in range(length):
		alpha = 2*math.pi/length
		y = math.sin(alpha*h)*100
		y+=500
		x = math.cos(alpha*h)*100
		x+=500
		pygame.draw.rect(scr,(40,40,180),  pygame.Rect(x-10,y-10,20,20))


	#for h in range(length):

	pygame.draw.rect(scr,(180,180,180),  pygame.Rect(490,490,20,20))

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				print("up"+str(1))
				length+=1
			elif event.key == pygame.K_s:
				print("down"+str(1))
				length-=1
	pygame.display.flip()
	t+=1



