#!/usr/bin/python
a,t="\n%s bottles of beer on the wall","\nTake one down, pass it around"
for d in range(99,0,-1):print(a%d*2)[:-12]+t+a%(d-1 or'No')
