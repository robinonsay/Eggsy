from socketIO_client import SocketIO, LoggingNamespace

host = "li1013-216.members.linode.com"
port = 5000

socketIO = SocketIO(host, port, LoggingNamespace)
print host
print port

socketIO.on('connection', on_connection)


def on_connection(*args):
    print('connected', args)
