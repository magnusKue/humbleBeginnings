import pygame

from functions import *
from SETTINGS import *

class Animator:
	def __init__(self):
		self.animation = "walk"
		self.animations = {"walk":["a.png", "b.png"]} 
		self.frame = 0

	def set_Animation(self, animation):
		pass

class Entity:
	def __init__(self):
		self.position = pygame.Vector2(0,0)
		self.velocity = pygame.Vector2(0,0)
		self.speed = 10
		self.acceleration = 0.01
		self.friction = .8

		self.animator = Animator()
		self.sprite = None

		self.hitbox = pygame.Rect(0,0,16,16)


	def moveAndCollide(self, subTiles, tileManager, cam):
		testRect = self.hitbox
		testRect.x += self.velocity.x
		testRect.y += self.velocity.y

		hitList = []
		for tile in subTiles:
			position = pygame.Vector2(int(tile.position.x*tileManager.tileSize.x), int(tile.position.y*tileManager.tileSize.x))
			color = (100,100,100)
			if testRect.colliderect(pygame.Rect((position.x, position.y), (tileManager.tileSize.x, tileManager.tileSize.y))):
				hitList.append(tile)
				color = (255,0,0)
			if COLLISION_DEBUG_MAP:
				pygame.draw.rect(pygame.display.get_surface(), color, pygame.Rect(position.x, position.y, 16, 16), 2)
		
		collisionDirection = {'top':False,'bottom':False,'right':False,'left':False}
		
		pygame.draw.rect(pygame.display.get_surface(), (0,0,255), pygame.Rect(cam.worldToCam(Vector2(testRect.x, testRect.y)),(self.hitbox.width*cam.zoom, self.hitbox.height*cam.zoom) )) # debug
		if hitList:
			self.velocity = Vector2(0,0)
		else:
			self.position += self.velocity

		self.velocity *= self.friction
		if self.velocity.length() < .0001:
			self.velocity = Vector2(0,0)

	def render(self, surface, cam):
		scaledSprite = pygame.transform.scale(self.sprite, (int(self.hitbox.width*cam.zoom), int(self.hitbox.height*cam.zoom)))
		position = cam.worldToCam(self.position)
		surface.blit(scaledSprite, (position.x, position.y))
		if DEBUG_MAP:
			surface.blit(self.sprite, (self.position.x, self.position.y))

	def getInput(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.velocity.y = clamp(self.velocity.y-self.acceleration, -self.speed, self.speed)
		elif keys[pygame.K_s]:
			self.velocity.y = clamp(self.velocity.y+self.acceleration, -self.speed, self.speed)
		if keys[pygame.K_a]:
			self.velocity.x = clamp(self.velocity.x-self.acceleration, -self.speed, self.speed)
		elif keys[pygame.K_d]:
			self.velocity.x= clamp(self.velocity.x+self.acceleration, -self.speed, self.speed)

	def update(self, surface, cam, mapData, tileManager):
		self.hitbox = pygame.Rect(self.position.x, self.position.y, self.sprite.get_width(), self.sprite.get_height())
		self.getInput()
		self.moveAndCollide(mapData, tileManager, cam)
		self.render(surface, cam)

	
class Player(Entity):
	def __init__(self):
		super().__init__()
		self.speed = 1.3
		self.acceleration = 0.2
		
