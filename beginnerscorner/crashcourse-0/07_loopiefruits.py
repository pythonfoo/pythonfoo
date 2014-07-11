#!/usr/bin/env python

userName = "anon"

# show a loop
for i in range(10):
	print i

# show after loop!
print 'afterloop:', i

# show what variable means!
for hamster in range(3):
	print userName, 'has', hamster, "hamsters"

# what is "range"
print range(10)
print range(5, 10)
print range(6, 43, 4)
print range(-10, 0)
print range(0, -10, -2)
	
# demonstrate some list stuff
randomList = ['foo', 42, 'hamster', 23]
for stuff in randomList:
	print stuff

# demonstrate while with name input
while userName != 'Dave':
	userName = raw_input('ENTER CORRECT USERNAME:')
	
print 'HELLO'
