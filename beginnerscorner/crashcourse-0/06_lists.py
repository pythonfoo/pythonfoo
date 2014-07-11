#!/usr/bin/env python

#### tuple
staticList = (23, 42, 'bar')
print staticList

## better not show? could be confusing
# pack vars to list
#staticList = 23, 42, 'bar'
#print staticList
# extract list to vars
#a1, a2, a3 = staticList
#print a3

# access single item by index
print staticList[1]

### list
aList = [3, 2, 4, 1, 'hamster', 'foo']
print aList

# access single item by index
print aList[3]

aList.reverse()
print aList

#sorted(aList)

aList.sort()
print aList

aList.append('bar')
print aList

tmpFoo = aList.pop()
print 'tmpFoo:', tmpFoo, 'aList:', aList

tmpFoo = aList.pop(-1)
print 'tmpFoo:', tmpFoo, 'aList:', aList

# good examples at: http://effbot.org/zone/python-list.htm


### dictionary
aDict = {'blue':'blau', 'yellow':'gelb', 'pirated':'zugutenberg'}
print aDict

print 'get by key:', aDict['pirated']

# access a non existing key
#print 'get by key:', aDict['nope']

# add stuff
aDict['cat'] = 'Katze'
print aDict

# change stuff
aDict['cat'] = 'Hund'
print aDict
