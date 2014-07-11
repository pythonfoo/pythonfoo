#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

class sqlitefoo(object):
    def __init__(self):
        self.filename = "initdata.pro"
        self.path = "./"

        self.fullpath = self.path + self.filename

    def get_connection(self, fullpath):   
        connection = sqlite3.connect(self.fullpath)
        return connection
    
    def get_cursor(self, connection): 
        cursor = connection.cursor()
        return cursor

    def datafoo(self):
        
        connection = self.get_connection(self.fullpath)
        cursor = self.get_cursor(connection)

        sqltxt = "SELECT adresse, name, vorname, key FROM adresse "

        cursor.execute(sqltxt)
        data = cursor.fetchall()

        for line in data:
            for element in line:
                print element
            print "--------------"


def main():
    doit = sqlitefoo()
    doit.datafoo()

if __name__ == "__main__":
    main()



print 8*"\n"
