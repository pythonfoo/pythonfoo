#!/usr/bin/python

print '\n# 10 times'
for i in range(10):
	print i

print '\n# from, to, steps'
test = range(5, 10 ,2)
print test

print '\n# reversed'
test.reverse()
print test

for i in range(9, -1, -1):
	print i
