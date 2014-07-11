#!/usr/bin/python

import gc

class tC(object):
	def __init__(self):
		self.name = 'nx'
		self.val = ''
		for i in range(100):
			self.val += 'ASDF'

def testArray():
	iAr = []

	raw_input('go')

	for i in range(50000):
		iAr.append(tC())
		print i
	
	raw_input('clear')
	print len(iAr)
	del iAr
testArray()
#iAr = None
#pop() / remove(iten)
#del iAr[1:49998]
#print len(iAr)
print "gc " + str(gc.get_count())
gc.collect()
raw_input('done')
print "gc " + str(gc.get_count())
