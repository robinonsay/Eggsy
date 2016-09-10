from socket import *

host = "li1013-216.members.linode.com"

print host

port = 5000

s = socket(AF_INET, SOCK_STREAM)

print "socket made"

s.connect((host,port))

print "socket connected!!!"
s.send("Python is Connected")


while 1:
    data = s.recv(1024)
    print data
    if not data:
        break
    s.send(data)
s.close()                    # Close the socket when done
