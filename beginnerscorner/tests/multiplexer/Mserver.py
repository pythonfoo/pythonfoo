#!/usr/bin/python
import socket
import select
import sys

print """Beispiel fuer einen einfachen multiplexenden Server mittels sockets"""

if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = 10007

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
                if nachricht == "\exit":
                    print("+++ " + format(ip) + " exits")
                elif nachricht:
                    #print("[(0)] [1]".format(ip, nachricht.decode()))
                    print ip + " " + nachricht.decode()
                else:
                    print("+++ Verbindung zu [0] beendet".format(ip))

                sock.close()
                clients.remove(sock)

finally:
    for c in clients:
        c.close()
    server.close()

