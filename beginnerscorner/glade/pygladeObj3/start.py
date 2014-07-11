#!/usr/bin/python
import sys
import gtk
import gtk.glade
import gnome.ui

""" In this Aplication ist Glade used in Mode GtkBuilder, 2.16 """

class mainwindowGTK:
    """ This is the main Window of the aplication """
   
    def __init__(self):
	# Window Open 
        self.gladefile = "main.glade"
	self.builder = gtk.Builder()
	self.builder.add_from_file(self.gladefile)
	self.builder.connect_signals(self)
	self.builder.get_object("window1").show()

    def run(self):
	try:
	    gtk.main()
	except KeyboardInterrupt:
	    pass

    def quit(self):
        gtk.main_quit()	


    def btnInfo_clicked(self, *args):
	# aendert den Text im Label1 
	hilfe = self.builder.get_object('label1')
        hilfe.set_label('Jo')

	
    def on_window1_delete_event(self, *args):
	self.quit()	

if __name__ == "__main__":
    """ instantiate Class/Program an GTK """
    mawi = mainwindowGTK()
    mawi.run()
