#!/usr/bin/python
#from:
#http://www.python-forum.de/viewtopic.php?p=36000&

#from Tkinter import *


# Echo client program
import socket

class chat:
    def __init__(self):     
        HOST = 'localhost'    # The remote host
        PORT = 9999         # The same port as used by the server
        self.chatter = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket-Obj erstellen
        self.chatter.connect((HOST, PORT)) #zu server verbinden
        
    def senden(self,inhalt):
        self.chatter.send(inhalt) #Daten zu server senden
        
    def empfangen(self):
        self.data = self.chatter.recv(4096) #Daten von Server empfangen
        self.chatter.close()
        return self.data
        
def inserttext(event):
    print "-------"
    ch.senden(EntryEing.get())

    stri = ch.empfangen()
    print stri

    print "-----stri-----" 

    text.insert("end",stri + "\n")
    text.see(END)
        

while True:
    ch = chat()
    ch.senden(raw_input("Nachricht: "))
    print ch.empfangen()

exit("done")

#unused code behind....

#root = Tk()
ch = chat()


#scroll = Scrollbar(root)
#scroll.place(x=200,y= 0,width=200)

#text = Text(root,yscrollcommand=scroll.set)
#text.place(x=0,y=10,width=200,height=250)

#scroll.config(command=text.yview)

#EntryEing  = Entry(root)
#EntryEing.place(x=0,y= 280,width=200)
#EntryEing.bind("<Return>",inserttext)

#root.minsize(230,300)
mainloop()
