#!/usr/bin/env python
# -*- coding: utf-8 -*-


# a simple Property
# =================

class propertyFoo(object):
    def __init__(self):
        self._x = 10

    @property
    def X(self):
        print "Using @property"
        return self._x
        

    @X.setter
    def X(self, value):
        self._x = value
        print "using @X.setter"

foo = propertyFoo()

print foo.X
foo.X = 12
print foo.X

# ----------- clear -------------------
# propertys are usefull in case of Typefoo

class propertyFoo(object):
    def __init__(self):
        self._x = 10

    @property
    def X(self):
        return self._x


    @X.setter
    def X(self, value):
        if isinstance(value, str):
            self._x = value
        else:
            raise Exception("Exception: Type Missmatch. Only INT allowed") 

      

foo = propertyFoo()
print 4*"*" + " Now test if Integer works "

foo.X = 12
print foo.X

print 4*"*" + " Now test if String works "

foo.X = "FooBar"
print foo.X

# ------------------ clear -------------------
# a Property ListArray

class address(object):
    def __init__(self):
        self._ID = None 
        self._Name = None
        self._Vorname = None
        
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, value):
        if isinstance(value, int):
            self._ID = value
        else:
            raise Exception("Exception: Type Missmatch. Only INT allowed")

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, value):
        if isinstance(value, str):
            self._Name = value
        else:
            raise Exception("Exception: Type Missmatch. Only STR allowed")


    @property
    def Vorname(self):
        return self._Vorname

    @Vorname.setter
    def Vorname(self, value):
        if isinstance(value, str):
            self._Vorname = value
        else:
            raise Exception("Exception: Type Missmatch. Only STR allowed")


adrList = []

adr1 = address()
adr1.ID = 0
adr1.Name = "Mustermann"
adr1.Vorname = "Hans"
adrList.append(adr1)

adr2 = address()
adr2.ID = 1
adr2.Name = "Hanswurst"
adr2.Vorname = "Mortima"
adrList.append(adr2)

for element in adrList:
    print element

for element in adrList:
    print element.ID, element.Vorname, element.Name
