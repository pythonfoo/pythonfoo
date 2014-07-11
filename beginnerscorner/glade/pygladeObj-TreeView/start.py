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
	self.window1 = self.builder.get_object("window1")
	self.window1.show()

    def run(self):
	try:
	    gtk.main()
	except KeyboardInterrupt:
	    pass

    def quit(self):
        gtk.main_quit()	


    def btnInfo_clicked(self, *args):
	# Ueberschriften Container instantiieren
	self.idColumn = gtk.TreeViewColumn('ID')
	self.nameColumn = gtk.TreeViewColumn('Name')
	self.vornameColumn = gtk.TreeViewColumn('Vorname')

	# Ueberschriften Container beschriften
	self.idColumn.Title = "ID"
	self.nameColumn.Title = "Name"
	self.vornameColumn.Title = "Vorname"

	# instantiiert einen CellRenderer um die Daten Anzuzeigen
	cell0 = gtk.CellRendererText()
	cell1 = gtk.CellRendererText()
	cell2 = gtk.CellRendererText()

	# Cells in die Columns packen und Daten anzeigen
	self.idColumn.pack_start(cell0, True)
	self.nameColumn.pack_start(cell1, True)
	self.vornameColumn.pack_start(cell2, True)	

	self.idColumn.set_attributes(cell0, text=0)
	self.nameColumn.set_attributes(cell1, text=1)
	self.vornameColumn.set_attributes(cell2, text=2)

	# treeview1 aus dem Glade.Gtk objekt Builder instantiieren
	self.treeview1 = self.builder.get_object('treeview1')

	# Ueberschriften Container dem TreeView1 Anfuegen
	self.treeview1.append_column(self.idColumn)
	self.treeview1.append_column(self.nameColumn)
	self.treeview1.append_column(self.vornameColumn)        

	# gtk Liststore instantiieren, der die Daten uebernehmen soll
	self.listStore1 = gtk.ListStore(int, str, str)
	
	# Daten in den Liststore geben
	self.listStore1.append([0,"Leppin","Bjoern"])
	self.listStore1.append([1,"Pollmeier","Klaus"])
	
	# ListStore in TreeView anzeigen
	self.treeview1.set_model(self.listStore1)

    def on_window1_delete_event(self, *args):
	self.quit()	

if __name__ == "__main__":
    """ instantiate Class/Program an GTK """
    mawi = mainwindowGTK()
    mawi.run()
