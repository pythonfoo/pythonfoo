#!/usr/bin/python
import time
import datetime
# 
# str(datetime.timedelta(seconds=666))

print time.strftime("%d %m %Y %H:%M:%S ")

inputTmp = raw_input("Enter Delay (in mins, def 0): ")
if inputTmp != '':
	execTime = int(inputTmp) * 60

actualTime = time.time()
targetTime = actualTime + execTime
while actualTime < targetTime:
	actualTime =  time.time()
	print str(targetTime - actualTime)
	print str(datetime.timedelta(seconds=(targetTime - actualTime)))
	time.sleep(1)

print "End!!1!"
