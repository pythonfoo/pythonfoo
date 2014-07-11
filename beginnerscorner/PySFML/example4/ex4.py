#!/var/bin/python

# Include the PySFML extension
from PySFML import *

# Create the main window
window = sf.RenderWindow(sf.VideoMode(800, 600), "PySFML test")

# Create a graphical string to display
text = sf.String("BMP SFML")


window.SetFramerateLimit(60)

running = True

texture = sf.Image()
texture.LoadFromFile("test.png")
sprite = sf.Sprite(texture)
# Start the game loop
running = True
while running:
    event = sf.Event()
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False
    

    # Draw the text, and update the window
    window.Clear(sf.Color.Blue)
    window.Draw(sprite)
    window.Draw(text)
    window.Display()
