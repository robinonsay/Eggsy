from socket import *

host = "li1013-216.members.linode.com"

print host

port = 5000

s = socket(AF_INET, SOCK_STREAM)

print "socket made"

s.connect((host,port))

print "socket connected!!!"
s.send("Python is Connected")

r, _, _ = select.select([self.conn], [], [])
if r:
    print "There is data"
    data = s.recv(1024)
    print data
    s.send(data)
s.close()                    # Close the socket when done
