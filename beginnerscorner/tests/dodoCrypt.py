# Verscchluesselungsarray schreiben
ascii = 65

a = chr(ascii)
y = []
for i in range(26):
   
    ip = chr(i + 65)
    x = []
    for p in range(26):
        if i+p+65 <= 90:
           x.append(chr(i+p+65))
        else:
            x.append(chr(i+p+65-26))
        
    y.append(x)


# Frage Key       
key = raw_input('Gib bitte die Spalte an: \n')
# Frage text
text = raw_input('Gib bitte die Zeile an: \n')


# Jeder Buchstabe des Keys ist =q
#for currentkeychar in key:
    #print q
    
#Mit dem ersten Buchstaben aus dem Text 
# Textstelle bekommt den Wer null    
textstelle = 0
for w in text:
        
        #print w
    arraystelle = 0
        
        #Suche in der Spalte nach dem Keybuchstaben mit selben Index
    for n in y[0]:
            
        if n == w:
                #print wrong
                #l = 0
            keystelle = 0
            while keystelle != 25:
                if y[keystelle][arraystelle] == key[textstelle]:
                    
                        #print wrong2
                        
                    print y[keystelle][0]
                        
                keystelle += 1
                    
                    #l += 1
                    
        arraystelle += 1
    textstelle += 1                    
            
       
