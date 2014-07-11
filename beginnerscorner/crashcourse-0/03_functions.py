#!/usr/bin/env python

# define a function
def imAfunction():
	print 'lolfunction'

# define a internal function (void)
def imAnotherfunction(name):
	print 'hello', name

# define a return function
def imAcoolFunction(int1, int2):
	# we COULD do it this way, but we make it nice ;)
	#return int1 * int2
	res = int1 * int2
	return res

# just show an empty function
def imEmpty():
	pass

imAfunction()
imAnotherfunction('dave')
imAcoolFunction(3, 3) # NO OUTPUT
print imAcoolFunction(3, 3)

fooInt = 11
fooInt += imAcoolFunction(2, 2)
print fooInt


