#!/usr/bin/python

# Echo server program
import socket
import thread

HOST = 'localhost'  # Symbolic name meaning the local host
PORT = 9999         # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #erstellen Server
s.bind((HOST, PORT)) #server auf localhost, Port 50007 laufen lassen
s.listen(5) #Server maximal 5 Client akzeptieren lassen... warten...

allDatas = []

def handclient(conn,addr):#,allDatas):
    while 1:
        global allDatas
        data = conn.recv(4096)
        if not data: break
        #allDatas = allDatas + data + "\n"
        allDatas.append(data)
        if len(allDatas) > 5:
            #del allDatas[0]
            allDatas.pop(0)
        sendString = ""
        for item in allDatas:
            sendString = sendString + item + "\n"
        conn.send(sendString) #Daten von Server zu Client senden
        print data
        print addr
        print conn
    conn.close()


def starter():
    while 1:
        conn, addr = s.accept()
        thread.start_new(handclient,(conn,addr))#,allDatas))

starter()

s.close()
