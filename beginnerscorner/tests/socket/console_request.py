#!/usr/bin/python
import socket               # Import socket module

s = socket.socket()

address = raw_input("Enter Server: ")
port = int(raw_input("Enter Port: "))

while True:
	try:
		s.connect((address, port))
		print "Connected to server %s on port %s." %(address, port)
		send = 0
		while True:
			msg = raw_input("command: ")
			send += 1
			s.send(msg)
			print send
			print s.recv(1024)
			
		s.close()           
	except socket.error, e: 
		print "Connecting to %s on port %s failed with the following error: %s" %(address, port, e)
		cmd = raw_input("enter to continue, q to abort...")
		if cmd == "q":
			exit('aborted')
		#return False 
