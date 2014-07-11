#!/usr/bin/python

print '############ imp_class ############'
import imp_class
imp_class.matrixRows = 2 # has NO effect to the import in the matrix-class!
mt = imp_class.matrix()
mt.printMatrix(23)

print '############ imp_var ############'
import imp_var

print imp_var.varDict
imp_var.varDict['key3'] = 'key3'
print imp_var.varDict

print '############ from imp_var import varDict ############'
from imp_var import varDict 

print varDict
varDict['key4'] = 'key4'
print varDict


