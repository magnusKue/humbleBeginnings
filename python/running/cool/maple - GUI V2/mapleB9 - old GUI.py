from math import *
from tkinter import colorchooser, filedialog
from numpy import tile
import pygame, sys, random, time
from tkinter import *
from pygame.locals import *
from tileProjClasses import *

# Pygame
clock = pygame.time.Clock()
success, failures = pygame.init()
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEWHEEL, MOUSEBUTTONUP, MOUSEBUTTONDOWN])
print(f"successes: {success}\nfailures: {failures}")

pygame.display.set_caption('maple')
winSize = 5/5
monitor_size = [int(pygame.display.Info().current_w*winSize), int(pygame.display.Info().current_h*winSize)]
s=1
window = pygame.display.set_mode((int(monitor_size[0]/s), int(monitor_size[1]/s)), pygame.NOFRAME)

# pragma Variables
FPS = 60;
running = True
lastFramepressed = False
project = None # loaded project
editingLayer = None
mouseWheel = 0
lastMouseWheelState = 0
typedText = ""
lastFramePressed = False
rlastFramePressed = False
roundness = 10
time = 0

#debugger = debug()
#> scene
selectedArea = 0
selectedLayer = 0 # -1 = select area
editname = False
sceneScroll = 0
lasty = 0
editedLayer = -1 # -1 = Area is edited not layer else layer id
editedArea = -1 # -1 = nothing is edited else area id
editedWindow = 0 # 0=sceneS 1=tilesS 2=previewS

#> Preview
bg = (133, 237, 230)

#> Tiles
selectedObjectKind = 1 # 0 = Obj, 1 = Tiles, 2 = Entities
editedTiletype = "-1" # int
editedObjecttype = "001"
filename = ""
tileScroll = 0
objectScroll = 0
tileSortMode = 0 # 0=age 1=name
editedSortingMode = 0 # 0 = obj, 1 = Tile
mouseEdgeAttached = 0 # 0=TopLeft 1=BottomRight
boxheight = 40 #tilesS.get_height()*1/17

#> options
optionsRequired = False
optionsKind = 1 # 0 = addObject, 1 = addTile

#
lockSurfaceFalse = pygame.transform.scale(pygame.image.load("gui/pixelLockFalse.png").convert(), (16,16))
lockSurfaceTrue = pygame.transform.scale(pygame.image.load("gui/pixelLockTrue.png").convert(), (16,16))
altColorSurfaceTrue = pygame.transform.scale(pygame.image.load("gui/altColTrue.png").convert(), (16,16))
altColorSurfaceFalse = pygame.transform.scale(pygame.image.load("gui/altColFalse.png").convert(), (16,16))

# Windows
tilesSceneRatio = -100 # shift gap upwards
menueS = pygame.Surface((int(monitor_size[0]*(4/5)), int(monitor_size[1]*.5/10)))
previewS = pygame.Surface((int(monitor_size[0]*(4/5)), int(monitor_size[1]*9.5/10)))
sceneS = pygame.Surface((int(monitor_size[0]*(1/5)), int(monitor_size[1]*(2/5))-tilesSceneRatio))
tilesS = pygame.Surface((int(monitor_size[0]*(1/5)), int(monitor_size[1]*(3/5))+tilesSceneRatio))
tileDispS = pygame.Surface( (int(monitor_size[0]*(1/5)), int(monitor_size[1]*(3/5))+tilesSceneRatio-boxheight), pygame.SRCALPHA, 32) # pragma tilefix
optionsS = pygame.Surface((int(monitor_size[0]*(1/5)), int(monitor_size[1]*(2/5))))
ppS = pygame.Surface((int(monitor_size[0]/s), int(monitor_size[1]/s)))

# Test project
project = Project()
project.tileRes = 16
project.areas.append(Area("Dirtmouth"))
project.areas[0].layers.append(Layer("city"))
project.areas[0].layers.append(Layer("well"))
project.areas.append(Area("Cristal Peak"))
project.areas[1].layers.append(Layer("core room"))
project.areas[1].layers.append(Layer("mine"))
project.areas[1].editIsVisible = True
project.areas[1].editIsExpanded = False
project.areas.append(Area("Godhome"))
project.areas[2].layers.append(Layer("bench"))
project.areas[2].layers.append(Layer("hall of gods"))
project.areas.append(Area("City of tears"))
project.areas[3].layers.append(Layer("village"))
project.areas[3].layers.append(Layer("fountain"))
project.areas.append(Area("Greenpath"))
project.areas[4].layers.append(Layer("Lake of un"))

add1 = staticTile()
add1.name = "wall"
add1.sprite = "wall.png"
project.tileTypes["h001"] = add1
project.tilesurfaces["h001"] = pygame.image.load("tiles/"+add1.sprite).convert_alpha()

add1 = staticTile()
add1.name = "chest"
add1.sprite = "chest.png"
project.tileTypes["h002"] = add1
project.tilesurfaces["h002"] = pygame.image.load("tiles/"+add1.sprite).convert_alpha()

add1 = staticTile()
add1.name = "bomb"
add1.sprite = "bomb.png"
project.tileTypes["h003"] = add1
project.tilesurfaces["h003"] = pygame.image.load("tiles/"+add1.sprite).convert_alpha()

add1 = staticTile()
add1.name = "wall ladder"
add1.sprite = "wallLadder.png"
project.tileTypes["h004"] = add1
project.tilesurfaces["h004"] = pygame.image.load("tiles/"+add1.sprite).convert_alpha()

#####	adds	#########
tileAdd = staticTile()
addTileAnimated = False
addEdit = 0 # 0 = nix, 1 = name
editingMode = 0 # 0 =add 1=edit
editedTileId = ""
f2p = False
lockToPixels = True
altColor = False
##############
add1 = staticObject()
add1.name = "tree"
add1.sprite = "tree.png"
project.objectTypes["001"] = add1

project.areas[0].layers[0].content.append(Chunk(Vec2(0,0),16))	
project.areas[0].layers[0].content[0].fill()

for x in ["Fluid", "Ice"]:
	project.collisionTypes.append(x)
print(project.collisionTypes)

font32 = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 32)
font32Fat = pygame.font.Font("fonts\\NotoSansJP-Medium.otf", 32)
font28 = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 28)
font24 = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 24)
font22 = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 22)
font20 = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 20)
font16 = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 16)

ppS.set_alpha(0)

ogsurf = pygame.image.load("tiles/grass.png").convert_alpha()

