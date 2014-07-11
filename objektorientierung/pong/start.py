#!/var/bin/python

############# Pong SFML WindowManager ##############################

# This is an Example created for the Pythonfoo Workshop at Chaosdorf
# Chaosdorf.de
# in 2012 by Oerb
#
# Include the PySFML extension

from lib import game

class main(object):
    def __init__(self):
        gamevar = game.pongGame()
        
if __name__== "__main__":
    start = main()
