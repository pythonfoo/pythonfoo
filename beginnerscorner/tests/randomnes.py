#!/usr/bin/python
import time

rangeInt = 1024 * 1024
rangeIntTmp = raw_input("How many bytes (enter for 1 MB):")
if rangeIntTmp != '':
	rangeInt = int(rangeIntTmp)
	
targetFile = "/dev/null"
print "FULLPATH to target file"
print "be careful! overwrites existing files without warning!"
targetFileTmp = raw_input("(just enter for '/dev/null'): ")
if targetFileTmp != "":
	targetFile = targetFileTmp

fRandom = open("/dev/urandom", "r")
fTarget = open(targetFile, "w")

timerStart = time.time()

try:
	for i in range(rangeInt):
		# Do stuff with byte.
		byte = fRandom.read(1)
		fTarget.write(byte)
		# !DANGEROUS! Could interact with console!
		#print str(byte)
except Exception, e:
	print "Error: ", str(e)
finally:
	fRandom.close()
	fTarget.close()
	
print "########### fin"
print "duration: " + str(time.time() - timerStart)
