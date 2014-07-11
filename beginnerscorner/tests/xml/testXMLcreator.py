#!/usr/bin/python3
# Beispiel zum schreiben eines XML-Baums

import xml.dom.minidom as dom

def erstelle_eintrag(idnr, name):
    # Definition der Baumelemente
    tag_eintrag = dom.Element("eintrag")
    tag_idnr = dom.Element("id")
    tag_name = dom.Element("name")
    
    # Typpruefung der datenelemente und typinfo schreiben in den Baum
    tag_idnr.setAttribute("typ", type(idnr).__name__)
    tag_name.setAttribute("typ", type(name).__name__)


    text = dom.Text()
    text.data = str(idnr)
    tag_idnr.appendChild(text)

    text = dom.Text()
    text.data = str(name)
    tag_name.appendChild(text)

    # Eintrag wird in Baum gefuegt
    tag_eintrag.appendChild(tag_idnr)
    tag_eintrag.appendChild(tag_name)
    return tag_eintrag

def schreibe_dict(d, dateiname):
    # Uebernimmt das Dictionary und Schreibt die Elemente in den Baum
    baum = dom.Document()
    tag_dict = dom.Element("dictionary")
    
    # fuehgt ein weiteres element in den Baum je schleifendurchlauf
    for idnr, name in d.items():
        tag_eintrag = erstelle_eintrag(idnr, name)
        tag_dict.appendChild(tag_eintrag)

    # fuegt den Hauptzweig mit allen Elementen in den XML Baum
    baum.appendChild(tag_dict)

    # schreibt die XMLdaten in die datei
    with open(dateiname, "w") as f:
        baum.writexml(f, "", "\t", "\n")

# Aufruf der Funktionen
# dictionary leermachen
dictdate = {}
# Werte an dictionary uebergeben
dictdata = { "idnr" : 1 , "name" : "Vorname" }
# XML Funktion schreiben mit dem im dictdata Dictionary enthaltenen Daten
schreibe_dict(dictdata, "testAuto.xml")

#print(erstelle_eintrag(1,"Vorname"))
