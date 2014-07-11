#!/usr/bin/env python                                                           
# -*- coding: utf-8 -*-                                                         
                                                                                
#               
#       Classes, Methods, Constructors 

# Der Klassenrumpf

class foo(object):
    pass


# Methoden 
# Keine Umlaute oder Operatoren im Namen
# nur Methoden etc verwenden ....


class foo_methods(object):
    print("Hurz")

    def print_Foo(self):
        print("Foo")

# --!! wie man sehen kann, wird print("Hurz") ausgegeben obwohl, 
# die Classe noch nicht aufgerufen / Instanziiert wurde
# deshalb nur methoden definitionen in classen verwenden nicht direkten code...

# richtig wäre:
# --------- von Hand ausbauen ----------


class foo_methods(object):
        def hurz(self):
            print("Hurz")

        def print_Foo(self):
                print("Foo")


# Instanziierung der Klasse

instanz_von_foo = foo_methods()

# aufruf der Methode print_Foo

instanz_von_foo.print_Foo()
instanz_von_foo.hurz()


# einfache Parameterübergabe in Methoden

class foo_methods(object):
    def print_Foo(self, text):
        print(text)

instanz_von_foo = foo_methods()
instanz_von_foo.print_Foo("Hallo Pythonfoo")


# mehrere fest definierte Parameter
# ---- von Hand ausbauen--------

class foo_methods(object):
    def print_Foo(self, text, multiplikator):
        print multiplikator*text

instanz_von_foo = foo_methods()
instanz_von_foo.print_Foo("Hallo Pythonfoo",5)

# variable Anzahl von Parametern

class foo_methods(object):
    def print_Foo(self, *foo_parameter):
        print "It is at Tuple: " , foo_parameter
        for param in foo_parameter:
            print param

instanz_von_foo = foo_methods()
instanz_von_foo.print_Foo("Hallo Pythonfoo","Python ist cool")

# variable Anzahl von Parametern in Dictionary

class foo_methods(object):

    def print_Foo(self, **foo_parameter):

        print "just printed: " , foo_parameter

        if "gruss" in foo_parameter:
            print "Die Grußformel lautet: " + foo_parameter["gruss"]
        else:
            print "Keine Grüße enthalten"

instanz_von_foo = foo_methods()
instanz_von_foo.print_Foo(gruss = "Hallo Pythonfoo",sagt = "Python ist cool")

# Construktor __init__
# Der Konstruktor einer Classe ist die Methode, die als erstes 
# bei der initialisierung der Classe aufgerufen wird.
# In python wird der Construktor __init__ genannt



class foo(object):
    def __init__(self):
        print "Ich bin der __init__ Konstruktor und komme bei der Instantiierung"
        
        # Variablendeklaration in einer Klasse während der Initialisierung
        
        self.magic = "Variablen einer Classe werden mit self. begonnen"
        
        # Es gibt nur die Konvention private Variablen und Methoden in
        # der Namensgebung mit Unterstrich zu beginnen.
        
        self._privat = "Private Variablen in Klassen unter Python gibt es nicht"


fooclass  = foo()
print fooclass.magic
print fooclass._privat



# Instantiierung mit Parameterübergabe
# Der Konstruktor kann bei der Instantiierung 
# der Klasse vergleichbar zur Methode Parameter entgegennehmen

class foo(object):
    def __init__(self, text):
        print text

fooclass  = foo("Hallo Pythonfoo")

# was tut self oder Variablen in Klassen 
# ------- die Prints nacheinander von Hand testen -----------
# ------- immer ein geht nicht dahinter ---------------------

class foo(object):
    def __init__(self):
        var1 = "Ich bin var1"
        self.var2 = "Ich bin var2"

    def printvar1(self):
            print var1


foobar = foo()

print var1
# print foobar.var1
# print foobar.printvar1()
# print foobar.var2

# wie man sehen kann, ist eine einfache Variable innerhalb 
# einer Methode nur in der Methode selbs zu benutzen
# für den Zugriff aus anderen Methoden oder von außerhalb in die Klasse
# ist self erforderlich
