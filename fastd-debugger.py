#!/usr/bin/python
import socket
import sys
import os
import json
from sets import Set



# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)



# Connect the socket to the port where the server is listening
sock_addr = str(sys.argv[1])
#print >>sys.stderr, 'connecting to %s' % sock_addr
try:
	sock.connect(sock_addr)
except socket.error, msg:
	print >>sys.stderr, "socket brocken" 
	sys.exit(1)


# Send data
#message = 'This is the message.  It will be repeated.'
#print >>sys.stderr, 'sending "%s"' % message
#sock.sendall(message)
connected = Set([])
disconnected = Set([])
nodes = {'connected': [], "disconnected": []}


channel = False
amount_received = 0
#amount_expected = len(message)
data = "start" 
all_data = ""
while data:
	data = sock.recv(100)
	all_data +=data
#print >>sys.stderr, '"%s"' % all_data
j = json.loads(all_data)
for peer in j["peers"]:
	p = j["peers"][peer]
	print p
	if  p["connection"]:
		connected.add(p["name"].encode("utf8"))
	else:
		disconnected.add(str(p["name"]))
disconnected = disconnected - connected
print len(connected)
print connected

sock.close()

