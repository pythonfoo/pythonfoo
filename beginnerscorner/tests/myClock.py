#!/usr/bin/python

import os
import time
import datetime

#   1. the year as a four-digit number, e.g. 2007
#   2. the month (1, 2, , 12)
#   3. the day of the month (1, 2, , 31)
#   4. hour (0, 1, , 23)
#   5. minutes (0, 1, , 59)
#   6. seconds (0, 1, , 61 where 60 and 61 are used for leap seconds)
#   7. week day (0=Monday, 1=Tuesday, , 6=Sunday)
#   8. day of the year (1, 2, , 366)
#   9. daylight saving time information (0, 1, or -1)

while True:
	locTime = time.localtime()
	os.system('clear')
	
	lineHolder = str(locTime[3]) + '| '
	for i in range(locTime[3]):
		lineHolder += '#'
	print lineHolder
		
	lineHolder = str(locTime[4]) + '| '
	for i in range(locTime[4]):
		lineHolder += '#'
	print lineHolder

	lineHolder = str(locTime[5]) + '| '
	for i in range(locTime[5]):
		lineHolder += '#'
	print lineHolder
				
	time.sleep(1)
