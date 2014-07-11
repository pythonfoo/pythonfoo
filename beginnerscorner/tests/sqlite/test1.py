#!/usr/bin/python
import sqlite3

""" Just simple testing SQLite"""

# Datenbankdatei erstellen - Durch die erste Verbindung wird die DB leer erstellt
connection = sqlite3.connect("test1.db")

# Man kann Sie auch nur im Memory laufen lassen :)
# connection = sqlite3.connect(":memory:")

# fuer die DB-Verarbeitung ist ein Cursor erforderlich:
cursor = connection.cursor()

# erste Tabelle anlegen
cursor.execute("""CREATE TABLE user (id INTEGER, name TEXT, vorname TEXT, pass TEXT)""")
cursor.execute("""CREATE TABLE chanel (id INTEGER, name TEXT, pass TEXT, typ INTEGER)""")

# Daten in die Tabelle fuellen
cursor.execute("""INSERT INTO user VALUES ( 1, 'oerb', 'the Real', 'hallo')""")
cursor.execute("""INSERT INTO user VALUES ( 2, 'bison', 'The Warhammer', 'hallo1')""")
connection.commit() # solange commit nicht ausgeführt, sind daten eventuell noch nicht geschrieben

# Sichere Datenuebergabe mit einem Dictionary 
werte = { "id" : "3", "name" : "00", "vorname" : "M", "pass" : "hallo3" }
sql = "INSERT INTO user VALUES (:id, :name, :vorname, :pass)"
cursor.execute(sql, werte)

connection.commit()

# alternativ geht auch folgendes
for row in ((4, "superhero", "Hero", "karabanga"),
            (4, "Nemo", "Captain", "Nautilus")):
    cursor.execute("INSERT INTO user VALUES(?,?,?,?)",row)

connection.commit()

# ne kleine selectabfrage

cursor.execute("SELECT vorname, name FROM user WHERE id=1")
data = cursor.fetchall()

print(data[0])
connection.close()
