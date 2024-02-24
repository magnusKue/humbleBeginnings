from tkinter import colorchooser, filedialog
import pygame, sys, random, time
from tkinter import *
from pygame.locals import *
from classes import *

# Pygame
clock = pygame.time.Clock()
success, failures = pygame.init()
print(f"successes: {success}\nfailures: {failures}")

pygame.display.set_caption('maple')
winSize = 5/5
monitor_size = [int(pygame.display.Info().current_w*winSize), int(pygame.display.Info().current_h*winSize)]
s=1
window = pygame.display.set_mode((int(monitor_size[0]/s), int(monitor_size[1]/s)), pygame.NOFRAME)

# Windows
menueS = pygame.Surface((int(monitor_size[0]*(4/5)), int(monitor_size[1]*.5/10)))
previewS = pygame.Surface((int(monitor_size[0]*(4/5)), int(monitor_size[1]*9.5/10)))
sceneS = pygame.Surface((int(monitor_size[0]*(1/5)), int(monitor_size[1]*(2/5))))
tilesS = pygame.Surface((int(monitor_size[0]*(1/5)), int(monitor_size[1]*(3/5))))
optionsS = pygame.Surface((int(monitor_size[0]*(1/5)), int(monitor_size[1]*(2/5))))
ppS = pygame.Surface((monitor_size[0], monitor_size[1]))

# Variables
FPS = 60;
running = True
lastFramepressed = False
project = None # loaded project
editingLayer = None
mouseWheel = 0
lastMouseWheelState = 0
typedText = ""
lastFramePressed = False

#> scene
selectedArea = 0
selectedLayer = 0
editname = False
sceneScroll = 0
lasty = 0
editedLayer = -1 # -1 = Area is edited not layer else layer id
editedArea = -1 # -1 = nothing is edited else area id
editedWindow = 0 # 0=sceneS 1=tilesS 2=previewS

#> Preview
bg = (133, 237, 230)

#> Tiles
selectedObjectKind = 1 # 0 = Obj, 1 = Tiles
editedTiletype = "001"
editedObjecttype = "001"
filename = ""

#> options
optionsRequired = False
optionsKind = 0 # 0 = addObject, 1 = addTile
#
#

# Test project
project = Project()
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
add1.name = "grass"
add1.sprite = "grass.png"
project.tileTypes["001"] = add1

add1 = staticTile()
add1.name = "dirt"
add1.sprite = "dirt.png"
project.tileTypes["002"] = add1

add1 = staticTile()
add1.name = "none"
add1.sprite = "none.png"
project.tileTypes["003"] = add1

for x in range(10):
	add1 = staticTile()
	add1.name = "new"+str(x+1)
	add1.sprite = "new"+str(x+1)+".png"
	project.tileTypes["000"+str(x+1)] = add1



add1 = staticObject()
add1.name = "tree"
add1.sprite = "tree.png"
project.objectTypes["001"] = add1

project.areas[0].layers[0].content.append(Chunk(Vec2(0,0),16))
project.areas[0].layers[0].content[0].fill()

font32 = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 32)
font32Fat = pygame.font.Font("fonts\\NotoSansJP-Medium.otf", 32)
font28 = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 28)
font24 = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 24)
font22 = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 22)
font20 = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 20)
font16 = pygame.font.Font("fonts\\NotoSansJP-Regular.otf", 16)

ppS.set_alpha(0)

###### functions ##################

def changeBgcolor():
	bg = colorchooser.askcolor()

## Tkinter ##

