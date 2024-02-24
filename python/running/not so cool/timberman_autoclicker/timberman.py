import pyautogui, time
# 1153, 397 = 000

#68 - 544 - 612
nextlog = "l"
time.sleep(4)
while True:
	myScreenshot = pyautogui.screenshot(region=(829, 1080-395, 300, 1))

	pxL = myScreenshot.getpixel((0, 0))
	pxR = myScreenshot.getpixel((233, 0))

	if pxR == (0,0,0):
		nextlog = "r"
	if pxL == (0,0,0):
		nextlog = "l"

	if nextlog == "r":
		pyautogui.write('a')
	elif nextlog == "l": 	
		pyautogui.write('d')

	pyautogui.write(' ')

	print(str(pxL) + " : " + str(pxR))
	#time.sleep(0.01)