import math

### CLASSES ###

class Vec:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def normalize(self):
		length = math.sqrt(self.x**2+self.y**2)
		if length > 0:
			self.x = self.x/length
			self.y = self.y/length

	def getLength(self):
		return math.sqrt(self.x**2+self.y**2)

	def printV(self):
		print(f"{self.x} : {self.y}")

class Rect:
	def __init__(self, position, size):
		self.position = position
		self.size = size

	def getVerts(self):
		return [Vec(self.position.x, self.position.y), Vec(self.position.x, self.position.y + self.size.y), Vec(self.position.x + self.size.x, self.position.y), Vec(self.position.x + self.size.x, self.position.y + self.size.y)]

class Circle:
	def __init__(self, position, radius):
		self.position = position
		self.radius = radius

### VECTORS ###

VecZERO = Vec(0,0)

def getDirectionVec(A,B):
	return Vec(B.x-A.x ,B.y-A.y)

def getLength(A):
	return math.sqrt(A.x**2+A.y**2)

def pVec(vec):
	print(str(vec.x) + " :: " + str(vec.y))

def getDistance(A,B):
	return math.sqrt((B.x-A.x)**2 + (B.y-A.y)**2)

def addVec(v1,v2):
	return Vec(
		v1.x + v2.x,
		v1.y + v2.y)

def subVec(v1,v2):
	return Vec(
		v1.x - v2.x,
		v1.y - v2.y)

def mulVec(v1,v2):
	return Vec(
		v1.x * v2.x,
		v1.y * v2.y)

def divVec(v1,v2):
	return Vec(
		v1.x / v2.x,
		v1.y / v2.y)


### COLLISIONS ###

def rectCol(A, B):
	for p in B.getVerts():
		if p.x >= A.position.x and p.x <= A.position.x + A.size.x:
			if p.y >= A.position.y and p.y <= A.position.y + A.size.y:
				return True
	return False

def circleCol(A, B):
	if getDistance(A.position, B.position) < A.radius + B.radius:
		return True
	else:
		return False

def rectCircleCol(rA, cB):
	pass

	
### MORE ###
def rotate(origin, point, angle):
	angle = math.radians(angle)*-1
	o=origin
	p=point
	q = Vec(o.x + math.cos(angle) * (p.x - o.x) - math.sin(angle) * (p.y - o.y),  o.y + math.sin(angle) * (p.x - o.x) + math.cos(angle) * (p.y - o.y))
	return q

def clamp(val, minV, maxV):
	valu = val
	if valu < minV:
		valu = minV
	elif valu > maxV:
		valu = maxV
	return valu

def getValue(val):
	if val > 0:
		return val
	elif val < 0:
		return val *-1
	else:
		return 0

def getVertsInCircle(origin,amount,radius=100,shift=1):
	Points = []
	for Vect in range(amount):
		angle = 2*math.pi/amount
		y = math.sin((angle*Vect)+shift)*radius
		y+=origin.y
		x = math.cos((angle*Vect)+shift)*radius
		x+=origin.x
		Points.append(Vec(x,y))
	return Points

def getVertsInCircleAndVectors(origin,amount,radius=100,shift=1):
	p = getVertsInCircle(origin,amount,radius,shift)
	pointlist = {}
	for point in p:
		pointlist[point] = getDirectionVec(origin, point)
		pointlist[point].normalize()
	return pointlist

### TILEMAP ###

class Tile:
	def __init__(self, position, tileType, collision):
		self.position = position 
		self.tileType = tileType
		self.collision = collision
		self.rawData = []
		self.spawnpoint = VecZERO


class Map:
	def __init__(self, tileSize):
		self.size = VecZERO
		self.tiles = []
		self.tileSize = tileSize
		self.tileTypes = {}

	def load(self, path, tileList):
		f = open(path + '.txt','r')
		data = f.read()
		f.close()
		data = data.split('\n')
		self.size.x = len(data[0])*self.tilesize
		self.size.y = len(data)*self.tilesize
		self.rawData = []
		for row in data:
			self. rawData.append(list(row))
		x, y = 0,0
		for line in self.rawData:
			x = 0
			for tile in line:
				if not tile == "S":
					self.tiles.append(Tile(Vec(x*self.tilesize,y*self.tilesize), tile, True))
				else:
					self.spawnpoint = Vec(x*self.tilesize,y*self.tilesize)
				x += 1
			y+=1


	def getRenderingInfo(self):
		return self.tiles, self.tileSize, self.tileTypes


