#!/usr/bin/python
import socket

host = ""#socket.gethostname()
port = 9999
s = socket.socket()
s.bind((host, port))

s.listen(1)

try: 
    while True: 
        komm, addr = s.accept() 
        while True: 
            data = komm.recv(1024)

            if not data: 
                komm.close() 
                break

            print "[%s] %s" % (addr[0], data) 
            
            #nachricht = raw_input("Antwort: ") 
            #komm.send(nachricht)
            datei = open("test.txt",'r')
            komm.send(datei.read()) 
finally: 
    s.close()

