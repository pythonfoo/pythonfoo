

size = 10
#foorayOne = [[0]*size]*size
foorayOne = []



for x in range(0, size):
	foorayOne.append([])
	for y in range(0, size):
		foorayOne[x].append(0)
		foorayOne[x][y] = x*y

print foorayOne