### colors ####################### 
hoverGray = (70, 75, 90)

lightGray = (141, 153, 174) #(141, 153, 174)
lighterGray = lightGray	#(171, 183, 204)
darkerGray = (121, 133, 154)
windowBg = (48, 51, 56)
windowBgDark = (28, 31, 36)
selectedColor = (151, 163, 184)
unselectedColor = (100, 113, 134)
customCollisionColor = (29, 155, 196)
altCollisionColor = (196, 29, 68)
###### functions ##################

def changeBgcolor():
	bg = colorchooser.askcolor()

def updateScene(sceneScroll, editedWindow, editedLayer, editedArea, selectedArea, selectedLayer, typedText, mouseWheel, lastMouseWheelState): 
	sceneS.fill(windowBg)
	# clamp scroll
	if mouseWheel == lastMouseWheelState:
		mouseWheel = 0
	lastMouseWheelState = mouseWheel
	
	#scorll if mouse hovers over area
	if mousePos[0] > int(monitor_size[0]*4/5) and mousePos[1] > 0 and mousePos[1] < sceneS.get_height():
		sceneScroll += mouseWheel * 15
		if sceneScroll >= 0: sceneScroll = 0

	#start drawing
	y = 50 + sceneScroll
	for x in range(0, len(project.areas)):
		#print(editedWindow, " : ", editedArea, " : ", editedLayer, " ", editname)
		# collide and expand
		areaTextWidth = font28.render(project.areas[x].name, 0, lightGray).get_width()
		areaTextHeight = font28.render(project.areas[x].name, 0, lightGray).get_height()
		expandTextWidth = font28.render(" ^", 0, lightGray).get_width()
		expandTextHeight = font28.render(" ^", 0, lightGray).get_height()
		spacing = 0
		if project.areas[x].editIsExpanded and selectedArea == x and not selectedLayer == -1 and project.areas[x].layers != []:
			spacing = 13
		ehitbox = Rect((10 + areaTextWidth + spacing,y), (int(expandTextWidth*2), expandTextHeight))
		ahitbox = Rect((10 + spacing, y), (areaTextWidth, areaTextHeight))
		

		if len(project.areas[x].layers) > 0 and not optionsRequired and pressed and ehitbox.collidepoint( ( int(mousePos[0]-monitor_size[0]*4/5) , mousePos[1])):
			if mousePos[1] > 49 and mousePos[1] < sceneS.get_height():
				project.areas[x].editIsExpanded = not project.areas[x].editIsExpanded
				typedText = typedText.rstrip()
				if editedArea == x and editedWindow == 0:
					editedWindow = -1
					editedAreaName = -1
					editedLayerName = -1
		if not optionsRequired and pressed and ahitbox.collidepoint( ( int(mousePos[0]-monitor_size[0]*4/5) , mousePos[1])):
			if mousePos[1] > 49 and mousePos[1] < sceneS.get_height():
				selectedArea = x
				selectedLayer = -1
			
			
		if editname and ahitbox.collidepoint( ( int(mousePos[0]-monitor_size[0]*4/5) , mousePos[1])):
			if mousePos[1] > 49 and mousePos[1] < sceneS.get_height():
				editedWindow = 0
				editedArea = x
				editedLayer = -1
				typedText = project.areas[x].name

		# collide and change visibility or add layer
		vTextWidth = font28.render("○", 5, (0,0,0)).get_width()
		vTextHeight = font28.render("○", 0, lightGray).get_height()
		vhitbox = Rect((monitor_size[0]*1/5-(vTextWidth+5), y+9), (vTextWidth, int(vTextHeight*2/3)))
		addLayerHitbox = Rect((monitor_size[0]*1/5-(vTextWidth+5)-20, y+9), (vTextWidth, int(vTextHeight*2/3)))

		if not optionsRequired and pressed and vhitbox.collidepoint( ( int(mousePos[0]-monitor_size[0]*4/5) , mousePos[1])):
			if mousePos[1] > 49 and mousePos[1] < sceneS.get_height():
				project.areas[x].editIsVisible = not project.areas[x].editIsVisible

		# add layer
		if not optionsRequired and pressed and addLayerHitbox.collidepoint( ( int(mousePos[0]-monitor_size[0]*4/5) , mousePos[1])):
			if mousePos[1] > 49 and mousePos[1] < sceneS.get_height():
				project.areas[x].editIsExpanded = True
				editedArea = x 
				selectedArea = x
				editedWindow = 0
				editedLayer = len(project.areas[x].layers)
				selectedLayer = editedLayer
				typedText = ""
				add = Layer("new Layer")
				project.areas[x].layers.append(add)


		# Area name editing
		if editedWindow == 0 and editedArea == x and editedLayer == -1:
			project.areas[x].name = typedText
			editingAreaTextHeight = font24.render(str(project.areas[x].name), 20, windowBg).get_height()
			pygame.draw.rect(sceneS, (0, 0, 0), Rect((0,y+7), (sceneS.get_width(), editingAreaTextHeight)))
		else:
			project.areas[x].name = project.areas[x].name.rstrip()

		# render area name + dropdown
		slowtime = int(sin(time*0.2)*2)
		if editedWindow == 0 and slowtime == 1 and editedArea == x and editedLayer == -1:
			taddition = "|"
		else:
			taddition = " "

		if selectedArea == x and selectedLayer == -1:
			col = lightGray
			pygame.draw.rect(sceneS, windowBgDark, Rect((0,y+7), (sceneS.get_width(), font28.render(project.areas[x].name, 20, (0,0,0)).get_height()-9))) 
		else: col = darkerGray

		if project.areas[x].editIsExpanded:
			if project.areas[x].layers != []:
				sceneS.blit(font28.render(project.areas[x].name + taddition + " ^", 20, col), (10, y))
			else:
				sceneS.blit(font28.render(project.areas[x].name + taddition + "  ", 20, col), (10, y))
		else:   
			if selectedArea == x and not selectedLayer == -1 and len(project.areas[x].layers) > 0:
				selectedTextHeight = font28.render(str(project.areas[x].name), 20, (0, 0, 0)).get_height()
				pygame.draw.rect(sceneS, windowBgDark, Rect((10,y+7), (8, selectedTextHeight-9)))
				if project.areas[x].layers != []:
					sceneS.blit(font28.render(project.areas[x].name + taddition + " v", 20, col), (23, y))
				else:
					sceneS.blit(font28.render(project.areas[x].name + taddition + "  ", 20, col), (23, y))
			else:
				if project.areas[x].layers != []:
					sceneS.blit(font28.render(project.areas[x].name + taddition + " v", 20, col), (10, y))
				else:
					sceneS.blit(font28.render(project.areas[x].name + taddition + "  ", 20, col), (10, y))


		# render visibility
		if project.areas[x].editIsVisible:    
			visibility = "●"            
		else:   
			visibility = "○"
		sceneS.blit(font16.render(visibility, 20, col), (monitor_size[0]*1/5-(vTextWidth), y+11))

		#if project.areas[x].editIsExpanded or not len(project.areas[x].layers) > 0:
		sceneS.blit(font20.render("+", 20, col), (monitor_size[0]*1/5-(vTextWidth)-20, y+8))
		y += 30



		# render layers #################################################
		for l in range(0, len(project.areas[x].layers)):
				
			# Layer name editing
			taddition = " "
			if editedWindow == 0 and editedArea == x and editedLayer == l:
				slowtime = int(sin(time*0.2)*2)
				if slowtime == 1:
					taddition = "|"
				else:
					taddition = " "
				project.areas[x].layers[l].name = typedText
				editingLayerTextHeight = font24.render(str(project.areas[x].layers[l].name), 20, lightGray).get_height()
				pygame.draw.rect(sceneS, (0,0,0), Rect((0,y+6), (sceneS.get_width(), editingLayerTextHeight-6)))
			else:
				project.areas[x].layers[l].name = project.areas[x].layers[l].name.rstrip()

			# layer rendering
			if project.areas[x].editIsExpanded:
				if x == selectedArea and l == selectedLayer:
					selectedTextHeight = font24.render(str(project.areas[x].layers[l].name), 20, lightGray).get_height()
					pygame.draw.rect(sceneS, windowBgDark, Rect((0,y+7), (sceneS.get_width(), selectedTextHeight-9)))
					sceneS.blit(font24.render("└ " + str(project.areas[x].layers[l].name) + taddition, 20, lightGray), (20, y))
				else:
					sceneS.blit(font24.render("└ " + str(project.areas[x].layers[l].name) + taddition, 20, darkerGray), (20, y)) 

				# collision
				lTextWidth = font24.render("└ " + str(project.areas[x].layers[l].name), 5, darkerGray).get_width()
				lTextHeight = font24.render("└ " + str(project.areas[x].layers[l].name), 0, darkerGray).get_height()
				lhitbox = Rect((monitor_size[0]*4/5, y+7), (sceneS.get_width(), int(lTextHeight)))
				pygame.draw.rect(sceneS, (255,0,0), lhitbox)

				if not optionsRequired and pressed and lhitbox.collidepoint( (mousePos[0] , mousePos[1])) and mousePos[1] > 49 and mousePos[1] < sceneS.get_height():
					selectedLayer = l
					selectedArea = x
				
				if editname and lhitbox.collidepoint( (mousePos[0] , mousePos[1])):
					typedText = project.areas[x].layers[l].name
					editedWindow = 0
					editedArea = x
					editedLayer = l


				y+=26
		y+=10

		lasty = y

	if y > int(monitor_size[1]*2/5):
		pass


	# add area collision
	addhitbox = Rect((monitor_size[0]-32, 5), (40,40))
	if not optionsRequired and pressed and addhitbox.collidepoint( (mousePos[0] , mousePos[1])):
		addButtonCol = unselectedColor
		# add area to scene
		ol=len(project.areas)
		project.areas.append(Area("new Area"))
		editedWindow = 0
		editedArea = ol
		editedLayer = -1
		typedText = ""
	else: addButtonCol = lighterGray

	# render sScene headline
	pygame.draw.rect(sceneS,windowBg, Rect((0,0), (int(monitor_size[0]*1/5), 49)))
	sceneS.blit(font32Fat.render("Areas: ", 20, lighterGray), (10, 5))
	sceneS.blit(font32Fat.render("+", 20, addButtonCol), (sceneS.get_width()-32, 5))

	

	return sceneScroll, editedWindow, editedLayer, editedArea, selectedArea, selectedLayer, typedText, mouseWheel, lastMouseWheelState

