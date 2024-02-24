
import math
import pygame

def roundSurface(ogsurf, roundness):
	size = ogsurf.get_size()
	mask = pygame.Surface(size, pygame.SRCALPHA)
	pygame.draw.rect(mask, (255, 255, 255), (0, 0, *size), border_radius=roundness)
	image = ogsurf.copy().convert_alpha()
	image.blit(mask, (0, 0), None, pygame.BLEND_RGBA_MIN)
	return image

class Vec2:
	def __init__(self, x = 0, y = 0):
		self.x = x;
		self.y = y

class animatedTile:
	def __init__(self):
		self.frames = []
		self.name = ""
		self.collision = 1 # index of collision groupe in project collisionType list
		self.animationSpeed = 1
		self.collisionRect = [[0,0],[1,1]] # top left and bottom right in UV coordinates
		
	def get_frame(self, time):
		index = int((time*0.05*self.animationSpeed)%(len(self.frames)))
		return self.frames[index]


class staticTile:
	def __init__(self):
		self.name = ""
		self.sprite = ""
		self.collision = 0 # index of collision groupe in project collisionType list
		self.collisionRect = [[0,0],[1,1]]

class supTile:
	def __init__(self):
		self.sprite = ""

class dynamicTile:
	def __init__(self):
		self.name = ""
		self.tiles = [] # index to subTiles -> see gamesheet (bsp: 0 = top left)
		self.collision = 1 # index of collision groupe in project collisionType list
		self.collisionRect = [[0,0],[1,1]]

class staticObject:
	def __init(self):
		self.name = ""
		self.sprite = ""
		self.collisionRect = [[0,0],[1,1]]

class animatedObject:
	def __init(self):
		self.name = ""
		self.frames = []
		self.animationSpeed = 1
		self.collisionRect = [[0,0],[1,1]]

	def get_frame(self, time):
		index = int((time*0.05*self.animationSpeed)%(len(self.frames)))
		return self.frames[index]

class Chunk:
	def __init__(self, position=Vec2(), resolution=16):
		self.resolution = resolution
		self.position = position # in chunk coordinates ( third chunk | second chunk )
		self.tiles = []

# Relative Tile position in chunk (used in get/setTile position vectors etc.)
#  (0,0) (1,0) (2,0)
#  (0,1) (1,1) (2,1)
#  (0,2) (1,2) (2,2)

	def fill(self, typeID="000000"): # fill "tiles" with empty space
		self.tiles = []
		
		for y in range(self.resolution):
			xList = []
			for x in range(self.resolution):
				xList.append(typeID) # 000000 = empty space tile id
			self.tiles.append(xList)

	def log(self):
		for row in self.tiles:
			for item in row:
				print(item + " ", end ="")
			print("\n",end="")
	
	def getTile(self, position = Vec2(0,0)):
		return self.tiles[position.y][position.x]

	def setTile(self, position = Vec2(0,0), tile = "000000"):
		self.tiles[position.y][position.x] = tile



class Layer:
	def __init__(self, name="newLayer"):
		self.content = [] # Objects, Portals, Chunks. Basically anything that exists on that layer
		self.name = name

class Area:
	def __init__(self, name):
		self.name = name
		self.layers = []
		self.editIsVisible = True
		self.editIsExpanded = True

class Project:
	def __init__(self, tileRes = 16):
		self.tileRes = tileRes
		self.areas = []
		self.tileTypes = {}
		self.objectTypes = {}
		self.collisionTypes = ["Custom", "None", "Full"]
		self.tilesurfaces = {}

class debug:
	def __init__(self):
		self.pos = (5,5)
		self.content = []
		self.font = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 22)

	def debug(self, info):
		self.content.append(str(info))

	def renderDebug(self):
		surf = pygame.display.get_surface()
		for index, item in enumerate(self.content):
			itemText = self.font.render(item, 2, (200,200,200))
			pygame.draw.rect(surf, (0,0,0), pygame.Rect((4, index*itemText.get_height()), (itemText.get_width(), itemText.get_height())))
			surf.blit(itemText, (4, index*itemText.get_height()))
		self.content = []
			


# debug

testC = Chunk(Vec2(0,0), 4)
testC.fill()
testC.setTile(Vec2(1,2), "00003H")
testC.log()
print(testC.getTile(Vec2(0,0)))