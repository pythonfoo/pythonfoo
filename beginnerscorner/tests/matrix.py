#!/usr/bin/python
import time

txt = "The MATRIX has you!"
space = " "
col = "\x1b[32m"
print col
while True:
	print  space + txt,
	if len(space) > 100:
		space = " "
	else:
		space = space + " "
	time.sleep(0.001)
