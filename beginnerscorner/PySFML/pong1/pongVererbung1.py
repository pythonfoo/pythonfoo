#!/var/bin/python

# This is an Example created for the Pythonfoo Workshop at the Chaosdorf
# in 2012 by Oerb

# Include the PySFML extension
from PySFML import *
import time

class windowmanager(object):
    def __init__(self,name):
        self._backgroundcolor = sf.Color.Blue
        self._drawlist = []
        self.winX = 800
        self.winY = 600
        self._window = sf.RenderWindow(sf.VideoMode(self.winX, self.winY), name)
        self._window.SetFramerateLimit(60)
        self._running = True
        self._fpsCounter = 0
        self._counterTime = time.time()
        self.fps = 0
        # testelement
        self.testlist = []
        self.testlist.append(sf.String("Hello SFML"))
        text2 = sf.String("Next")
        text2.SetPosition(0, 100)
        self.testlist.append(text2)
        
        

    def show(self):
        while self._running:
            self._drawlist = []
            # fps Kram im test
            fpsZahl = str(self._fpsCount())
            text3 = sf.String(fpsZahl)
            text3.SetPosition(0,200)
            for e in self.testlist:
                self._drawlist.append(e)
            self._drawlist.append(text3)
            # must have
            self._eventmanager()
            self._window.Clear(self._backgroundcolor)
            self._draw(self._drawlist)
            self._window.Display()

    def _draw(self, drawlist):
        # Draw Elements
        for drawelement in drawlist:
            self._window.Draw(drawelement)
            
    def _eventmanager(self):        
        event = sf.Event()
        while self._window.GetEvent(event):
            if event.Type == sf.Event.Closed:
                self._running = False

    def _fpsCount(self):
        self._fpsCounter +=1
        if time.time() - self._counterTime >=1:
            self.fps = self._fpsCounter
            self._fpsCounter = 0
            self._counterTime = time.time()
        return self.fps                    

# Definition der Elternklasse von PongObjekten, von der
# weitere Pongobjekte abgeleitet werden sollen.

class pongObj(object):
    def __init__(self):
        _xPosition
        _yPosition

    def _eventmanager(self,event):
        pass # ist eine Pseudoanweisung die nichts tut 


class pongBall(pongObj):
    def __init__(self, imagename, startx, starty):
        _xPosition = startx
        _yPosition = starty
    def _eventmanager(self,event):
        if event.Type == 10:
            _xPosition = event.MouseMove.X
            _yPosition = event.MouseMove.Y
            print "X: " + _xPosition + " Y: " + _yPosition             


# _Main Start
window = windowmanager("Window")
window.show()                                                       
