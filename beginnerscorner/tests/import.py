#!/usr/bin/env python 

'''
import importlib
my_module = importlib.import_module('os')
help(my_module)
'''

moduleNames = ['os']
#moduleNames
#['sys', 'os', 're', 'unittest']
module = map(__import__, moduleNames)
help(module[0])
print module
