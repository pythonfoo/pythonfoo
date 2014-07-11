#!/usr/bin/python
import time
import thread
import threading
import socket



# config
host = "" #socket.gethostname()
port = 1723
timeOut = 60

printConnected = True
printRecieved = False
printError = True
printInfo = True

portList =  {
			'a':['test', 9999],
			'b':['PPTP', 1723],
			'c':['http', 80]
			}

# the main PRINT function!
def printEx(txt, printType = ''):
	timeString = time.strftime("%d.%m.%Y %H:%M:%S|")
	if printType == 'connected' and printConnected == True:
		print timeString, txt
	elif printType == 'recieved' and printRecieved == True:
		print timeString, txt
	if printType == 'error' and printError == True:
		print timeString, txt
	elif printType == 'info' and printInfo == True:
		print timeString, txt
	elif printType == '':
		print timeString, txt

# show default ports to select
for key in sorted(portList.iterkeys()):
	print key, ')', portList[key][0], '(', portList[key][1], ')'

# get the port to listen on
tmp = raw_input('Enter port (def.'+ str(port) +'):')
if tmp == '':
	# on empty entry do NOTHING at all and keep predefined value
	pass
elif tmp.isdigit():
	# if the entry is digit, it "MUST" be a port
	port = int(tmp)
else:
	# anything else shoud be the selected port from list, so we read it from there 
	port = portList[tmp][1]

printEx( 'selected port:'+ str(port), 'info' )


s = socket.socket()		# inizialise socket
s.settimeout(timeOut)	# general time-out for "s.accept()"
s.bind((host, port))
printEx( 'port bounded', 'info' )

s.listen(1)
printEx( 'started listening', 'info' )


def comlink(tId, con, addr):
	printEx( str(tId) +' enters thread for: '+ str(addr), 'info' )
	try:
		trips = 0
		while True:
			data = con.recv(1024)
					
			if not data: 
				con.close()
				break
		
			printEx( "%s)[%s] %s" % (tId, addr[0], data), 'recieved')
			
			if trips == 0:
				con.sendall('im  alive' + "\r\n")
			else:
				con.sendall('still alive' + "\r\n")
				
			trips += 1
	except Exception, e:
		printEx( 'Error for:' + str( addr[0] ) + 'Message:' + str( e ), 'error')
		con.close()
	printEx( str(tId) + ' has exited for:'+  str(addr), 'info' )
	

keepTrying = True
connectionIdCounter = 0

while keepTrying:
	try:
		con, addr = s.accept()
		printEx( "connection from [%s]" % (addr[0]), 'connected' )
		thread.start_new_thread(comlink, (connectionIdCounter, con, addr))
		connectionIdCounter += 1
	except socket.timeout:
		# on timeout do nothing!
		printEx( 'TimeOut', 'info' )
	except Exception, e:
		# exit on every other error!
		keepTrying = False
		printEx( 'Socket Error:'+ str( e ), 'error' )
try:
	printEx( 'Trying to close socket...' )
	s.close()
	printEx( 'socket closed' )
except Exception, e:
	printEx( 'error during socket close:'+ str(e), 'error' )


