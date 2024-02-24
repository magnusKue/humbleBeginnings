import pygame, os, json
from pathlib import Path
from PIL import Image 

# Creates map files from pixels of an .png image


#-------Config---------
type_ = '.txt' ## /".json"
air = '0'
path='result/' #C:/Users/magnu/Downloads/platformer_project_2/ 		don't start with '/'
source='map.png'
filename='map'
alpha = (255,255,255)
colors = {(153, 229, 80, 255):'1', (0, 0, 0, 255):'2', (255, 243, 0):'S'}
#--------Code----------
if path == '':
	files = str(os.path.realpath(__file__)).split('\\')
	path = files[:-1]
	print(path)
	PATH = ''
	for x in path:
		PATH += str(x) + '/'
else: PATH = path
error = False
image = Image.open(source)
width, height = image.size
print(f'MapSize:[{width}, {height}]')
px = image.load() 
Path(PATH + filename + type_).touch()
map = open((PATH + filename + type_), 'w')
dataJson = {};dataTxt = '';process = ''
print(PATH + filename + type_)

for yR in range(height):
	for xR in range(width):
		if px[xR,yR] in colors:
			num = colors[px[xR,yR]]
			print(num, end='')
			process+=num
		elif px[xR,yR] == alpha:
			print(air, end='')
			process+=air
		else:
			error = True
			print(f'\n\n Error: Unknown Pixel: {px[xR, yR]} \n\n')
	print()
	dataTxt += process +'\n'
	dataJson[yR] = process
	process = ''

json_data = json.dumps(dataJson, indent = 4)
if type_ == '.txt':
	map.write(dataTxt)
	print('\nwrote as txt')
elif type_ == '.json':
	map.write(json_data)
	print('\nwrote as txt')
if error:
	print('\n\n\n\n!!!!!!!!!!!!!!!!!!Error: Tile not found!!!!!!!!!!!!!!!!!!!!!\n\n\n')
else: print('\n\nsucces!\n\n')



