#!/usr/bin/env python
# -*- coding: utf-8 -*-

# what we would write "normally"
#!/usr/bin/python

# thanks to derf (https://github.com/derf)
# thats the way today (system independent)
#!/usr/bin/env python

# you ONLY need coding: utf-8 buts way nicer
# -*- coding: utf-8 -*-

# demonstrate some encoding stuff
#fooBar = "\xc3".decode('latin1')
#print fooBar

# demonstrate indend block-foo
if 1 == 2:
	# tab indend
	print 'foo'
else:
    #space indend
    print 'bar'

# this would NOT work!!1!
'''
# mixed stuff
if 1 == 1:
	# tab indend
	print 'foo'
    #space indend
    print 'bar'
'''
