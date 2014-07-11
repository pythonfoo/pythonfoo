#!/usr/bin/python

import socket
import select
import sys
import urllib

port = 8080

#172.22.26.158 GET /favicon.ico HTTP/1.1
#Host: 172.22.26.127
#User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1
#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
#Accept-Language: de-de,de;q=0.8,en-us;q=0.5,en;q=0.3
#Accept-Encoding: gzip, deflate
#Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
#Connection: keep-alive


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", port))
server.listen(1)
clients = []
try:
    while True:
        lesen, schreiben, oob = select.select([server] + clients, [], [])

        for sock in lesen:
            if sock is server:
                client, addr = server.accept()
                clients.append(client)
                print("+++ Client (0) verbunden", format(addr[0]))
            else:
                nachricht = sock.recv(1024)
                ip = sock.getpeername()[0]
                # first commands!
                if nachricht == '\exit':
                    print("+++ " + format(ip) + " exits")
                elif nachricht:
                    #print("[(0)] [1]".format(ip, nachricht.decode()))
					print ip + " " + nachricht#.decode()
					f = open('header.html', "r")
					text = f.read()
					f.close()
					sock.send(text)
					web = urllib.urlopen("http://blog.fefe.de")
					# Read from the object, storing the page's contents in 's'.
					webString = web.read()
					web.close()
					webString = webString.replace("Fefe","bison")
					sock.send(webString)
                else:
                    print("+++ Verbindung zu [0] beendet".format(ip))

                sock.close()
                clients.remove(sock)
#http://172.22.26.127/google
#GET /google HTTP/1.1


finally:
    for c in clients:
        c.close()
    server.close()

