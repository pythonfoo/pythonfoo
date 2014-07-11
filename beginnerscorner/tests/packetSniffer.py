#!/usr/bin/env python 
import socket, sys 
from optparse import OptionParser
def scan_server(address, port): 
	s = socket.socket() 
	print "Attempting to connect to %s on port %s." %(address, port) 
	try: 
		s.connect((address, port)) 
		print "Connected to server %s on port %s." %(address, port) 
		return True 
	except socket.error, e: 
		print "Connecting to %s on port %s failed with the following error: %s" %(address, port, e) 
		return False 

if __name__ == '__main__': 
#if True == True:
	print 'go:'
	parser = OptionParser() 
	parser.add_option("-a", "--address", dest="address", default="localhost", help="ADDRESS for server", metavar="ADDRESS") 
	parser.add_option("-p", "--port", dest="port", help="PORT for server", metavar="PORT") 
	(options, args) = parser.parse_args() 
	if options.port == 'all': 
		print 'checking all ports...' 
		for x in range(1,6 5536): 
			print 'checking port %s on %s' %(x, options.address) 
			check = scan_server(options.address, x) 
			print 'scan_server returned %s' %(check) 
	else:
		options.port = int(options.port) 
		print 'options: %s, args: %s' %(options, args) 
		check = scan_server(options.address, options.port) 
		print 'scan_server returned %s' %(check) 
		sys.exit(not check) 
