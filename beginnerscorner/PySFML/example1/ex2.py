#!/var/bin/python

# Include the PySFML extension
from PySFML import *
import time

# Create the main window
window = sf.RenderWindow(sf.VideoMode(800, 600), "PySFML mover ;)")

# Create a graphical string to display
textX = 0
textY = 0
text = sf.String("Hello SFML")
frameRate = sf.String("0")
frameRate.Move(650,5)
# Start the game loop
running = True

fpsTimer = time.time()
fpsCounter = 0
while running:
    event = sf.Event()
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False
        elif event.Type == sf.Event.KeyPressed:
            print event.Key.Code
            if event.Key.Code == 291: #left
                text.Move(-5,0)
            elif event.Key.Code == 292: #right
                text.Move(5,0)
            elif event.Key.Code == 293: #up
                text.Move(0,-5)
            elif event.Key.Code == 294: #down
                text.Move(0,5)

    if (time.time() - fpsTimer) >= 1:
        frameRate.SetText(str(fpsCounter) + ' fps')
        fpsTimer = time.time()
        fpsCounter = 0
    # Draw the text, and update the window
    window.Clear()
    window.Draw(text)
    window.Draw(frameRate)
    window.Display()
    fpsCounter += 1
