from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from threading import Thread
import serial
import time
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

arduino_conn = serial.Serial("/dev/ttyAMA0", 9600, timeout=None)
cook = False

@app.route('/')
def hello_world():
    print('root called')
    return render_template('socketTest.html')

@app.route('/cook/')
def cook():
    print("Cook Egg")
    global cook
    cook = True
    arduino_conn.write("1")
    return "Cooking an Egg"

def main_routine():
    socketio.run(app, host='0.0.0.0')

def serial_comm():
    global cook
    while True:
        if cook:
            print "Writing to pi"
            arduino_conn.write("1")
            cook = False
        else:
            time.sleep(2)

t1 = Thread(target=main_routine)
#t2 = Thread(target=serial_comm)

t1.start()
#t2.start()
