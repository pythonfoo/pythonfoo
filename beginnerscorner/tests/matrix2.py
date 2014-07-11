#!/usr/bin/python
import sys
import time

fulltxt=""
txt = "The MATRIX has you!"
space = " "
col = "\x1b[32m"
print col
while True:
	if len(space) > 1024:
		fulltxt=txt
		space=""
	fulltxt = space + txt
	print fulltxt
	time.sleep(0.1)
	#while len(space)<(len(fulltxt)/2):
	space += " "
	#print txt, " "
	#sys.stdout.write(txt)
