#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exploring Modules

import sys

# dir() shows what a Module contains
for element in  dir(sys):
    print element

# Getting Help 

help(sys)

# Getting Help on Method

help(ses.flags)


# Using Documentation
print range.__doc__

# und wenn garnichts mehr geht man aber schon nen guter 
# Pyhtoncoder ist helfen nur noch die sourcen aber 
# dafür müssen diese natürlich mitinstalliert sein
import copy
print copy.__file__

# Kommentare und Hilfe in seine Objekte zu bekommen ist recht einfach. Einfach
# direkt hinter den Klassennamen oder hinter den Methodennamen in
# Kommentarzeichen meistens so """ Kommentartext """ schreiben

class beispiel(object):
    """ dies ist ein Besipielkommentar für die Klasse """

    def doit(self):
        """ das ist jetzt der Hilfetext für die Methode doit """
        pass

test = beispiel()
print help(test)

