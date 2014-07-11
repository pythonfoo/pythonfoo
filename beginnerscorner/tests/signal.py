#!/usr/bin/python
import signal
import sys, select

#ValueError: signal only works in main thread
def interrupted(signum, frame):
	#"called when read times out"
	#print 'interrupted!'
	signal.signal(signal.SIGALRM, 'no commands')

def cmdInput():
	try:
		#print 'You have 5 seconds to type in your stuff...'
		foo = raw_input("Type 'q' to end: ")
		return foo
	except:
			# timeout
			return ''

# set catcher for no command
signal.signal(signal.SIGALRM, interrupted)
# set alarm
signal.alarm(1)
cmd = self.cmdInput()
# disable the alarm after success
signal.alarm(0)


#import sys, select
print "You have ten seconds to answer!"
i, o, e = select.select( [sys.stdin], [], [], 10 )
if (i):
  print "You said", sys.stdin.readline().strip()
else:
  print "You said nothing!"