def updateTiles(selectedObjectKind, editedTiletype, editedObjecttype, optionsRequired, optionsKind, editingMode, editedTileId, tileAdd, addTileAnimated, tileScroll):

	### Top bar ################################# pragma tilefix
	invBoxheight = tilesS.get_height() -40 # #tilesS.get_height()*16/17
	translatedMousePos = (int(mousePos[0]-(monitor_size[0]*4/5)), int(mousePos[1]-(monitor_size[1]*2/5-tilesSceneRatio)))
	# collide obj / tiles
	objBox = Rect((10,11), (int(tilesS.get_width()*1/5), int(boxheight-10)))
	if not optionsRequired and objBox.collidepoint(translatedMousePos) and pressed:
		selectedObjectKind = 0

	tilesBox = Rect((int(tilesS.get_width()*1/5+21),11), (int(tilesS.get_width()*1/5), int(boxheight-10)))
	if not optionsRequired and tilesBox.collidepoint(translatedMousePos) and pressed:
		selectedObjectKind = 1

	enititesBox = Rect((int(tilesS.get_width()*2/5+11+19),9), (int(tilesS.get_width()*1/5+4), int(boxheight-10+4)))
	if not optionsRequired and enititesBox.collidepoint(translatedMousePos) and pressed:
		selectedObjectKind = 2
	pygame.draw.rect(tilesS, windowBgDark, Rect((0,0), (tilesS.get_width(), 2)) )	# trennlinie
	pygame.draw.rect(tilesS, windowBgDark, Rect( (0,int(boxheight-2)), (tilesS.get_width(), int(invBoxheight+11)) ) )


	pygame.draw.rect(tilesS, windowBgDark, Rect((8,9), (int(tilesS.get_width()*1/5+4), int(boxheight-10+4))),border_top_left_radius=roundness+2, border_top_right_radius=roundness+2)
	if selectedObjectKind == 0:
		pygame.draw.rect(tilesS, windowBg, objBox,border_top_left_radius=roundness, border_top_right_radius=roundness)
	else:
		pygame.draw.rect(tilesS, windowBgDark, objBox, border_top_left_radius=roundness, border_top_right_radius=roundness)

	objFont = font20.render("Object", 20, lightGray)
	tilesS.blit(objFont, (objBox.x+int((objBox.width-objFont.get_width())/2), objBox.y))
	


	pygame.draw.rect(tilesS, windowBgDark, Rect((int(tilesS.get_width()*1/5+19),9), (int(tilesS.get_width()*1/5+4), int(boxheight-10+4))),border_top_left_radius=roundness+2, border_top_right_radius=roundness+2)
	if selectedObjectKind == 1:
		pygame.draw.rect(tilesS, windowBg, tilesBox,border_top_left_radius=roundness, border_top_right_radius=roundness)
	else: 
		pygame.draw.rect(tilesS, windowBgDark, tilesBox,border_top_left_radius=roundness, border_top_right_radius=roundness)
	tileFont = font20.render("Tile", 20, lightGray)
	tilesS.blit(tileFont, (tilesBox.x+int((tilesBox.width-tileFont.get_width())/2), tilesBox.y))



	pygame.draw.rect(tilesS, windowBgDark, Rect((int(tilesS.get_width()*2/5+11+19),9), (int(tilesS.get_width()*1/5+4), int(boxheight-10+4))),border_top_left_radius=roundness+2, border_top_right_radius=roundness+2)
	if selectedObjectKind == 2:
		pygame.draw.rect(tilesS, windowBg, Rect((int(tilesS.get_width()*2/5+11+19+2),11), (int(tilesS.get_width()*1/5), int(boxheight-10+4))),border_top_left_radius=roundness, border_top_right_radius=roundness)
	else: 
		pygame.draw.rect(tilesS, windowBgDark, Rect((int(tilesS.get_width()*2/5+11+19+2),11), (int(tilesS.get_width()*1/5), int(boxheight-10+4))) ,border_top_left_radius=roundness, border_top_right_radius=roundness)
	tileFont = font20.render("Entity", 20, lightGray)
	tilesS.blit(tileFont, (enititesBox.x+int((enititesBox.width-tileFont.get_width())/2), enititesBox.y))


	# render add tile button + collision
	txt = font24.render("+", 20, lightGray)
	width = txt.get_width()
	height = txt.get_height()
	addTileHitbox = Rect((int( tilesS.get_width() - 5 - width ), 0), (width,height))
	col = lightGray
	if not optionsRequired and pressed and addTileHitbox.collidepoint(translatedMousePos):
		col = hoverGray
		if selectedObjectKind == 1:
			optionsRequired = True
			optionsKind = 3
		elif selectedObjectKind == 0:
			optionsRequired = True
			optionsKind = 0

	txt = font24.render("+", 20, col)
	tilesS.blit(txt, (int( tilesS.get_width() - 5 - width ), 0))

	pygame.draw.rect(tilesS, windowBg, Rect((0,int(boxheight)), (tilesS.get_width(), int(invBoxheight+11)) ) )

	###### Render Tiles ######################
	if selectedObjectKind == 1:
		if mousePos[0] > monitor_size[0] * 4/5 and mousePos[1] > sceneS.get_height():
			tileScroll += mouseWheel * 15
		xgap = 10
		ygap = 40
		yshift = 15 # shift tiles down
		IconsPerLine = 6
		iconSize = int((tileDispS.get_width()-xgap*(IconsPerLine+1))/IconsPerLine)
		y = 0
		x = 0
		tileScroll = min(-boxheight, tileScroll)
		for Id in project.tileTypes:
			if f2p and  editedTiletype == Id:
				optionsKind = 1
				optionsRequired = True
				editingMode=1
				editedTileId = Id
				tileAdd = project.tileTypes[Id]
				addTileAnimated = type(tileAdd) == type(animatedTile())
				
			### Collision ##################
			tileIconHitbox = Rect((xgap + x * (iconSize+xgap),  ygap + y * (iconSize+ygap) + yshift + tileScroll + 10+boxheight), (iconSize, iconSize))
			if mousePos[1] > sceneS.get_height() + boxheight and not optionsRequired and tileIconHitbox.collidepoint( mousePos[0] - previewS.get_width(), mousePos[1] - sceneS.get_height()) and mousePos[1] > sceneS.get_height(): 
				if pressed:
					editedTiletype = Id

			


		### Render Tile Icons ##########
			
			
			
			if not isinstance(project.tilesurfaces[Id], list):
				try:
					icon = project.tilesurfaces[Id]
				except:
					icon = pygame.image.load("gui/notFound.png").convert_alpha()
			else:
				frame = int((time*0.05*project.tileTypes[Id].animationSpeed)%(len(project.tileTypes[Id].frames)))
				print("frame"+str(frame))
				icon = project.tilesurfaces[Id][frame]
				#except:
				#	icon = pygame.image.load("gui/notFound.png").convert_alpha()

			#debugger.debug(str(Id)+" : "+str(project.tileTypes[Id].name) )
			if editedTiletype == Id:
				pygame.draw.rect(tileDispS, selectedColor, Rect((xgap + x * (iconSize+xgap),  ygap + y * (iconSize+ygap) + tileScroll + yshift + 10), (iconSize, iconSize)), 0, roundness+2)
				icon = pygame.transform.scale(icon, (iconSize-6, iconSize-6))
				icon = roundSurface(icon, roundness)
				tileDispS.blit(icon, (3 + xgap + x * (iconSize+xgap), 3 + ygap + yshift + tileScroll + y * (iconSize+ygap)  + 10))
				col = selectedColor
			else:
				icon = pygame.transform.scale(icon, (iconSize, iconSize))
				icon = roundSurface(icon, roundness)
				tileDispS.blit(icon, (xgap + x * (iconSize+xgap),  ygap + yshift + tileScroll + y * (iconSize+ygap) + 10 - 5))
				col = unselectedColor

			nameTxt = project.tileTypes[Id].name
			name = font20.render(nameTxt, 2, col)
			cut = 8 # //NOTE: EXPENSIVE, USE WITH CAUTION!!!
			while name.get_width() > iconSize+4:
				cut -= 1
				nameTxt = project.tileTypes[Id].name[:cut]+".."
				name = font20.render(nameTxt, 2, col)
			tileDispS.blit(name, (xgap + x * (iconSize+xgap) + ((iconSize-name.get_width())/2),  ygap + y * (iconSize+ygap) + tileScroll + yshift +7 + iconSize))
			if x <= IconsPerLine-2:
				x += 1
			else:
				x = 0
				y += 1
		pygame.draw.rect(tileDispS, windowBg, Rect((0,0), (tileDispS.get_width(), 10)))
	###### Render Objects ######################
	elif selectedObjectKind == 0:
		xgap = 10
		IconsPerLine = 4
		iconSize = int((tilesS.get_width()-xgap*(IconsPerLine+1))/IconsPerLine)
		x = 0
		y = 0
		for Id in project.objectTypes:
			### Collision ##################
			tileIconHitbox = Rect((xgap + x * (iconSize+xgap),  xgap + y * (iconSize+xgap) + boxheight + 10), (iconSize, iconSize))
			if  not optionsRequired and tileIconHitbox.collidepoint( mousePos[0] - previewS.get_width(), mousePos[1] - sceneS.get_height()) and pressed:
				editedObjecttype = Id

		### Render Object Icons ##########
			#try:
			orgIcon = pygame.image.load("objects/"+project.objectTypes[Id].sprite).convert_alpha()
			if orgIcon.get_width() > orgIcon.get_height():
				size = orgIcon.get_width()
			else: size = orgIcon.get_height()
			icon = pygame.Surface((size, size))
			icon.fill((117,109,109))  
			icon.blit(orgIcon, (int((size-orgIcon.get_width())/2),0))
			#except:
				#print("didnt find tile icon of ID: " + str(Id))
				#icon = pygame.image.load("gui/notFound.png").convert_alpha()
			if editedObjecttype == Id:
				pygame.draw.rect(tilesS, (170,170,200), Rect((xgap + x * (iconSize+xgap),  xgap + y * (iconSize+xgap) + boxheight + 10), (iconSize, iconSize)) )  
				icon = pygame.transform.scale(icon, (iconSize-6, iconSize-6))
				tilesS.blit(icon, (3 + xgap + x * (iconSize+xgap), 3 + xgap + y * (iconSize+xgap) + boxheight + 10))
			else:
				icon = pygame.transform.scale(icon, (iconSize, iconSize))
				tilesS.blit(icon, (xgap + x * (iconSize+xgap),  xgap + y * (iconSize+xgap) + boxheight + 10))

			if x <= IconsPerLine-2:
				x += 1
			else:
				x = 0
				y += 1



		
	return selectedObjectKind, editedTiletype, editedObjecttype, optionsRequired, optionsKind, editingMode, editedTileId, tileAdd, addTileAnimated, tileScroll

