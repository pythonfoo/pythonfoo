#!/var/bin/python

# Include the PySFML extension
from PySFML import *
import time

# Create the main window
window = sf.RenderWindow(sf.VideoMode(800, 600), "PySFML test")
#window.SetFramerateLimit(60)

# Create a graphical string to display
text = sf.String("Hello SFML")

fps = sf.String("0")
fps.Move(400,0)
fpsCounter = 0
counterTime = time.time()


# Start the game loop
running = True

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
            if event.Key.Code == 291: #left
                text.Move(-5,0)
            elif event.Key.Code == 292: #right
                text.Move(5,0)
            elif event.Key.Code == 293: #up
                text.Move(0,-5)
            elif event.Key.Code == 294: #down
                text.Move(0,5)
            elif event.Key.Code == sf.Key.Q: #lefrrot q
                text.Rotate(-5)
            elif event.Key.Code == sf.Key.E: #rightrot e
                text.Rotate(+5)
            print event.Key.Code

    # Draw the text, and update the window
    window.Clear()
    window.Draw(fps)
    window.Draw(text)
    window.Display()
    
