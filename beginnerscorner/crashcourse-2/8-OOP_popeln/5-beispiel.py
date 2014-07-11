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

    def get_data_by_tblName(self, tblName):
        if tblName == "adresse":
            sqltxt = "SELECT adresse, name, vorname, key FROM adresse "
            data = self.fetch_data_bySQL(sqltxt)
            return data 
        else:
            raise Exception("EX 0002: Table " + tblName + "does not exist")


    def datafoo(self):
        data = self.get_data_by_tblName("adresse")
        for line in data:
            for element in line:
                print element
            print "--------------"

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
        else:
            raise Exception("ES 0001: Type missmatch. has to be str")


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) == str:
            self._name = value
        else:
            raise Exception("ES 0001: Type missmatch. has to be str")

    @property
    def vorname(self):
        return self._vorname

    @vorname.setter
    def vorname(self, value):
        if type(value) == str:
            self._vorname = value
        else:
            raise Exception("ES 0001: Type missmatch. has to be str")


    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        if type(value) == int:
            self._key = value
        else:
            raise Exception("ES 0001: Type missmatch. has to be str")

def main():
    doit = sqlitefoo()
    doit.datafoo()

if __name__ == "__main__":
    main()



print 8*"\n"
