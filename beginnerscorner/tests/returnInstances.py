#! /usr/bin/env python

class Test(object):
	def __init__(self, num = 1):
		self.number = 100 + num

	def returnTest(self, num = 0):
		return Test(num)
    
	def returnTest2(self):
		tmp = Test()
		return tmp

t = Test()
print t
print t.returnTest()
print t.returnTest()
t2 = t.returnTest()
print t2
t3 = t.returnTest()
print t3

print t.returnTest(6).number
print t.returnTest2()
print t.returnTest2()

print 'array test'

tmpAr = [t.returnTest(1), t.returnTest(2), t.returnTest(3)]
for c in tmpAr:
	print c
	print c.number
