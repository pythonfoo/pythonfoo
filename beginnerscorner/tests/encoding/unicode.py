#!/usr/bin/python
s = u"\u221E"
print('sign: ' + s)
print ord(u'\u221E')
print unichr(ord(u'\u221E'))
print "to UTF8:" + unichr(8734).encode('utf-8')
