import math,time
SPEED = .1
MULTIPLYER = 5
count = 0
delay = 5
while True:
	y = [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]
	y[int(math.sin(count)* MULTIPLYER+delay)] = "@"
	print(y)
	time.sleep(.03)
	count += SPEED