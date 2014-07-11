#!/usr/bin/python
import time
import threading

class MultiThread(threading.Thread): 
	def __init__(self, count): 
		threading.Thread.__init__(self)
		self.count = count
				
	def run(self):
		time.sleep(0.5 + self.count)
		print 'fin ' + str(self.count)

counts = 4
myThreads = [] 
for i in range(counts):
	thread = MultiThread(i)
	myThreads.append(thread)
	thread.start()
	time.sleep(0.300)
	
# wait for all threads to finish 
for t in myThreads: 
	print 'before join'
	t.join()
	print 'after join'

print 'fin main'
