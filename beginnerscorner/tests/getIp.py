#!/usr/bin/python
# Quelle: http://fabaff.blogspot.de/2007/07/ip-adresse-und-python.html

deviceName = 'wlan0' # eth0, ath0.....

import socket

print '############ V1 ############'

# System name
sys_name = socket.gethostname()
# IP adress
ip_addr = socket.gethostbyname(sys_name)

print ip_addr 

print '############ V2 ############'

import os

ip_adress = os.system('cat /proc/net/arp | grep '+ deviceName +' | cut -c -15')
print ip_adress

print '############ V3 ############'

#import socket
import fcntl
import struct

def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
			s.fileno(),
			0x8915,  # SIOCGIFADDR
			struct.pack('256s', ifname[:15])
			)[20:24])

print get_ip_address(deviceName) #('ath0')

# Quelle: http://houseoflaudanum.com/navigate/snippets/discovering-local-ip-addresses-in-python/
print '############ V4 ############'

#import socket

hostname = socket.gethostname()
address = socket.gethostbyname("%s.local" % hostname)
addr = address #, port
print addr, address, hostname
print 'short method:', socket.gethostbyname("%s.local" % socket.gethostname())
