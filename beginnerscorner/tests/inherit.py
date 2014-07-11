class class1(object):
	testText1 = 'fooo'
	testText2 = 'bar'
	
	def __init__(self):
		pass

	def printText(self):
		print self.testText1, self.testText2
		
class class2(class1):
	testText3 = 'TXT 3'

	def __init__(self):
		self.testText2 = 'fail'
		self.testText4 = 'TXT 4'
		
	def createNewGlobal(self):
		self.testText5 = '555555'
		
	def printTextChild(self):
		print self.testText1, self.testText2, self.testText3, self.testText4, self.testText5
		

c1 = class1()
print 'c1.printText():'
c1.printText()

print ''

c2 = class2()
print 'c2.printText():'
c2.printText()
c2.createNewGlobal()
print 'c2.printTextChild()'
c2.printTextChild()
