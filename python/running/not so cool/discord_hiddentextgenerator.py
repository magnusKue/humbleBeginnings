import os
os.system("echo \u001b[31m !!Maxi is daPussy!! \u001b[0m")
running = True
while running:
	string = "pop"
	if "EXIT" in string.upper():
		running = not running
		print("done")
		continue
	end = ""
	st = True
	for x in string:
		if st:
			st = not st
			continue
		elif len(end)<=200-5:
			if x==" " and string[0]=="Y":
				end+=" "
				continue
			end += "||"+x+"||"
	print(end)