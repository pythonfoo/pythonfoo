#!/usr/bin/python

# Whats this?
# I tried to write a piece of code that executes my changes in a file automatically.
# Worked great with Python 2.7.
# BUT it did not work with Python 2.6
# I Wrote it under Ubuntu 12.04 but have Debian 6 on my Laptop.
# FOOOOO!!1!
# So I used "clear; python cc.py" for my Presentation instead -.-

import os, time, subprocess
#http://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/

def clear():
	# clear the console
	#os.environ.clear()
	#os.system('CLS') # for windows!
	os.system('clear')

clear()

print os.path.basename(__file__)
print 'PLEASE STAND BY FOR CHANGES'

filesDates = {}
while True:
	dirList = os.listdir(".")
	for fname in dirList:
		#print fname
		#print "last modified: %s" % time.ctime(os.path.getmtime(fname))
		#print "created: %s" % time.ctime(os.path.getctime(fname))
		
		# ignore myself!
		if fname != os.path.basename(__file__):
			mtime = os.path.getmtime(fname)
			if not fname in filesDates:
				# we are NOT interested in created files
				# and on the first run just add all files with theyr dates
				filesDates[fname] = {'mtime':mtime}
			elif filesDates[fname]['mtime'] != mtime:
				clear()
				
				# remember the new time
				filesDates[fname]['mtime'] = mtime
				res = 'nothing...'
				try:
					res = subprocess.check_output('python '+fname, shell=True) #  stderr=subprocess.STDOUT,
				except Exception as e:
					res = 'ERROR: ' + str(e)
				
				# get the longest "string" in the output header
				maxLen = len(str(mtime))
				if len(fname) > maxLen:
					maxLen = len(fname)
				
				# remember to add the left and right space AND # to the calculation (+4 chars)
				print (maxLen+4)*'#' # draw topline
				print '#', 'OUTPUT'.center(maxLen, ' '), '#'
				print '#', fname.center(maxLen, ' '), '#'
				print '#', str(mtime).center(maxLen, ' '), '#'
				print (maxLen+4)*'#' # draw bottomline
				print res

	time.sleep(1.1)
