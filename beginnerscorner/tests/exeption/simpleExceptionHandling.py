#!/usr/bin/python

hasOnlyNumbers = True
while hasOnlyNumbers == True:
    tmpInput = ""
    try:
        tmpInput = raw_input("Enter a Number: ")
        if tmpInput.isdigit() == True:
            print("Number: " + tmpInput)
            tmpCalc = 0 / int(tmpInput)
        else:
            raise RuntimeError("idiot!")

    except RuntimeError as err:
        print("You are doing it WRONG! " + str(err))
        hasOnlyNumbers = False
    except Exception as ex:
        print("OtherException: " + str(ex))
        #hasOnlyNumbers = False
         
raw_input("End of Program!")
