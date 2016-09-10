from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

def ack():
    print("recieved")

@app.route('/')
def hello_world():
    print('root called')
    return render_template('socketTest.html')

@app.route('/cook/')
def cook():
    print("Sending")
    emit('response', {'data': 'Sending From Server on cook'}, namespace='/', broadcast=True)
    return "Sent"

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    send({'data': 'Sending From Server'},json=True, room=room)

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)

@socketio.on('test response')
def handle_my_custom_event(json):
    print('received response: ' + str(json))

@socketio.on('my event')
def handle_my_custom_event(json):
    send({'data': 'Sending From Server'}, json=True, callback=ack)
    print('received json: ' + str(json))
