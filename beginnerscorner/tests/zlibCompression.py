#!/usr/bin/python
import sys
import zlib

def ByteToHex( byteStr ):
    #Convert a byte string to it's hex string representation e.g. for output.
	ret = ''.join( [ "%02X" % ord( x ) for x in byteStr ] ).strip()
	return ret.lower()

if len(sys.argv) == 0:
	print '1st Parameter: string to compress'
	print '2nd Parameter (optional) Compression level 0-9'

else:

	if len(sys.argv) > 1:
		cstring = sys.argv[1]
	
	lvl = 9 # fastes level, 9 slowest, best compression
	if  len(sys.argv) > 2:
		lvl = int(sys.argv[2])
	
	compressed = zlib.compress(cstring, lvl)
	hexCompressed = ByteToHex(compressed)
	print 'UnCompressed: ' + str(len(cstring))
	print 'Compressed: ' + str(len(compressed))
	print 'Compressed Hex: ' + str(len(hexCompressed))