def updatePreview():
	#selectedArea 
	# selectedLayer
	pass #showAllLayers
	#for chunk in project.areas[selectedArea]
	
while running:
	window.fill(windowBg)
	
	tileDispS = pygame.Surface((int(monitor_size[0]*(1/5)), int(monitor_size[1]*(3/5))+tilesSceneRatio), pygame.SRCALPHA, 32)
	tilesS = pygame.Surface((int(monitor_size[0]*(1/5)), int(monitor_size[1]*(3/5))+tilesSceneRatio))
	sceneS = pygame.Surface((int(monitor_size[0]*(1/5)), int(monitor_size[1]*(2/5))-tilesSceneRatio))



	#debugger.debug(int(clock.get_fps()))
	#debugger.debug(len(project.tilesurfaces))
	# check if mouse is pressed 
	mousePos = pygame.mouse.get_pos()
	mouseState = pygame.mouse.get_pressed()[0]
	if mouseState and mouseState != lastFramePressed:
		pressed = True
	else:
		pressed = False
	
	lastFramePressed = mouseState

	rmouseState = pygame.mouse.get_pressed()[2]
	if rmouseState and rmouseState != rlastFramePressed:
		rpressed = True
	else:
		rpressed = False
	
	rlastFramePressed = rmouseState

	# main loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:				
			if event.key == K_ESCAPE:
				if optionsRequired:
					optionsRequired = False
					addEdit = 0
				else:
					running = False
			elif event.key == K_DELETE:
				sceneHitbox = Rect((int(monitor_size[0]*4/5), 0), (sceneS.get_width(), int(monitor_size[1]*2/5)-tilesSceneRatio))
				if sceneHitbox.collidepoint(mousePos[0], mousePos[1]):
					if selectedLayer != -1:
						if len(project.areas[selectedArea].layers) > 0:
							try:
								project.areas[selectedArea].layers.pop(selectedLayer)
							except:
								pass
					else:
						try:
							project.areas.pop(selectedArea)
							selectedArea = max(0,selectedArea-1)
						except:
							pass
				tilesHitbox = Rect((int(monitor_size[0]*4/5), int(monitor_size[1]*2/5)-tilesSceneRatio), (sceneS.get_width(), int(monitor_size[1]*3/5)+tilesSceneRatio))
				if tilesHitbox.collidepoint(mousePos[0], mousePos[1]):
					if selectedObjectKind == 1: # tiles
						try:
							project.tileTypes.pop(editedTiletype)
						except:
							pass
			elif event.key == K_F11:
				pygame.display.toggle_fullscreen()
			elif event.key == pygame.K_BACKSPACE:
				typedText = typedText[:-1]
			elif event.key == K_UP:
				tilesSceneRatio -= 30
			elif event.key == K_DOWN:
				tilesSceneRatio += 30
			elif event.key == pygame.K_RETURN:
				addEdit = 0
				typedText = typedText.rstrip()
				editedWindow = -1
				editedAreaName = -1
				editedLayerName = -1
			elif event.key == K_F2:
				sceneHitbox = Rect((int(monitor_size[0]*4/5), 0), (sceneS.get_width(), int(monitor_size[1]*2/5)-tilesSceneRatio))
				if sceneHitbox.collidepoint(mousePos[0], mousePos[1]):
					editname = True
				tilesHitbox = Rect((int(monitor_size[0]*4/5), int(monitor_size[1]*2/5)-tilesSceneRatio), (sceneS.get_width(), int(monitor_size[1]*3/5)+tilesSceneRatio))
				if tilesHitbox.collidepoint(mousePos[0], mousePos[1]):
					f2p = True
			else:
				print("none")
				editname = False
				typedText += event.unicode
		if event.type == MOUSEWHEEL:
			mouseWheel = event.y
		if event.type == MOUSEBUTTONUP:
			if event.button == BUTTON_LEFT:
				print("button released")
				
 	# edit

