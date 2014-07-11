#!/usr/bin/env python

userName = 'Dave'

# demonstrate uppercase, lowercase stuff
if userName == 'Dave':
	print 'HELLO'
elif userName == 'anon':
	print 'legion'
else:
	print 'I CAN NOT ALLOW THAT', userName
	

icnat = 'I CAN NOT ALLOW THAT'

# demonstrate negative
if userName != 'Dave' and userName != 'dave':
	print icnat
else:
	print 'hello', userName
	
	
# demonstrate some basic logic stuff
numOne = 1
numTwo = 2

if numOne == 1 and numTwo == 2:
	print "all true"
elif numOne != 1:
	print "one is out space"
elif numTwo != 2:
	print "two is out space"
