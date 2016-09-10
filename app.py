import json
import socket
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



s = socket.socket()
host = socket.gethostname()
port = 12
s.bind((host,port))
s.listen(5)

def ack():
    print("Recieved Callback")

@app.route('/')
def hello_world():
    print('root called')
    return render_template('socketTest.html')

@app.route('/cook/')
def cook():
    print("Cook Egg")
    message = {'data':'Cook Egg', 'cook': True}
    emit('cook', message, namespace='/', broadcast=True)
    return json.dumps(message)

@socketio.on('join')
def on_join(data):
    message = {'data':'Joined Room', 'cook': False}
    room = data['room']
    join_room(room)
    send(json.dumps(message),json=True, room=room)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
    while True:
        c, addr = s.accept()
        print("Connection accepted from " + repr(addr[1]))

        c.send("Server approved connection\n")
        print repr(addr[1]) + ": " + c.recv(1026)
        c.close()
