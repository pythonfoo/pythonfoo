#!/usr/bin/python
import time

timeClock = time.clock()
print 'clock: ', timeClock

print time.strftime("%d %m %Y %H:%M:%S ")

#mail-header-format
#Date: Mon, 4 Dec 2006 15:51:37 +0100' + '\n'
print time.strftime("%a, %d %b %Y %H:%M:%S")


pingTimerLast = time.time()

print 'clock: ', time.clock()

for i in range(10000):
	print 'i+clock: ', i, time.clock()
	print str(time.time())
	print str(time.time() - pingTimerLast)

print 'timeClock: ', time.clock()

