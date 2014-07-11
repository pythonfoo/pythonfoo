#!/usr/bin/python
import socket
import threading
SIZE =4
class client(threading.Thread):
    def __init__(self,c):
        threading.Thread.__init__(self)
        self.conn = c
        self.stopIt = False

    def mrecv(self):
        data = self.conn.recv(SIZE)
        self.conn.send('OK')
        return self.conn.recv(int(data))

    def run(self):
        while not self.stopIt:
            msg = self.mrecv()
            print 'recieved-> ',msg

soc1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc1.connect(('127.0.0.1',5432))
soc1.send('WILL SEND') # telling server we will send data from here

soc2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc2.connect(('127.0.0.1',5432))
soc2.send('WILL RECV') # telling server we will recieve data from here

def msend(conn,msg):
    if len(msg)<=999 and len(msg)>0:
        conn.send(str(len(msg)))
        if conn.recv(2) == 'OK':
            conn.send(msg)
    else:
        conn.send(str(999))
        if conn.recv(2) == 'OK':
            conn.send(msg[:999])
            msend(conn,msg[1000:]) # calling recursive
thr = client(soc2)
thr.start()
try:
    while 1:
        msend(soc1,raw_input())
except:
    print 'closing'
thr.stopIt=True
msend(soc1,'bye!!') # for stoping the thread
thr.conn.close()
soc1.close()
soc2.close()
