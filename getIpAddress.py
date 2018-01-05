#!/usr/bin/env python3.5
def IpAddress():
	import socket
	import subprocess
	import smtplib
	#gets and prints the hostname hostname = socket.gethostname() print('hostname: %s' % hostname) gets and
	#prints the local host IP address address = socket.gethostbyname(hostname) print('localhost IP: %s' %
	#address) gets and prints the DNS assigned IP address
	arg='ip route list'
	p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
	data = p.communicate()
	split_data = data[0].split() # returns a byte array
	ipaddr = split_data[17] # get the byte array that is at element 13
	ipaddr = ipaddr.decode("utf-8") # converts the byte array into a string
	#print('IP address: %s' % ipaddr)
	return ipaddr