###### MENUE WINDOW ###################################################################################
	menueS.fill(windowBg)
	editB = Rect((2,2), (int(menueS.get_width()*1/9), menueS.get_height()-4))
	pygame.draw.rect(menueS, (150,150,150), editB)  
	if not optionsRequired and pressed:
		if editB.collidepoint((mousePos[0], mousePos[1])):
			print("pressed")
			root = Tk()
			btn=Button(root, text="Change Viewport color", command=changeBgcolor)
			btn.place(x=0, y=0)
			root.title('Edit')
			root.mainloop()
###### PREVIEW WINDOW #################################################################################
	previewS.fill(bg)
###### Tiles WINDOW ###################################################################################
	tilesS.fill(windowBg)
	selectedObjectKind, editedTiletype, editedObjecttype, optionsRequired, optionsKind, editingMode, editedTileId, tileAdd, addTileAnimated, tileScroll = updateTiles(selectedObjectKind, editedTiletype, editedObjecttype, optionsRequired, optionsKind, editingMode, editedTileId, tileAdd, addTileAnimated, tileScroll)
###### SCENE WINDOW ###################################################################################
	sceneScroll, editedWindow, editedLayer, editedArea, selectedArea, selectedLayer, typedText, mouseWheel, lastMouseWheelState = updateScene(sceneScroll, editedWindow, editedLayer, editedArea, selectedArea, selectedLayer, typedText, mouseWheel, lastMouseWheelState)
