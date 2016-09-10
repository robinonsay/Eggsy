from socket import *

host = "li1013-216.members.linode.com"

print host

port = 5000

s = socket(AF_INET, SOCK_STREAM)

print "socket made"

s.connect((host,port))

print "socket connected!!!"

print s.recv(1024)
s.close                     # Close the socket when done
