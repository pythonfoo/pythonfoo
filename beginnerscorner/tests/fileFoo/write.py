# schreibt Hello an die Datei test.txt hinten an ( 'a' fuer anhaengen und 'w' fuer schreiben/neu )

datei = open('test.txt', 'a')
datei.write('Hello!')
datei.close()
