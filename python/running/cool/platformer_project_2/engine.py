import pygame

class Particle:
	def __init__(self, position, lt, scroll, color):
		self.color = color
		self.pos = position
		self.lifetime = lt
		self.alive = True
		self.scroll = scroll

	def Update(self):
		self.lifetime -= 0.15
		if self.lifetime <= 0:
			self.alive = False

class Vector2:
	def __init__(self, values):
		self.x = values[0]
		self.y = values[1]

	def Zero(self):
		self.x,self.y = 0,0

if __name__ == "__main__":
	print('Wrong script executed')
