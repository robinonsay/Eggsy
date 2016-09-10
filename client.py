from socket import *

host = "li1013-216.members.linode.com"

print host

port = 5000

s = socket(AF_INET, SOCK_STREAM)

print "socket made"

s.connect((host,port))

print "socket connected!!!"

nreceive = True#nreceive = Not Received
ticks = 0
f = None
while nreceive and ticks < 101:#try to get the info 100 times or until it's received
    ticks+=1
    try:
        f = s.makefile('rb')
        if not f == None:
            nreceive = False
    except:
        pass
data = f.read(1024)

print data
s.close                     # Close the socket when done
