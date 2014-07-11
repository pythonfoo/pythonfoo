#!/usr/bin/python
import socket
import sys

print "Client zum multiplexenden Server - Reciever"
print "!BUG! Bei Server-Fail, CPU=100%"
print "BE CAREFUL WITH THAT!"

# len prueft die Anzahl der Elemente im array
if len(sys.argv) > 1:
    ip = sys.argv[1]
else:
    ip = "localhost"

if len(sys.argv) > 2:
    port = int(sys.argv[2])
else:
    port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((ip, port))
    keepRecieving = True
    while keepRecieving == True:
        nachricht = s.recv(1024)
        nachricht = nachricht.decode()
        
        if nachricht == '\leave':
            keepRecieving = False
        elif nachricht:
            keepRecieving = True
        #else:
        #    keepRecieving = False
        print nachricht.decode()
finally:
    s.close()

