#!/usr/bin/python
#shezi
#https://github.com/shezi
#CC BY-SA 4.0

"""
Im a module!

how to use:
import docstrings
help(docstrings)
"""


##
# here is the description doxigen

class A():
	"""
	manny cool funcions
	
	first string in class = docu!
	docstring
	call me with
	help(docstrings.A)
	
	"""
	
	# just a useless comment!
	
	# you cant make a docstring for a var
	CLASS_VAR = 'just a var'
	
	def foo(self, bar):
		"""
		evil laugh (descrition string, max 120 chars! one sentence.
		
		a long block of text
		with everyting `markdownm`
		
		the >>> is for doctest
		import doctest
		doctest.testmod(docstreings)
		
		@param bar does nothing
		
		>>> a = A()
		>>> a.foo('BAR')
		muhahah
		
		"""

		print("muhahah")
