#!/usr/bin/python
import time, os

timerStart = time.time()
for aFile in os.listdir('.'):
	mTime = time.ctime(os.path.getmtime(aFile))
	mTimeLocal = time.localtime(os.path.getmtime(aFile))
	
	cTime = time.ctime(os.path.getctime(aFile))
	cTimeLocal = time.localtime(os.path.getctime(aFile))
	
	print '############', aFile , '############'
	print 'mtime:', mTime, 'local:', time.strftime('%d_%m_%Y' , mTimeLocal), mTimeLocal
	print 'ctime:', cTime, 'local:', time.strftime('%d_%m_%Y' , cTimeLocal), cTimeLocal


print 'mtime = last changed'
print 'ctime = last access'
print 'duration:', str(time.time() - timerStart)

