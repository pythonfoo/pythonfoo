#!/var/bin/python

# This is an Example created for the Pythonfoo Workshop at the Chaosdorf
# in 2012 by Oerb

# Include the PySFML extension
from PySFML import *
import time

class windowmanager(object):
    def __init__(self,name):
        self._backgroundcolor = sf.Color.Blue
        self.winX = 800
        self.winY = 600
        self._drawlist = []
        self._window = sf.RenderWindow(sf.VideoMode(self.winX, self.winY), name)
        self._window.SetFramerateLimit(60)
        self._running = True
        self._fpsCounter = 0
        self._counterTime = time.time()
        self.fps = 0
        self.fpsBox = pongTxtBox("0")
        self.fpsBox.xPos = 0
        self.fpsBox.yPos = 50
                                        
       
        # PongObjekt Indizierer
        self._PongObjIndexer = 0
        self._PongObjDict = {}       

        self.registerPongObj(self.fpsBox)


    def show(self):
        while self._running:
            self.fpsZahl = str(self._fpsCount())
            self._PongObjDict[0].text = self.fpsZahl
            self._eventmanager()
            self._window.Clear(self._backgroundcolor)
            self._draw()
            self._window.Display()

    # Zeichnen der SMFL Objekte
    def _draw(self):
        # registerierte Objekte in Drawlist uebernehmen
        # da sie fuer jeden show neu erzeugt wird
        for key in self._PongObjDict:
            if self._PongObjDict[key].visible:
                self._window.Draw(self._PongObjDict[key].show())
            
    def _eventmanager(self):        
        event = sf.Event()
        while self._window.GetEvent(event):
            if event.Type == sf.Event.Closed:
                self._running = False
            elif event.Key.Code == 113: #Q for Quit
                self._running = False
            elif event.Key.Code == 256: #ESC for Quit
                self._running = False
            # sending eventinfo to PongObjekts for manipulations   
            for key in self._PongObjDict:
                self._PongObjDict[key].eventmanager(event)

    def _fpsCount(self):
        self._fpsCounter +=1
        if time.time() - self._counterTime >=1:
            self.fps = self._fpsCounter
            self._fpsCounter = 0
            self._counterTime = time.time()
        return self.fps                    
    
    # when PongObj ist initialized it must be registered here
    # so that it will be shown when visible = True
    def registerPongObj(self, pongObj):
        self._PongObjDict[self._PongObjIndexer] = pongObj
        #return self._PongObjIndexer
        self._PongObjIndexer += 1
        return self._PongObjIndexer    

# Definition der Elternklasse von PongObjekten, von der
# weitere Pongobjekte abgeleitet werden sollen.
class pongObj(object):
    def __init__(self, PongObjTyp):
        self._xPosition = 0
        self._yPosition = 0
        self._PongObjTyp = PongObjTyp
        self._visible = True

    @property
    def xPos(self):
        return self._xPosition
    @xPos.setter
    def xPos(self, value):
        self._xPosition = value

    @property
    def yPos(self):
        return self._yPosition
    @yPos.setter
    def yPos(self, value):
        self._yPosition = value

    @property
    def objID(self):
        return self._PongObjID

    @property
    def PongObjTyp(self):
        return self._PongObjTyp

    @property
    def visible(self):
        return self._visible
    @visible.setter
    def visible(self, value):
        self._visible = value

    def eventmanager(self,event):
        pass # ist eine Pseudoanweisung die nichts tut 

    def show(self):
        pass

# Nachfolgend PongObjekt Kind-Klassen
class pongBall(pongObj):
    def __init__(self, imagename):
        super(pongBall,self).__init__("Ball") # fuer Klassenvererbung erf.
        self._window = windowmanager("Window")
        self._imagename = imagename
        self._dx = 0 
        self._dy = 0
        self._outofwindow = False
        self._reversecount = 0
        self._gameover = True
        self._visible = False
        self._Points = 0
        self._spin = 0
        self._Balken1 = pongBalken("test.png")
        self._Balken1.visible = False
        self._window.registerPongObj(self._Balken1)
        self._window.registerPongObj(self)
        self._window.show()
    

    @property
    def outofwindow(self):
        return self._outofwindow

    @property
    def revcount(self):
        return str(self._reversecount)

    def _newgame(self):
        self._gameover = False
        self._visible = True
        self._outofwindow = False
        self._Balken1.visible = True
        self.xPos = 700
        self.yPos = 200
        self._dy = 1
        self._dx = -4
        self._reversecount = 0
#        print "NewGame"

    def advance(self):
        if not self._gameover:
            self._xPosition += self._dx
            self._yPosition += self._dy
            if self.yPos >= 575 or self.yPos <= 0:
                self._dy = -self._dy
            if self._xPosition >= 775:
                self._dx = -self._dx                                  
            if self._xPosition <=90:  # Bug if here <= 0 not nice but funktional
                self._outofwindow = True
            if self._xPosition <= 100:
                if self._yPosition >= self._Balken1.yPos and self._yPosition <= self._Balken1.yPos + 100:
                    self._kontakt(self._spin)

    def _kontakt(self, spin):
        self._dx = -self._dx
        self._dy = self._dy + spin
        if not self._gameover:
            self._reversecount += 1

    def _setGameOver(self):
        self._gameover = True
        self.visible = False
        self._Balken1.visible = False
        self._Points = self.revcount

    def eventmanager(self,event):
        if event.Key.Code == 110: # N for new Game
            if self._gameover:
                self._newgame()
                       

    def show(self):
        if not self._gameover:
            self.advance()
            if self._outofwindow:
                self._setGameOver()        
        self._texture = sf.Image()
        self._texture.LoadFromFile(self._imagename)
        self._sprite = sf.Sprite(self._texture)
        self._sprite.SetPosition(self._xPosition,self._yPosition)
        return self._sprite

# der Schlaeger/Balken 
class pongBalken(pongObj):
    def __init__(self,imagename):
        super(pongBalken,self).__init__("Balken") # fuer Klassenvererbung erf.
        self._imagename = imagename

    @property
    def yPos(self):
        return self._yPosition
    @yPos.setter
    def yPos(self, value):
        if value >= 500:
            self._yPosition = 500
        else:
            self._yPosition = value

    def eventmanager(self,event):
        if event.Type == 10:
            self._xPosition = 0 #event.MouseMove.X
            self._yPosition = event.MouseMove.Y

    def show(self):
        self._texture = sf.Image()
        self._texture.LoadFromFile(self._imagename)
        self._sprite = sf.Sprite(self._texture)
        self._sprite.SetPosition(self._xPosition,self._yPosition)
        return self._sprite

# Einen Text anzeigen
class pongTxtBox(pongObj):
    def __init__(self, text):
        super(pongTxtBox, self).__init__("TxtBox") # fuer Klassenvererbung erf.
        self._text = text
        
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, value):
        self._text = value
        
    def eventmanager(self,event):
        pass
    def show(self):
        self._sftxt = sf.String(self._text)
        self._sftxt.SetPosition(self._xPosition, self._yPosition)
        return self._sftxt

# Klasse fuer den Hauptprogrammteil
class main(object):
    def __init__(self):
        # damit das Spiel startet muss ein Ball initialisiert werden
        Ball = pongBall("ball.png")
#        Ball.xPos = 200
#        Ball.yPos = 200

# _Main Start
# wird nur ausgefuehrt bei direktem Probrammaufruf nicht bei Moduleinbindung
if __name__ == "__main__":
            start = main()
                                                          