def updateScene(sceneScroll, editedWindow, editedLayer, editedArea, selectedArea, selectedLayer, typedText, mouseWheel, lastMouseWheelState):
	sceneS.fill((48, 51, 56))

	# clamp scroll
	if mouseWheel == lastMouseWheelState:
		mouseWheel = 0
	lastMouseWheelState = mouseWheel

	sceneScroll += mouseWheel * 10
	if sceneScroll >= 0: sceneScroll = 0

	#start drawing
	y = 50 + sceneScroll
	for x in range(0, len(project.areas)):
		#print(editedWindow, " : ", editedArea, " : ", editedLayer, " ", editname)
		# collide and expand
		areaTextWidth = font28.render(project.areas[x].name + " ^", 0, (141, 153, 174)).get_width()
		areaTextHeight = font28.render(project.areas[x].name + " ^", 0, (141, 153, 174)).get_height()
		ahitbox = Rect((10,y), (areaTextWidth, areaTextHeight))

		if pressed and ahitbox.collidepoint( ( int(mousePos[0]-monitor_size[0]*4/5) , mousePos[1])):
			project.areas[x].editIsExpanded = not project.areas[x].editIsExpanded
		if editname and ahitbox.collidepoint( ( int(mousePos[0]-monitor_size[0]*4/5) , mousePos[1])):
			editedWindow = 0
			editedArea = x
			editedLayer = -1
			typedText = project.areas[x].name

		# collide and change visibility or add layer
		vTextWidth = font28.render("○", 5, (0,0,0)).get_width()
		vTextHeight = font28.render("○", 0, (141, 153, 174)).get_height()
		vhitbox = Rect((monitor_size[0]*1/5-(vTextWidth+5), y+9), (vTextWidth, int(vTextHeight*2/3)))
		addLayerHitbox = Rect((monitor_size[0]*1/5-(vTextWidth+5)-20, y+9), (vTextWidth, int(vTextHeight*2/3)))

		if pressed and vhitbox.collidepoint( ( int(mousePos[0]-monitor_size[0]*4/5) , mousePos[1])):
			project.areas[x].editIsVisible = not project.areas[x].editIsVisible
		if pressed and addLayerHitbox.collidepoint( ( int(mousePos[0]-monitor_size[0]*4/5) , mousePos[1])):
			editedArea = x 
			editedWindow = 0
			editedLayer = len(project.areas[x].layers)
			typedText = ""
			add = Layer("new Layer")
			project.areas[x].layers.append(add)


		# Area name editing
		if editedWindow == 0 and editedArea == x and editedLayer == -1:
			project.areas[x].name = typedText
			editingAreaTextHeight = font24.render(str(project.areas[x].name), 20, (48, 51, 56)).get_height()
			pygame.draw.rect(sceneS, (0, 0, 0), Rect((0,y+7), (sceneS.get_width(), editingAreaTextHeight)))
		else:
			project.areas[x].name = project.areas[x].name.rstrip()

		# render area name + dropdown
		if project.areas[x].editIsExpanded:
			if project.areas[x].layers != []:
				sceneS.blit(font28.render(project.areas[x].name + " ^", 20, (141, 153, 174)), (10, y))
			else:
				sceneS.blit(font28.render(project.areas[x].name + "  ", 20, (141, 153, 174)), (10, y))
		else:   
			if selectedArea == x:
				selectedTextHeight = font28.render(str(project.areas[x].name), 20, (0, 0, 0)).get_height()
				pygame.draw.rect(sceneS, (151, 163, 184), Rect((0,y+7), (sceneS.get_width(), selectedTextHeight-9)))
				if project.areas[x].layers != []:
					sceneS.blit(font28.render(project.areas[x].name + " v", 20, (48, 51, 56)), (10, y))
				else:
					sceneS.blit(font28.render(project.areas[x].name + "  ", 20, (48, 51, 56)), (10, y))
			else:
				if project.areas[x].layers != []:
					sceneS.blit(font28.render(project.areas[x].name + " v", 20, (141, 153, 174)), (10, y))
				else:
					sceneS.blit(font28.render(project.areas[x].name + "  ", 20, (141, 153, 174)), (10, y))


		# render visibility
		if project.areas[x].editIsVisible:    
			visibility = "●"            
		else:   
			visibility = "○"
		if selectedArea == x and not project.areas[x].editIsExpanded:
			col = (48, 51, 56)
		else: col = (141, 153, 174)
		sceneS.blit(font16.render(visibility, 20, col), (monitor_size[0]*1/5-(vTextWidth), y+11))

		sceneS.blit(font20.render("+", 20, col), (monitor_size[0]*1/5-(vTextWidth)-20, y+8))
		y += 30



		# render layers #################################################
		for l in range(0, len(project.areas[x].layers)):
				
			# Layer name editing
			if editedWindow == 0 and editedArea == x and editedLayer == l:
				project.areas[x].layers[l].name = typedText
				editingLayerTextHeight = font24.render(str(project.areas[x].layers[l].name), 20, (48, 51, 56)).get_height()
				pygame.draw.rect(sceneS, (0,0,0), Rect((0,y+6), (sceneS.get_width(), editingLayerTextHeight-6)))
			else:
				project.areas[x].layers[l].name = project.areas[x].layers[l].name.rstrip()

			# layer rendering
			if project.areas[x].editIsExpanded:
				if x == selectedArea and l == selectedLayer:
					selectedTextHeight = font24.render(str(project.areas[x].layers[l].name), 20, (48, 51, 56)).get_height()
					pygame.draw.rect(sceneS, (151, 163, 184), Rect((0,y+7), (sceneS.get_width(), selectedTextHeight-9)))
					sceneS.blit(font24.render("└ " + str(project.areas[x].layers[l].name), 20, (48, 51, 56)), (20, y))
				else:
					sceneS.blit(font24.render("└ " + str(project.areas[x].layers[l].name), 20, (151, 163, 184)), (20, y))

				# collision
				lTextWidth = font24.render("└ " + str(project.areas[x].layers[l].name), 5, (0,0,0)).get_width()
				lTextHeight = font24.render("└ " + str(project.areas[x].layers[l].name), 0, (141, 153, 174)).get_height()
				lhitbox = Rect((monitor_size[0]*4/5, y+7), (sceneS.get_width(), int(lTextHeight)))
				pygame.draw.rect(sceneS, (255,0,0), lhitbox)

				if pressed and lhitbox.collidepoint( (mousePos[0] , mousePos[1])) and mousePos[1] > 49 and mousePos[1] < sceneS.get_height():
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
	if pressed and addhitbox.collidepoint( (mousePos[0] , mousePos[1])):
		addButtonCol = (100, 110, 120)
		# add area to scene
		ol=len(project.areas)
		project.areas.append(Area("new Area"))
		editedWindow = 0
		editedArea = ol
		editedLayer = -1
		typedText = ""
	else: addButtonCol = (171, 183, 204)

	# render sScene headline
	pygame.draw.rect(sceneS,(48, 51, 56), Rect((0,0), (int(monitor_size[0]*1/5), 49)))
	sceneS.blit(font32Fat.render("Areas: ", 20, (171, 183, 204)), (10, 5))
	sceneS.blit(font32Fat.render("+", 20, addButtonCol), (sceneS.get_width()-32, 5))

	window.blit(menueS, (0,0))
	window.blit(previewS, (0,int(monitor_size[1]*.5/10)))
	window.blit(sceneS, (int(monitor_size[0]*4/5),0))
	window.blit(tilesS, (int(monitor_size[0]*4/5),int(monitor_size[1]*2/5)))

	return sceneScroll, editedWindow, editedLayer, editedArea, selectedArea, selectedLayer, typedText, mouseWheel, lastMouseWheelState

