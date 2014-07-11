#!/usr/bin/python

from Xlib import x, display

d = display.Display()
s = d.screen()
root = s.root
root.warp_pointer(300,300)
d.sync()
