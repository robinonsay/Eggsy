from socketIO_client import SocketIO, BaseNamespace

host = "li1013-216.members.linode.com"
port = 5000

class Namespace(BaseNamespace):

    def on_connect(self):
        print('[Connected]')

socketIO = SocketIO(host, port, LoggingNamespace)
socketIO.wait(seconds=1)

print host
print port

def on_connection(*args):
    print('connected', args)

socketIO.on('connection', on_connection)
