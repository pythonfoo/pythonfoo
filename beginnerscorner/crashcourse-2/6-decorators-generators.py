#!/usr/bin/env python
# -*- coding: utf-8 -*-

#       Decorators 
# sind Funktionen, die vorher definiert werden müssen, die 
# Funktionen entgegennehmen und diese verändern

# Nachfolgend werden die Ergebnisse aus fak() 
# gecached, so dass sie nur Berechnet werden,
# wenn sie noch nicht im Cache sind 

class CacheDecorator(object):

    def __init__(self):
        self.cache = {} 
        self.func = None

    def cachedFunc(self, *args): 
        if args not in self.cache: 
            self.cache[args] = self.func(*args) 
        else:
            print "cachedINFO"
        return self.cache[args]

    def __call__(self, func):
        self.func = func
        return self.cachedFunc

@CacheDecorator()
def fak(n):
    ergebnis = 1
    for i in xrange(2, n+1):
        ergebnis *= i
    return ergebnis



print fak(10)
print fak(20)
print fak(10)
print fak(20)

# -------------------------------
# Generators
# -------------------------------

# Beispiel random versus xrandom mittels Generatoren

# 1. der pythonic range() weg
for i in range(10):
    print "range i: ", i

# 2. der Weg mit weniger speicher aber langsam wegen der prüfung auf <= 10
i = 0
while i <= 10:
    print "While i:  ", i
    i += 1

# 3. der Weg wie in 2 jedoch als generatorfunktion

def xgen(param):
    while i <= 10:
        x += 1
        yield x

for i in xgen(10):
    print "xgen i: ", i
