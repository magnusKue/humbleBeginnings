# Just some tries
x = ["sword", "shield", "axe", "bow", "crossbow", "rod", "stick", "bat", "lance", "dagger", "shortsword", "spear"]
items = {"sword" : 3, "shield" : 2, "axe": 2, "bow" : 5, "crossbow" : 6, "rod" : 7, "stick" : 4, "bat" : 2, "lance" : 4, "dagger" : 3, "shortsword" : 1, "spear" : 6}
for c in range(0, len(x)):
	print(x[c], ":",items[x[c]])