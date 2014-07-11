#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import your Stuff
# als erstes machen wir mal eine Datei foo.py, mit einer Klasse namens bar, die 
# wir dann in einem anderen Programm 
# benutzen wollen.

class bar(object):
    def __init__(self):
        self._text = "Ich bin bar aus foo oder auch foobar genannt!"
        self.endline = "---------------------------------------------------"
    def _printStuff(self, txt):
        print(txt)
        print(self.endline)

    def printText(self):
        print(self._text)
        print(self.endline)


# Jetzt erstellt man eine zweite Datei test.py, in der wir den neuen code importieren

import foo 

foobar = foo.bar()

foobar._printStuff("This is a Test")
foobar.printText()

# alternativ kann man auch

from foo import bar

# schreiben, wobei die Instanziierung dann so lauten müsste:

foobar = bar()

# eine weitere Alternative:

from foo import *

# hier wird wie bei "from foo import bar" importiert jedoch sollten noch mehr 
# klassen vorhanden sein, so würden diese mit importiert werden.

# Jetzt legen wir ein Unterverzeichnis namens testlib an
# und erstellen mit touch __init__.py eine leere Datei in diesem Verzeichnis
# Die Datei ist dafür verantwortlich, dass Python mit import in diesem Verzeichnis sucht.
# danach verschieben wir die date foo.py in den neuen Unterordner.
# der Import sieht daraufhin wie folgt aus:

import testlib.foo

# und die Instanziierung 

foobar = testlib.foo.bar()

# jetzt noch ein klein wenig magic...
# wir schreiben in die datei foo.py unter die Klasse noch ein wenig normalen code
# und führen den import wie oben noch einmal aus

# unter der classe:

foobar = bar()
i=0
while i < 10:
    foobar.printText()
    i += 1

# wie man sehen kann, wird der code beim instanziieren automatisch mit ausgeführt
# das will man eigentlich nicht. Aus diesem Grund benutzt man main um Testcode 
# in seine Libery zu implementieren. Dieser wird nur dann ausgeführt, 
# wenn die Datei direkt ausgeführt wird. Ansonsten werden nur die 
# betreffenden Elemente importiert.

class main(object):
    def __init__(self):
        foobar = bar()
        i = 0
        while i < 10: 
            foobar.printText()
            i += 1

if __name__== "__main__":
    start = main()
# schau __all__ das muss auf Modulebene implementiert werden um festzulegen,
# was man nicht importieren soll
