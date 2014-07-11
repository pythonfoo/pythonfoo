#!/usr/bin/python
import socket
import sys

print "Client zum multiplexenden Server - Sender"

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
    while True:
        nachricht = raw_input("Nachricht: ")       
        s.send(unicode(nachricht, "utf-8"))
finally:
    s.close()