def updateTiles(selectedObjectKind, editedTiletype, editedObjecttype, optionsRequired, optionsKind):

	### Top bar ################################
	# collide obj / tiles
	objBox = Rect((10,11), (int(tilesS.get_width()*1/5), int(tilesS.get_height()*1/17-10)))
	if objBox.collidepoint((int(mousePos[0]-monitor_size[0]*4/5), int(mousePos[1]-monitor_size[1]*2/5))) and pressed:
		selectedObjectKind = 0

	tilesBox = Rect((int(tilesS.get_width()*1/5+21),11), (int(tilesS.get_width()*1/5), int(tilesS.get_height()*1/17-10)))
	if tilesBox.collidepoint((int(mousePos[0]-monitor_size[0]*4/5), int(mousePos[1]-monitor_size[1]*2/5))) and pressed:
		selectedObjectKind = 1

	pygame.draw.rect(tilesS, (28, 31, 36), Rect((0,0), (tilesS.get_width(), 2)) )	# trennlinie
	pygame.draw.rect(tilesS, (28, 31, 36), Rect( (0,int(tilesS.get_height()*1/17-2)), (tilesS.get_width(), int(tilesS.get_height()*16/17+11)) ) ) 


	pygame.draw.rect(tilesS, (28, 31, 36), Rect((int(tilesS.get_width()*1/5+19),9), (int(tilesS.get_width()*1/5+4), int(tilesS.get_height()*1/17-10+4))))
	if selectedObjectKind == 1:
		pygame.draw.rect(tilesS, (48, 51, 56), Rect((int(tilesS.get_width()*1/5+21),11), (int(tilesS.get_width()*1/5), int(tilesS.get_height()*1/17-10))))
	else: 
		pygame.draw.rect(tilesS, (28, 31, 36), Rect((int(tilesS.get_width()*1/5+21),11), (int(tilesS.get_width()*1/5), int(tilesS.get_height()*1/17-10))))
	tilesS.blit(font20.render("Tile", 20, (141, 153, 174)), (int(tilesS.get_width()*1/5+24), 7))

	pygame.draw.rect(tilesS, (28, 31, 36), Rect((8,9), (int(tilesS.get_width()*1/5+4), int(tilesS.get_height()*1/17-10+4))))
	if selectedObjectKind == 0:
		pygame.draw.rect(tilesS, (48, 51, 56), Rect((10,11), (int(tilesS.get_width()*1/5), int(tilesS.get_height()*1/17-10))))
	else:
		pygame.draw.rect(tilesS, (28, 31, 36), Rect((10,11), (int(tilesS.get_width()*1/5), int(tilesS.get_height()*1/17-10))))
	tilesS.blit(font20.render("Object", 20, (141, 153, 174)), (12, 7))

	txt = font24.render("+", 20, (141, 153, 174))
	width = txt.get_width()
	height = txt.get_height()
	addTileHitbox = Rect((int( tilesS.get_width() - 5 - width ), 0), (width,height))
	col = (141, 153, 174)
	if pressed and addTileHitbox.collidepoint((mousePos[0] - previewS.get_width(), mousePos[1] - sceneS.get_height())):
		col = (70, 75, 90)
		if selectedObjectKind == 1:
			optionsRequired = True
			optionsKind = 1

	txt = font24.render("+", 20, col)
	tilesS.blit(txt, (int( tilesS.get_width() - 5 - width ), 0))



	pygame.draw.rect(tilesS, (48, 51, 56), Rect( (0,int(tilesS.get_height()*1/17)), (tilesS.get_width(), int(tilesS.get_height()*16/17+11)) ) )
	
	###### Render Tiles ######################
	if selectedObjectKind == 1:
		gap = 10
		IconsPerLine = 6
		iconSize = int((tilesS.get_width()-gap*(IconsPerLine+1))/IconsPerLine)
		x = 0
		y = 0
		for Id in project.tileTypes:
			### Collision ##################
			tileIconHitbox = Rect((gap + x * (iconSize+gap),  gap + y * (iconSize+gap) + int(tilesS.get_height()*1/17) + 10), (iconSize, iconSize))
			if  tileIconHitbox.collidepoint( mousePos[0] - previewS.get_width(), mousePos[1] - sceneS.get_height()) and pressed:
				editedTiletype = Id


		### Render Tile Icons ##########
			try:
				icon = pygame.image.load("tiles/"+project.tileTypes[Id].sprite)
			except:
				icon = pygame.image.load("gui/notFound.png")
			if editedTiletype == Id:
				pygame.draw.rect(tilesS, (170,170,200), Rect((gap + x * (iconSize+gap),  gap + y * (iconSize+gap) + int(tilesS.get_height()*1/17) + 10), (iconSize, iconSize)) )
				icon = pygame.transform.scale(icon, (iconSize-6, iconSize-6))
				tilesS.blit(icon, (3 + gap + x * (iconSize+gap), 3 + gap + y * (iconSize+gap) + int(tilesS.get_height()*1/17) + 10))
			else:
				icon = pygame.transform.scale(icon, (iconSize, iconSize))
				tilesS.blit(icon, (gap + x * (iconSize+gap),  gap + y * (iconSize+gap) + int(tilesS.get_height()*1/17) + 10))

			if x <= IconsPerLine-2:
				x += 1
			else:
				x = 0
				y += 1

	###### Render Objects ######################
	elif selectedObjectKind == 0:
		gap = 10
		IconsPerLine = 4
		iconSize = int((tilesS.get_width()-gap*(IconsPerLine+1))/IconsPerLine)
		x = 0
		y = 0
		for Id in project.objectTypes:
			### Collision ##################
			tileIconHitbox = Rect((gap + x * (iconSize+gap),  gap + y * (iconSize+gap) + int(tilesS.get_height()*1/17) + 10), (iconSize, iconSize))
			if  tileIconHitbox.collidepoint( mousePos[0] - previewS.get_width(), mousePos[1] - sceneS.get_height()) and pressed:
				editedObjecttype = Id

		### Render Object Icons ##########
			#try:
			orgIcon = pygame.image.load("objects/"+project.objectTypes[Id].sprite)
			if orgIcon.get_width() > orgIcon.get_height():
				size = orgIcon.get_width()
			else: size = orgIcon.get_height()
			icon = pygame.Surface((size, size))
			icon.fill((117,109,109))
			icon.blit(orgIcon, (int((size-orgIcon.get_width())/2),0))
			#except:
				#print("didnt find tile icon of ID: " + str(Id))
				#icon = pygame.image.load("gui/notFound.png")
			if editedObjecttype == Id:
				pygame.draw.rect(tilesS, (170,170,200), Rect((gap + x * (iconSize+gap),  gap + y * (iconSize+gap) + int(tilesS.get_height()*1/17) + 10), (iconSize, iconSize)) )
				icon = pygame.transform.scale(icon, (iconSize-6, iconSize-6))
				tilesS.blit(icon, (3 + gap + x * (iconSize+gap), 3 + gap + y * (iconSize+gap) + int(tilesS.get_height()*1/17) + 10))
			else:
				icon = pygame.transform.scale(icon, (iconSize, iconSize))
				tilesS.blit(icon, (gap + x * (iconSize+gap),  gap + y * (iconSize+gap) + int(tilesS.get_height()*1/17) + 10))

			if x <= IconsPerLine-2:
				x += 1
			else:
				x = 0
				y += 1


	# render mode-buttons
	# Tile mode
	# render add button
	return selectedObjectKind, editedTiletype, editedObjecttype, optionsRequired, optionsKind


