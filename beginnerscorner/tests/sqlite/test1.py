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
cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, vorname TEXT, pass TEXT, personalNummer INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS chanel (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT, typ INTEGER)")

# Daten in die Tabelle fuellen (is aber kacke so)
cursor.execute("INSERT INTO user VALUES (NULL, 'oerb', 'the Real', 'hallo', 1337);")
cursor.execute("INSERT INTO user VALUES (NULL, 'bison', 'The Warhammer', 'hallo1', 23);")
connection.commit()  # solange commit nicht ausgefuehrt, sind daten eventuell noch nicht geschrieben

# Sichere Datenuebergabe mit einem Dictionary 
werte = { "id" : None, "name" : "00", "vorname" : "M", "pass" : "hallo3", "personalNummer": 01 }
sql = "INSERT INTO user VALUES (:id, :name, :vorname, :pass, :personalNummer)"
cursor.execute(sql, werte)

connection.commit()


werte = {"id": None, "name" : "01", "vorname" : "M", "pass" : "hallo3", "personalNummer": 02 }
sql = "INSERT INTO user VALUES (:id, :name, :vorname, :pass, :personalNummer)"
cursor.execute(sql, werte)

connection.commit()

# alternativ geht auch folgendes
for row in ((None, "superhero", "Hero", "karabanga", 77),
            (None, "Nemo", "Captain", "Nautilus", 88)):
    cursor.execute("INSERT INTO user VALUES(?,?,?,?,?)", row)

connection.commit()

# ne kleine selectabfrage (in kacke)
cursor.execute("SELECT vorname, name FROM user WHERE personalNummer>2")
dataRows = cursor.fetchall()

for data in dataRows:
    print(data)

print dataRows[0]

print '--------------------'

# ne kleine selectabfrage (in "sicher")
cursor.execute("SELECT vorname, name FROM user WHERE personalNummer>:personalNummer", {"personalNummer": 2})
dataRows = cursor.fetchall()

for data in dataRows:
    print(data)

print dataRows[0]


connection.close()