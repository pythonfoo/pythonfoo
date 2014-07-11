#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://docs.python.org/2/library/queue.html
from multiprocessing import Process, Queue
import time
import random

def my_function(q, x):
	doSleep = random.randint(1,11)
	print doSleep
	time.sleep(doSleep)
	q.put( str(x + 100) + ' slept:' + str(doSleep) )

if __name__ == '__main__':
	queue = Queue()
	
	for i in range(11):
		p = Process(target=my_function, args=(queue, i))
		p.start()
		#p.join()	# this deadlocks
	
	try:
		while True:
			result = queue.get(True, 11)
			print result
	except Exception as e: #Queue.Empty:
		print 'nothing left', e
