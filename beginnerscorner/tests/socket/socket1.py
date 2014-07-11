#!/usr/bin/python
import socket
import sys

#print sys.argv[1]
# senden einer Datei mittels Socket

address = "localhost"
port = 9999
filename = "test.txt"

datei = open(filename,'r')
data = datei.read()
datei.close()

#data = "test"

s1 = socket.socket()
s1.connect((address, port))


s1.send(data)
print s1.recv(1024)
s1.close()


