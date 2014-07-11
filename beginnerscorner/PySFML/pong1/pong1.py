#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Include the PySFML extension
from PySFML import *
import time
# Create the main window
window = sf.RenderWindow(sf.VideoMode(800, 700), "PySFML test")

# Counter for show FPS
fpsCounter = 0
counterTime = time.time()


window.SetFramerateLimit(60)

running = True

texture = sf.Image()
texture.LoadFromFile("test.png")
balltex = sf.Image()
balltex.LoadFromFile("ball.png")
ballstring = sf.Sprite(balltex)
balkenstring = sf.Sprite(texture)
# Start the game loop
running = True
x = 0

class txtBox(object):
    def __init__(self, txt, x, y):
        self._xPosition = x
        self._yPosition = y
        self._txt = txt
        self._sftxt = sf.String(self._txt)
        self._sftxt.Move(x, y)
        self._sftxt.SetText(self._txt)
        self._visible = True

    @property
    def xPosition(self):
        return self._xPosition
    @xPosition.setter
    def xPosition(self, value):
        self._xPosition = value

    @property
    def yPosition(self):
        return self._yPosition
    @yPosition.setter
    def yPosition(self, value):
        self._yPosition = value

    @property
    def txt(self):
        return self._txt
    @txt.setter
    def txt(self, value):
        self._txt = value
        self._sftxt.SetText(value)

    @property
    def visible(self):
        return self._visible
    @visible.setter
    def visible(self,value):
        self._visible = value 

    def Show(self):
        window.Draw(self._sftxt)


class BallObj(object):
    def __init__(self, x, y, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self._outofwindow = False
        self._reversecount = 0
    @property
    def outofwindow(self):
        return self._outofwindow

    @property
    def revcount(self):
        return str(self._reversecount)
    def newgame(self):
        self._reversecount = 0
    def advance(self):
        self.x += self.dx
        self.y += self.dy
        if self.y >= 575 or self.y <=0:
            self.dy = -self.dy
        if self.x >= 775:
            self.dx = -self.dx
        if self.x <=90:  # Bug if here <= 0 not nice but funktional
            self._outofwindow = True

    def kontakt(self, spin):
        self.dx = -self.dx 
        self.dy = self.dy + spin
        if not gameover:
            self._reversecount += 1

class BalkenObj(object):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed   
        self.yOld = y
        self._spin = 1
        self.info = 0
        self._usecount = 0
        self.time = time.time()
    @property
    def outofwindow(self):
        return self._outofwindow
    @property
    def spin(self):
        return self._spin    

    def SetPosition(self, xp, yp): 
        if yp >= 500:
            self.y = 500      
        else:
            self.y = yp
        # Spin Element
        # Bug - Schnelle Bewegung gibt viele Punkte.... (Zeipruefung als Loesung?)
        if time.time() - self.time <= 0.02:
            if self.yOld - self.y < -1:
                self._spin = 2
            elif self.yOld - self.y > 1:
                self._spin = -2
            else:
                self._spin = 0
            self.info = "1 " + str(time.time() - self.time)
            self.yOld = self.y
        else:
            self._spin = 0
            self.info = 0
        self.time = time.time()
        
# Menue Bottom
line1 = sf.Shape.Line(0,600,800,600,2,sf.Color.Yellow)
# Game Messages
headertxt = txtBox("PONG",500, 600)
fpstxt = txtBox("FPS: 60 Rev: 0",200,600)
helpmsg = txtBox("Keys: n = New Game, h = Help, q or ESC = quit",50,650)
helpmsg.visible = False
# Runnig
gameover = True
nogame = True



while running:
    fpsCounter +=1
    if time.time() -  counterTime >=1:
        fpstxt.txt = "FPS: " + str(fpsCounter) 
        fpsCounter = 0
        counterTime = time.time()

    event = sf.Event()
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False
        
        elif event.Type == sf.Event.KeyPressed:
            if event.Key.Code == 104: #h for Help
                if helpmsg.visible:
                    helpmsg.visible = False
                else:
                    helpmsg.visible = True
        # Mouse Movement       
        elif event.Type == 10:
            if not gameover:
                x = event.MouseMove.X
                y = event.MouseMove.Y
                balken.SetPosition(x,y)

        elif event.Key.Code == 113: #Q for Quit
                running = False
        elif event.Key.Code == 256: #ESC for Quit
                running = False
        elif event.Key.Code == 110: #N for Next Game
            if gameover:    
                gameover = False
                nogame = False
                balken = BalkenObj(0,0,10) # Startlocation Balken + KeySpeed
                ball = BallObj(700, 200) # Startlocation Ball
                ball.dy = 1
                ball.dx = 4
                ball.newgame()
#        print event.Key.Code
# helps to find the Key-Code       
        
    if not gameover:
        ball.advance()
        if ball.outofwindow: 
            gameover = True
            count = ball.revcount


        # Ball beruehrt Balken
        if ball.x <= 100:
            if ball.y >= balken.y and ball.y <= balken.y + 100:
                ball.kontakt(balken.spin)
                print "Spin: " + str(balken.spin)
                print "Spininfo: " + str(balken.info)
        # Ball movement
        ballstring.SetPosition(ball.x, ball.y)
        # Balken movement
        balkenstring.SetPosition(balken.x, balken.y)
    # Draw the text, and update the window
    window.Clear(sf.Color.Blue)
    if helpmsg.visible:
        helpmsg.Show()
        
    headertxt.Show()
    # SFML Polygon Test
    window.Draw(line1)    

    if not gameover:
        window.Draw(ballstring)
        window.Draw(balkenstring)
    if gameover and not nogame:
        fpstxt.txt = " Game Over - Rev: " + count
    fpstxt.Show()       
        
        
    window.Display()  


