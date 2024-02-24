import math

### CLASSES ###

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Vec2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def normalize(self):
		length = math.sqrt(self.x**2+self.y**2)
		self.x = self.x/length
		self.y = self.y/length

	def getLength(self):
		return math.sqrt(self.x**2+self.y**2)

class rect:
	def __init__(self, pos, size):
		self.pos = pos
		self.size = size

	def getPoints(self):
		return [Point(self.pos.x, self.pos.y), Point(self.pos.x, self.pos.y + self.size.y), Point(self.pos.x + self.size.x, self.pos.y), Point(self.pos.x + self.size.x, self.pos.y + self.size.y)]

### VECTORS ###

vecZERO = Vec2(0,0)

def getDirectionVec2(A,B):
	return Vec2(B.x-A.x ,B.y-A.y)

def getLength(A):
	return math.sqrt(A.x**2+A.y**2)

def pVec(vec):
	print(str(vec.x) + " :: " + str(vec.y))


### POINTS ###

def pPoint(poi):
	print(str(poi.x) + " :: " + str(poi.y))

def getDistance(A,B):
	return math.sqrt((B.x-A.x)**2 + (B.y-A.y)**2)

def addVec(v1,v2):
	return Vec2(
		v1.x + v2.x,
		v1.y + v2.y)

def subVec(v1,v2):
	return Vec2(
		v1.x - v2.x,
		v1.y - v2.y)

def mulVec(v1,v2):
	return Vec2(
		v1.x * v2.x,
		v1.y * v2.y)

def divVec(v1,v2):
	return Vec2(
		v1.x / v2.x,
		v1.y / v2.y)


### COLLISIONS ###

def rectCol(A, B):
	for p in B.getPoints():
		if p.x >= A.pos.x and p.x <= A.pos.x + A.size.x:
			if p.y >= A.pos.y and p.y <= A.pos.y + A.size.y:
				return True
	return False

### MORE ###

def getPointsInCircle(origin,amount,radius=100,shift=1):
	points = []
	for point in range(amount):
		angle = 2*math.pi/amount
		y = math.sin((angle*point)+shift)*radius
		y+= origin.y
		x = math.cos((angle*point)+shift)*radius
		x+=origin.x
		points.append(Point(x,y))
	return points

def getPointsInCircleAndVectors(origin,amount,radius=100,shift=1):
	p = getPointsInCircle(origin,amount,radius,shift)
	pointlist = {}
	for point in p:
		pointlist[point] = getDirectionVec2(origin, point)
		pointlist[point].normalize()
	return pointlist






### TILEMAP ###

class Tile:
	def __init__(self, position, tileType, collision):
		self.position = position 
		self.tileType = tileType
		self.collision = collision


class Map:
	def __init__(self, tilesize, tilelist):
		self.size = Vec2(0,0)
		self.tiles = []
		self.tilesize = tilesize
		self.tilelist = tilelist

	def load(self, path):
		f = open(path + '.txt','r')
		data = f.read()
		f.close()
		data = data.split('\n')
		mapW = len(data[0])*16
		mapH = len(data)* 16
		rawData = []
		for row in data:
			rawData.append(list(row))

		x, y = 0,0
		playerpos = vecZERO
		for line in rawData:
			x = 0
			for tile in line:
				if not tile == "S":
					self.tiles.append(Tile(Vec2(x*self.tilesize,y*self.tilesize), tile, True))
				else:
					playerpos = Vec2(x*self.tilesize,y*self.tilesize)
				x += 1
			y+=1
		return playerpos

	def getRenderingInfo(self):
		return self.tiles, self.tilesize, self.tilelist

