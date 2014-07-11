#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Typenprüfung
# ============

# Der Befehl type() aus crashcourse-0
#-------------------------------------

var1 = 10
var2 = 0.20
var3 = "Hallo"
print type(var1)
print type(var2)
print type(var3)

# type() und Klassen
#--------------------

class foo(object):
    def __init__(self):
        self._data = "Rot"
        self.data = "blau"
        print "Print inside Class: ", self._data

class foobar(object):
    pass

# Instanziierung
fooClass = foo()
foobarClass = foobar()


print(type(fooClass))

# Typenprüfung mittels Type
if type(fooClass) == foo:
    print "Jo fooClass is foo"
else:
    print "Ups fooClass isn't foo"

if type(foobarClass) == foo:
    print "Jo foobarClass is foo"
else:
    print "Ups foobarClass isn't foo"

# Typenprüfung mittels isinstance

if isinstance(fooClass, foo):
    print "Jo ...shit!!! it is foo"
else:
    print "F! it isn't foo"

# Ableitungen von Klassen

class subfoo(foo):
    def __init__(self):
        super(subfoo, self).__init__() 
        self.subdata = "Grün"

classSubfoo = subfoo()

print "Subfoo Data: ", classSubfoo.data, classSubfoo.subdata 


# Typenprüfung type vs isinstance

if type(classSubfoo) == foo:
    print "by type Subfoo is foo"
else:
    print "by type subfoo isn't foo"

if isinstance(classSubfoo, foo):
    print "by isinstance Subfoo is foo"
else:
    print "by isinstance subfoo isn't foo"


# und man kann auch auf die Elternklasse der Elternklasse prüfen

if isinstance(classSubfoo, object):
    print "Jo, Subfoo Parent ist object"
else:
    print "Subfoo ist not child of object"