while running:
	window.fill((0,0,0))
	# check if mouse is pressed 
	mousePos = pygame.mouse.get_pos()
	mouseState = pygame.mouse.get_pressed()[0]
	if mouseState and mouseState != lastFramePressed:
		pressed = True
	else:
		pressed = False
	lastFramePressed = mouseState
	
	# main loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.VIDEORESIZE:
			window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
			monitor_size = [event.w, event.h]
			previewS = pygame.Surface((int(monitor_size[0]*(4/5)), int(monitor_size[1])))
			sceneS = pygame.Surface((int(monitor_size[0]*(1/5)), int(monitor_size[1]*(2/5))))
			tilesS = pygame.Surface((int(monitor_size[0]*(1/5)), int(monitor_size[1]*(3/5))))
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
			elif event.key == K_DELETE:
				sceneHitbox = Rect((monitor_size[0]*4/5, 0), (sceneS.get_height(), sceneS.get_width()))
				if sceneHitbox.collidepoint(mousePos[0], mousePos[1]):
					if len(project.areas[selectedArea].layers) > 0:
						project.areas[selectedArea].layers.pop(selectedLayer)
			elif event.key == K_F2:
				editname = True
			elif event.key == K_F11:
				pygame.display.toggle_fullscreen()
			elif event.key == pygame.K_BACKSPACE:
				typedText = typedText[:-1]
			elif event.key == pygame.K_RETURN:
				typedText = typedText.rstrip()
				editedWindow = -1
				editedAreaName = -1
				editedLayerName = -1
			else:
				editname = False
				typedText += event.unicode
		if event.type == MOUSEWHEEL:
			mouseWheel = event.y
	# edit

