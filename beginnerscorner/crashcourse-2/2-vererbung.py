#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Klassen Vererbung

# in Python werden Klassen seit python 2.7 sauber deklariert, in dem man sie 
# grundsätzlich von der Klasse object erben lässt.

# foo erbt seien Eigenschaften von der Superklasse object
class foo(object):
    def __init__(self):
        print "I am foo"
    
# jetzt lassen wir die Klasse b von der Klasse foo erben
class b(foo):
    def printme(self):
        print "and me too"

foobar = b()

#foobar.printme()



# Überschreiben von Methoden

class foo(object):
    def printme(self):
        print "I am foo"


class b(foo):
    def printme(self):
        print "I am b"

foobar = foo()
B = b()

foobar.printme()
# und jetzt die Überschriebene Methode
B.printme()

# Das wirft bei der Benutzung von Konstruktoren Probleme auf wie man 
# hier sehen kann:

class foo(object):
    def __init__(self):
        print "ich bin foo"

class b(foo):
    def __init__(self):
        print "ich bin b"

foobar = foo()
B = b()

# The Magic of super
# Denn man möchte bei einer abgeleiteten Klasse meistens auch 
# den Konstruktor der Elternklasse mit aufrufen
# deshalb gibt es super

class foo(object):
    def __init__(self):
        print "Ich bin foo"

class b(foo):
    def __init__(self):
        super(b, self).__init__()
        print "ich bin b"

foobar = foo()
B = b()

