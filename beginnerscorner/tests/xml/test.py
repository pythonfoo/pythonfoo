
#!/usr/bin/python3
import xml.dom.minidom as dom

def knoten_auslesen(knoten):
        return eval("%s('%s')" % (knoten.getAttribute("typ"), knoten.firstChild.data.strip()))

def lade_dict(dateiname):
    d=()
    baum = dom.parse(dateiname)
    idnr = [] 
    name = []
        

    for eintrag in baum.firstChild.childNodes:
        if eintrag.nodeName == "eintrag":
            schluessel = wert = None
            for knoten in eintrag.childNodes:
                if knoten.nodeName == "id":
                    idnr = knoten_auslesen(knoten)
                    print(idnr)
                elif knoten.nodeName == "name":
                    name = knoten_auslesen(knoten)
                    print(name)
    return (idnr , name)


data = None
data = lade_dict("beispielObjDeclaration.xml")
print("#################################")
for d in data:
   print(d)
