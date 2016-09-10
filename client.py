import socket

s = socket.socket()
host = "li1013-216.members.linode.com"
port = 5000
s.connect((host, port))
print s.recv(1024)
inpt = raw_input('type anything and click enter... ')
s.send(inpt)
print "the message has been sent"
