#!/usr/bin/env python

# basic vars
tmpTxt = '' # just a temp var!
fooTxt = 'i am a string'
fooInt = 101
fooFloat = 1.01

# show what we have
print fooTxt, fooInt, fooFloat

# concat errors!
#tmpTxt = fooTxt + fooInt + fooFloat

# correct!
tmpTxt = fooTxt + str(fooInt) + str(fooFloat)

# print what we have
print tmpTxt

# add stuff
fooInt += 22
fooFloat += fooInt

print fooInt, fooFloat


# OVERWRITE / RE-ASSIGN
fooInt = 22
fooFloat = fooInt

print fooInt, fooFloat

