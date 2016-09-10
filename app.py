import json
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


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

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('join')
def on_join(data):
    message = {'data':'Joined Room', 'cook': False}
    room = data['room']
    join_room(room)
    send(json.dumps(message),json=True, room=room)

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    send({'cook': False},json=True, room=room)

@socketio.on('test response')
def handle_my_custom_event(json):
    print('received response: ' + str(json))

@socketio.on('connection')
def handle_connection(json):
    send({'data': 'Server Connected'}, json=True, callback=ack)
    print('received connection json from client: ' + str(json))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
