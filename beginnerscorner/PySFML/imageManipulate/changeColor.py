#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Include the PySFML extension
from PySFML import *
import time
import sys, os

# Create the main window
window = sf.RenderWindow(sf.VideoMode(800, 600), "PySFML test")

#window.SetBackgroundColor(sf.Color(0,0,0))

fps = sf.String("0")
fps.Move(400,0)
fpsCounter = 0
counterTime = time.time()


# Start the game loop
running = True

texture = sf.Image()
texture.LoadFromFile(os.path.dirname(sys.argv[0]) + "/nyan.png")

iSprite = sf.Sprite(texture)

bgColor = sf.Color(0,0,0)
Width  = iSprite.GetSize()[0]
Height = iSprite.GetSize()[1]
while running:
		
    fpsCounter +=1
    if time.time() -  counterTime >=1:
        fps.SetText(str(fpsCounter))
        fpsCounter = 0
        counterTime = time.time()
        
    event = sf.Event()
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False
        elif event.Type == sf.Event.KeyPressed:
            #http://www.sfml-dev.org/documentation/1.6/namespacesf_1_1Key.php
            if event.Key.Code == sf.Key.Q: #....
                #text.Move(-5,0)
                running = False
            elif event.Key.Code == sf.Key.E: #execute

                for iX in range(int(Width)):
                    for iY in range(int(Height)):
                    	Pixel = texture.GetPixel(iX, iY)
                    	Pixel.b = 255
                    	#Pixel.a = 255
                    	texture.SetPixel(iX, iY, Pixel)
                iSpryte = sf.Sprite(texture)
                    	
                
    
    window.Clear(bgColor)
    window.Draw(fps)
    window.Draw(iSprite)
    window.Display()
