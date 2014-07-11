#!/usr/bin/python
import sys
from urllib import urlopen
if len(sys.argv) > 1:
	print urlopen(sys.argv[1]).read()
else:
	print 'give me a page to show!'