###### MENUE WINDOW ###################################################################################
	menueS.fill((48, 51, 56))
	editB = Rect((2,2), (int(menueS.get_width()*1/9), menueS.get_height()-4))
	pygame.draw.rect(menueS, (150,150,150), editB)
	if pressed:
		if editB.collidepoint((mousePos[0], mousePos[1])):
			print("pressed")
			root = Tk()
			btn=Button(root, text="Change Viewport color", command=changeBgcolor)
			btn.place(x=0, y=0)
			root.title('Edit')
			root.mainloop()

###### PREVIEW WINDOW #################################################################################
	previewS.fill(bg)
###### SCENE WINDOW ###################################################################################
	sceneScroll, editedWindow, editedLayer, editedArea, selectedArea, selectedLayer, typedText, mouseWheel, lastMouseWheelState = updateScene(sceneScroll, editedWindow, editedLayer, editedArea, selectedArea, selectedLayer, typedText, mouseWheel, lastMouseWheelState)
###### Tiles WINDOW ###################################################################################
	tilesS.fill((48, 51, 56))
	selectedObjectKind, editedTiletype, editedObjecttype, optionsRequired, optionsKind = updateTiles(selectedObjectKind, editedTiletype, editedObjecttype, optionsRequired, optionsKind)
###### options WINDOW ###################################################################################
	optionsS.fill((255,0,0))
	#print(optionsRequired)
	if optionsRequired:
		if optionsKind == 1:
			optionsS.blit(font28.render("AddTile", 20, (141, 153, 174)), (10, 5))
		
		window.blit(optionsS, ((monitor_size[0]-optionsS.get_width())/2,(monitor_size[1]-optionsS.get_height())/2))

######              ###################################################################################

	# PP
	ppS.fill((0,0,0))
	window.blit(ppS, (0,0))
	pygame.display.update()
	deltatime = clock.tick(FPS)

pygame.quit()
sys.exit()



