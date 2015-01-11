#!/usr/bin/env python

# basic print
print 'foo'

# different print
print('bar')

# parameters
print("foo", 'bar')
print "foo", 'bar'

# "return"
print "foo\nbar"
print 'foo\nbar'

# no auto return
print "bar",
print 'foo'

# concat print
print "#"+'foo'+'bar'+'#'

# show special string stuff 
print 8*'#'

# some formatting stuff
print 'parse string %s and integer %i' % ('ssd', 23)

''' i am
a multiline
print 'foo'
comment
'''

print '''i am a long comment and should not be vissible
at
ALL!!1!
'''
