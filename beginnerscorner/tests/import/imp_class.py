import random
import imp_var

class matrix(object):
	def printMatrix(self, lines):
		for i in range(lines):
			row = ''
			
			for rw in range(imp_var.matrixRows):
				row += str(random.randint(0,1))
			
			print row
