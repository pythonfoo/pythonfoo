#!/usr/bin/env python
# -*- coding: utf-8 -*-


# some stuff with Propertys
# and why OOP is nice

# merge a simple code to OOP

import sqlite3


filename = "initdata.pro"
path = "./"

fullpath = path + filename

connection = sqlite3.connect(fullpath)
cursor = connection.cursor()

sqltxt = "SELECT adresse, name, vorname, key FROM adresse "

cursor.execute(sqltxt)
data = cursor.fetchall()

for line in data:
    for element in line:
        print element
    print "--------------"



print 8*"\n"
