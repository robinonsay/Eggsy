from socketIO_client import SocketIO, LoggingNamespace

host = "li1013-216.members.linode.com"
port = 5000

socketIO = SocketIO(host, port, LoggingNamespace)
socketIO.wait()
print host
print port

def on_connection(*args):
    print('connected', args)

socketIO.on('connection', on_connection)
