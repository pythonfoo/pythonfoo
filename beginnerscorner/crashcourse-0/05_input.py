#!/usr/bin/env python

# get user input
myInput = raw_input("enter some foo: ")

# THIS is BALLZ (in python 2.6/2.7), describe why!
#myInput = input("enter some foo: ")

print "you entered:", myInput

# do stuff ONLY if this the input is a digit
if myInput.isdigit() == True:
	print 'yes we digit'
	
	numberOne = 11
	numberTwo = 0
	
	# this would fail
	#numberTwo = myInput
	
	# convert FIRST
	numberTwo = int(myInput)
	
	numberOne += numberTwo
	print numberOne
	
else:
	print 'just text dude'

