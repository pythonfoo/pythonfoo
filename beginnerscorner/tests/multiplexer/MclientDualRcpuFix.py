#!/usr/bin/python
import socket
import sys
import select

def makeNumberFromCharCode(code):
    return (ord(code[0]) << 24) | (ord(code[1]) << 16) | (ord(code[2]) << 8) | ord(code[3])

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
noMessageCount = 0
try:
    s.connect((ip, port))
    keepRecieving = True
    while keepRecieving == True:
        #r, w, e=select([s],[],[s], 0)
        #print r,'|',w,'|',e
        nachricht = s.recv(1024)
        
        if nachricht == '\leave':
            keepRecieving = False
        elif nachricht:
            print 'recieved MESSAGE'
            keepRecieving = True
        elif nachricht == False:
            print 'recieved FALSE'
            keepRecieving = False
        elif nachricht == '':
            print 'EMPTY!'
            keepRecieving = False
        #elif nachricht
        #print makeNumberFromCharCode(nachricht)
        nachricht = nachricht.decode()
        print 'msg', nachricht.decode()
except socket.error:
    print 'yay'
    if e[0] in (errno.EWOULDBLOCK, errno.EAGAIN): # since this is a non-blocking socket..
        #return # no error
        print 'nofoo'
    else:
        # error
        print 'CLOSE error'
        socket.close()
finally:
    s.close()