###### PREVIEW WINDOW #################################################################################
	updatePreview()
#######################################################################################################
	# PP
	ppS.fill((0,0,0))
	if optionsRequired:
		ppS.set_alpha(150)
	else:
		ppS.set_alpha(0)
	
###### options WINDOW ###################################################################################
	#print(optionsRequired)
	if optionsRequired:
		if optionsKind == 1:
			height = 300

			if tileAdd.collision == 0:
				height += 120
			if addTileAnimated:
				height += 35
			optionsS = pygame.Surface((int(monitor_size[0]*(1/5)), height))
			optionsS.fill(windowBg)
			y = 5
			y += 45
			pygame.draw.rect(optionsS, windowBgDark, Rect((4,4), (optionsS.get_width()-8, y-8)), 0, roundness)  
			if editingMode==0:
				header = "Add Tile"
			elif editingMode == 1:
				header = "Edit Tile"
			optionsS.blit(font28.render(header, 20, lightGray), (20, 5))
			y += 10
			txt = font22.render("select Sprite: ", 20, lightGray)
			optionsS.blit(txt, (10, y))
			spriteButton = pygame.Surface((130, txt.get_height()))
			spriteButton.fill((24, 25, 28))  

			if not addTileAnimated:
				spriteButton.blit(font20.render(str(tileAdd.sprite.split("/")[-1]), 20, lightGray), (5, 0))
				try: 
					optionsS.blit(roundSurface(pygame.transform.scale(pygame.image.load("tiles/"+str(tileAdd.sprite)).convert_alpha(), (spriteButton.get_height(), spriteButton.get_height())), 4), (optionsS.get_width()-(145+spriteButton.get_height()), y))
				except:
					if not tileAdd.sprite == "":
						print(tileAdd.sprite)
						print("couldnt render tile preview")
			else:
				optionsS.blit(roundSurface(pygame.transform.scale(pygame.image.load("tiles/"+tileAdd.get_frame(time)).convert_alpha(), (spriteButton.get_height(), spriteButton.get_height())), 4), (optionsS.get_width()-(145+spriteButton.get_height()), y))
				spriteButton.blit(font20.render(str(len(tileAdd.frames))+" Frames", 20, lightGray), (5, 0))

			if Rect((optionsS.get_width()-140, y), (130, txt.get_height())).collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
				if pressed:
					root = Tk()
					root.withdraw()
					selection = ""
					selection = filedialog.askopenfilenames() # pragma select sprites
					if len(selection) > 1:
						addTileAnimated = True
						new = animatedTile()
						new.name = tileAdd.name
						new.collision = tileAdd.collision
						for elem in selection:
							new.frames.append(elem.split("/")[-1])
						tileAdd = new

					elif len(selection) == 1:
						tileAdd.sprite = selection[0].split("/")[-1]
						addTileAnimated = False
					root.destroy()
			
			optionsS.blit(spriteButton, (optionsS.get_width()-140, y))


			y += spriteButton.get_height() + 15

			txt = font22.render("Name:", 20, lightGray)
			optionsS.blit(txt, (10, y))
			
			txt = font20.render(tileAdd.name + "|", 20, lightGray)
			nameField = pygame.Surface(( min(max(txt.get_width()+10,130), 300), txt.get_height()))
			if not addEdit == 1:
				nameField.fill((24, 25, 28))  
				txt = font20.render(tileAdd.name, 20, lightGray)
			else:
				nameField.fill((14, 15, 18))  
				slowtime = int(sin(time*0.2)*2)
				if slowtime == 1:
					txt = font20.render(tileAdd.name + "|", 20, lightGray)
				else:
					txt = font20.render(tileAdd.name + " ", 20, lightGray)
			if Rect((optionsS.get_width()-140, y), (130, txt.get_height())).collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
				if pressed:
					addEdit = 1
					typedText = tileAdd.name
			nameField.blit(txt, (5,0))
			optionsS.blit(nameField, (optionsS.get_width() -10 -nameField.get_width() ,y))
			if addEdit == 1:
				tileAdd.name = typedText 
			

			y += nameField.get_height() + 15
			txt = font22.render("CollisionType:", 20, lightGray)
			w = txt.get_width()
			optionsS.blit(txt, (10, y))

			txt = font20.render(project.collisionTypes[tileAdd.collision], 20, lightGray)
			colField = pygame.Surface(( min(max(txt.get_width()+10,130), 300), txt.get_height()))

			# change collision type
			color = lightGray
			add = font22.render("+", 20, lightGray)
			addHitbox = Rect((optionsS.get_width() -10 -colField.get_width() - 35 ,y), (add.get_width(), add.get_height()))
			if addHitbox.collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
				color = (91, 103, 124)  
				if pressed:
					color = (21, 30, 54)  
					if not tileAdd.collision + 1 > len(project.collisionTypes)-1:
						tileAdd.collision += 1
			add = font22.render("+", 20, color)
			optionsS.blit(add, (optionsS.get_width() -10 -colField.get_width() - 35 ,y))

			color = lightGray
			sub = font22.render("-", 20, color)
			subHitbox = Rect((optionsS.get_width() -10 -colField.get_width() - 15 ,y), (sub.get_width(),sub.get_height()))
			if subHitbox.collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
				color = (91, 103, 124) 
				if pressed:
					color = (21, 30, 54)
					if not tileAdd.collision - 1 < 0:
						tileAdd.collision -= 1
			sub = font22.render("-", 20, color)
			optionsS.blit(sub, (optionsS.get_width() -10 -colField.get_width() - 15 ,y))

			# render collision type
			colField.fill((24, 25, 28))  
			colField.blit(txt, (5,0))
			optionsS.blit(colField, (optionsS.get_width() -10 -colField.get_width() ,y))
			
			y += addHitbox.height + 15
			if addTileAnimated:
				animSpeedTitle = font22.render("animation Speed:", 20, lightGray)
				optionsS.blit(animSpeedTitle, (10,y))
				steps = 0.5
				color = lightGray
				add = font22.render("+", 20, lightGray)
				addHitbox = Rect((optionsS.get_width() -10 -colField.get_width() - 35 ,y), (add.get_width(), add.get_height()))
				if addHitbox.collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
					color = (91, 103, 124)  
					if pressed:
						color = (21, 30, 54)  
						tileAdd.animationSpeed += steps
				add = font22.render("+", 20, color)
				optionsS.blit(add, (optionsS.get_width() -10 -colField.get_width() - 35 ,y))

				color = lightGray
				sub = font22.render("-", 20, color)
				subHitbox = Rect((optionsS.get_width() -10 -colField.get_width() - 15 ,y), (sub.get_width(),sub.get_height()))
				if subHitbox.collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
					color = (91, 103, 124) 
					if pressed:
						color = (21, 30, 54)
						tileAdd.animationSpeed -= steps
				sub = font22.render("-", 20, color)

				optionsS.blit(sub, (optionsS.get_width() -10 -colField.get_width() - 15 ,y))
				
				txt = font20.render(str(tileAdd.animationSpeed), 20, lightGray)
				colField = pygame.Surface((txt.get_width()+10, txt.get_height()))
				colField.fill((24, 25, 28))  
				colField.blit(txt, (5,0))
				optionsS.blit(colField, (optionsS.get_width() -10 - colField.get_width() ,y))
			
			# var
			iconSize = 200
			############ lock to pixes selector #####
			if tileAdd.collision == 0:
				y += addHitbox.height + 15
				if lockToPixels:
					optionsS.blit(lockSurfaceTrue, (10+iconSize+5, optionsS.get_height()-10-iconSize))
				else:
					optionsS.blit(lockSurfaceFalse, (10+iconSize+5, optionsS.get_height()-10-iconSize))



				if pressed and Rect((10+iconSize+5, optionsS.get_height()-10-iconSize), (16,16)).collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
					lockToPixels = not lockToPixels

				######## Alternative color ############
				if altColor:
					optionsS.blit(altColorSurfaceTrue, (10+iconSize+5, optionsS.get_height()-10-iconSize+5+25))
				else:
					optionsS.blit(altColorSurfaceFalse, (10+iconSize+5, optionsS.get_height()-10-iconSize+5+25))



				if pressed and Rect((10+iconSize+5, optionsS.get_height()-10-iconSize+5+25), (16,16)).collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
					altColor = not altColor

				############ custom collision##############################
			
				# render collision icon preview
			
				pygame.draw.rect(optionsS, windowBgDark, Rect((10, optionsS.get_height()-10-iconSize), (iconSize, iconSize)), 0, roundness )
				if not addTileAnimated:
					try: 
						optionsS.blit(pygame.transform.scale(pygame.image.load("tiles/"+str(tileAdd.sprite)).convert_alpha(), (iconSize, iconSize)), (10, optionsS.get_height()-10-iconSize))
					except:
						if not tileAdd.sprite == "":
							print(tileAdd.sprite)
							print("couldnt render custom collision tile image preview")
				else:
					optionsS.blit(pygame.transform.scale(pygame.image.load("tiles/"+tileAdd.get_frame(time)).convert_alpha(), (iconSize, iconSize)), (10, optionsS.get_height()-10-iconSize))

				# corner logic
				if pygame.mouse.get_pressed()[0]:
					if Rect((5 + tileAdd.collisionRect[0][0]*iconSize, (optionsS.get_height()-10-iconSize)+ tileAdd.collisionRect[0][1]*iconSize-5 ), (10,10)).collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
						mouseEdgeAttached = 0
					elif Rect((5 + tileAdd.collisionRect[1][0]*iconSize, (optionsS.get_height()-10-iconSize)+ tileAdd.collisionRect[1][1]*iconSize-5 ), (10,10)).collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
						mouseEdgeAttached = 1
				else:
					mouseEdgeAttached = -1
					

				if mouseEdgeAttached in [1,0]:
					tileAdd.collisionRect[mouseEdgeAttached][0] = (mousePos[0] - (((monitor_size[0]-optionsS.get_width())/2)+10)) / iconSize       
					tileAdd.collisionRect[mouseEdgeAttached][1] = (mousePos[1] - (((monitor_size[1]-optionsS.get_height())/2)+optionsS.get_height()-10-iconSize)) / iconSize       

				gap = 0.05 # max distance between edges on axis

				


				if lockToPixels:
					tileAdd.collisionRect = [[math.ceil(tileAdd.collisionRect[0][0] * project.tileRes)/project.tileRes, 	math.ceil(tileAdd.collisionRect[0][1] * project.tileRes)/project.tileRes],
						[math.ceil(tileAdd.collisionRect[1][0] * project.tileRes)/project.tileRes, 	math.ceil(tileAdd.collisionRect[1][1] * project.tileRes)/project.tileRes]]

				tileAdd.collisionRect[1][0] = min(1, max(tileAdd.collisionRect[0][0] + gap, tileAdd.collisionRect[1][0]))
				tileAdd.collisionRect[1][1] = min(1, max(tileAdd.collisionRect[0][1] + gap, tileAdd.collisionRect[1][1]))
				tileAdd.collisionRect[0][0] = min(tileAdd.collisionRect[1][0] - gap, max(0, tileAdd.collisionRect[0][0]))
				tileAdd.collisionRect[0][1] = min(tileAdd.collisionRect[1][0] - gap, max(0, tileAdd.collisionRect[0][1]))

				tileAdd.collisionRect[1][0] = min(1, max(0+gap, tileAdd.collisionRect[1][0]))
				tileAdd.collisionRect[1][1] = min(1, max(0+gap, tileAdd.collisionRect[1][1]))
				tileAdd.collisionRect[0][0] = min(1-gap, max(0, tileAdd.collisionRect[0][0]))
				tileAdd.collisionRect[0][1] = min(1-gap, max(0, tileAdd.collisionRect[0][1]))


				# render corners
				if altColor:
					col = altCollisionColor
				else:
					col = customCollisionColor
				for corner in (tileAdd.collisionRect):
					pygame.draw.circle(optionsS, col, (10 + corner[0]*iconSize, (optionsS.get_height()-10-iconSize)+ corner[1]*iconSize ), 5)
				fix = 1
				pygame.draw.rect(optionsS, col, Rect( (10 + tileAdd.collisionRect[0][0]*iconSize, 		(optionsS.get_height()-10-iconSize) + tileAdd.collisionRect[0][1]*iconSize   ), 					((iconSize*tileAdd.collisionRect[1][0])-(iconSize*tileAdd.collisionRect[0][0])+fix, (iconSize*tileAdd.collisionRect[1][1])-(iconSize*tileAdd.collisionRect[0][1])+fix) ), 2, 2 ) 


			############ Done button ###################################
			color = (24, 25, 28)
			txt = font28.render("Done", 20, lightGray)
			w = txt.get_width()
			h = txt.get_height()
			x = 12
			pos = [optionsS.get_width()-w-25, optionsS.get_height()-h-8]
			doneRect = Rect((pos[0]-20, pos[1]), (w+40, h+4))
			if doneRect.collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
				color = (14, 15, 18)  
				if pressed:
					done = True
					if tileAdd.name == "":
						done = False
					if addTileAnimated:
						if tileAdd.frames == []:
							done = False
					else:
						if tileAdd.sprite == "":
							done = False						
					if done: # pragma done
						if editingMode == 0:
							Id = str(len(project.tileTypes)+1).zfill(4)
							project.tileTypes[Id] = tileAdd
							optionsRequired = False
							optionsKind = 0
							addEdit = 0
							if not addTileAnimated:
								project.tilesurfaces[Id] = pygame.image.load("tiles/"+str(tileAdd.sprite))
							else:
								temSpriteList = []
								for frame in tileAdd.frames:
									temSpriteList.append(pygame.image.load("tiles/"+str(frame)))
								project.tilesurfaces[Id] = temSpriteList

									
						elif editingMode == 1:
							Id = editedTileId
							project.tileTypes[Id] = tileAdd
							optionsRequired = False
							optionsKind = 0
							addEdit = 0
					else:
						color = (255,10,40)  
					
			
			pygame.draw.rect(optionsS, color, doneRect)
			txt = font28.render("Done", 20, lightGray)
			optionsS.blit(txt, ((pos[0], pos[1]-2)))

		elif optionsKind == 0:
			optionsS = pygame.Surface((int(monitor_size[0]*(1/8)), int(monitor_size[1]*(2/5))))
			optionsS.fill(windowBg)
			optionsS.blit(font28.render("Add Object", 20, lightGray), (10, 5))

		elif optionsKind == 3:
			am = 3
			optionsS = pygame.Surface((int(monitor_size[0]*(1/8)), int(monitor_size[1]*(2/12))))
			optionsS.fill(windowBg)

			# Title
			rect = Rect((8, 0),     (optionsS.get_width()-16,	int((optionsS.get_height()/am) -2)))
			txt = font28.render("Select type", 20, lightGray)
			w = txt.get_width()
			h = txt.get_height()
			optionsS.blit(txt, ((optionsS.get_width()-w) /2, rect.y +  (rect.height-h)/2 ))

			# static Tile
			rect = Rect((8, int((optionsS.get_height()/am) * 1 )),     (optionsS.get_width()-16,	int((optionsS.get_height()/am) -8)))
			txt = font22.render("static Tile", 20, lightGray)
			w = txt.get_width()
			h = txt.get_height()
			col = (33, 31, 36)  
			if rect.collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
				col = (26, 24, 29)  
				if pressed:
					col = (0,0,0)
					optionsKind = 1
					tileAdd = staticTile()
					tileAdd.collision=1
					addTileAnimated = False
					editingMode=0
			pygame.draw.rect(optionsS, col, rect, 0, roundness)
			optionsS.blit(txt, ((optionsS.get_width()-w) /2, rect.y +  (rect.height-h)/2 ))

			# dynamic tile
			rect = Rect((8, int((optionsS.get_height()/am) * 2 )),     (optionsS.get_width()-16,	int((optionsS.get_height()/am) -8)))
			txt = font22.render("dynamic Tile", 20, lightGray)
			w = txt.get_width()
			h = txt.get_height()
			col = (33, 31, 36)  
			if rect.collidepoint((mousePos[0]-(monitor_size[0]-optionsS.get_width())/2),  (mousePos[1]-(monitor_size[1]-optionsS.get_height())/2)):
				col = (26, 24, 29) 
				if pressed:
					col = (0,0,0)
					pass
			pygame.draw.rect(optionsS, col, rect, 0, roundness)
			optionsS.blit(txt, ((optionsS.get_width()-w) /2, rect.y +  (rect.height-h)/2 ))
			#pygame.draw.rect(optionsS, windowBgDark, Rect((8, int((optionsS.get_height()/am) * 2 )), 	(optionsS.get_width()-16,	int((optionsS.get_height()/am) -16)) ))
			#pygame.draw.rect(optionsS, windowBgDark, Rect((8, int((optionsS.get_height()/4) * 3 )),		(optionsS.get_width()-16,	int((optionsS.get_height()/4) -16)) ))


	window.blit(menueS, (0,0))
	window.blit(previewS, (0,int(monitor_size[1]*.5/10)))
	window.blit(sceneS, (int(monitor_size[0]*4/5),0))
	window.blit(tilesS, (int(monitor_size[0]*4/5),int(monitor_size[1]*2/5 - tilesSceneRatio)))
	window.blit(tileDispS, (int(monitor_size[0]*4/5),int(monitor_size[1]*2/5 - tilesSceneRatio+boxheight)))
	window.blit(ppS, (0,0))
	if optionsRequired:
		optionsS = roundSurface(optionsS, roundness+2)
		window.blit(optionsS, ((monitor_size[0]-optionsS.get_width())/2,(monitor_size[1]-optionsS.get_height())/2))
	#debugger.debug(addTileAnimated)
	debugger.renderDebug()
	pygame.display.flip()
	pygame.display.update()
	editname = False
	f2p = False
	time +=1
	deltatime = clock.tick(FPS)
pygame.quit()
sys.exit()