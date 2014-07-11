#!/usr/bin/python

a = [[1,2,3,4,5],[6,7,8,9,10]]
print a
for i in a:
    print i
    for p in i:
        print p

print "Mittels Koordinaten:"
print a[1][3]

b = []

b.append(5)
b.append(4)
c = []
c.append(b)

b=[]
b.append("t")
b.append("s")

c.append(b)

print c
