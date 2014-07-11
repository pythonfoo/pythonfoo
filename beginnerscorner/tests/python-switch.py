#!/usr/bin/python
#-*- coding:utf8 -*-

# Benutzen eines Dictionary um gewissermaßen Switchfunktion aus C# zu haben
# Da Funktion in Switch nur als Funktion aber nicht ausgeführte Funktion funkioniert
# lambda benutzen, 
def y():
    print("hallo")

d = {
    "a": lambda x: x**2,
    "b": y,
}

print d["a"](8)
d["b"]()



# sehr schnell wemm viele Vergleiche Richtung 1000 und mehr


