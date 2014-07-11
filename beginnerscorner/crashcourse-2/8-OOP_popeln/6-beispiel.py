#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3

class sqlitefoo(object):
    def __init__(self):
        self.filename = "initdata.pro"
        self.path = "./"

        self.fullpath = self.path + self.filename

    def get_connection(self, fullpath):   
        connection = sqlite3.connect(fullpath)
        return connection
    
    def get_cursor(self, connection): 
        cursor = connection.cursor()
        return cursor

    def get_connection_cursor(self, fullpath):
        connection = self.get_connection(fullpath)
        cursor = self.get_cursor(connection)
        return cursor

    def fetch_data_bySQL(self, sqltxt):
        cursor = self.get_connection_cursor(self.fullpath)
        cursor.execute(sqltxt)
        data = cursor.fetchall()
        return data

    def get_dataproperty_Larray(self, tblName):
        data = self.get_data_by_tblName(tblName)
        propLarray = []
        for line in data:
            adr = adresse()
            adr.adresse = line[0]
            adr.name = line[1]
            adr.vorname = line[2]
            adr.key = int(line[3])        
            propLarray.append(adr)
        return propLarray

    def get_data_by_tblName(self, tblName):
        if tblName == "adresse":
            sqltxt = "SELECT adresse, name, vorname, key FROM adresse "
            data = self.fetch_data_bySQL(sqltxt)
            return data 
        else:
            raise Exception("EX 0002: Table " + tblName + "does not exist")


class adresse(object):
    def __init__(self):
        self._adresse = ""
        self._name = ""
        self._vorname = ""
        self._key = None

    @property
    def adresse(self):
        return self._adresse

    @adresse.setter
    def adresse(self, value):
        if type(value) == str:
            self._adresse = value
        elif type(value) == unicode:
            self._adresse = str(value)
        else:
            raise Exception("ES 0001: Type missmatch. has to be str")


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) == str:
            self._name = value
        elif type(value) == unicode:
            self._name = str(value)
        else:
            raise Exception("ES 0001: Type missmatch. has to be str")

    @property
    def vorname(self):
        return self._vorname

    @vorname.setter
    def vorname(self, value):
        if type(value) == str:
            self._vorname = value
        elif type(value) == unicode:
            self._vorname = str(value)
        else:
            raise Exception("ES 0001: Type missmatch. has to be str")


    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        if type(value) == int:
            self._key = value
        elif type(value) == unicode:
            self._key = int(value)
        else:
            raise Exception("ES 0001: Type missmatch. has to be int")

def main():
    doit = sqlitefoo()
    propdatalist = doit.get_dataproperty_Larray("adresse")
    for adr in propdatalist:
        print adr.name
        print adr.vorname
        print adr.adresse
        print adr.key
        print 8*"-"

if __name__ == "__main__":
    main()

# Wo man jetzt weiter machen könnte:
# ----------------------------------
# TODO: get_dataproperty_Larray() zu ner eigenen adressHandler Klasse machen
# TODO: typenprüfung Str und Int an einer Stelle machen
# TODO: SQL-String generieren auf Input des Tabellennamens
# TODO: SQL-Input schreiben
# TODO: SQLITE File erzeugen und Tabelle erzeugen

# Literaturempfehlung:
# -------------------------
# Bezugsquelle: http://www.amazon.de/Expert-C-2008-Business-Objects/dp/1430210192
# Author: Rockford Lhotka
# Titel: Expert C# 2008 Business Objects
# -------------------------
# Projektlink: http://sourceforge.net/projects/habanero/
# Projektname: Habanero
# Sprache: C#
# Info: OpenSource Business Application Framework
# -------------------------
# Projektlink: https://www.openerp.com/de/
# Projektname: openerp
# Sprache: Python 
# Info: OpenSource Business Application Framework
# -------------------------


print 8*"\n"
