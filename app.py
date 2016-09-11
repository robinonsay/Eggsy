from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from threading import Thread
import serial
import time
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

arduino_conn = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
arduino_conn.flushInput()
arduino_conn.flushOutput()
cook = False

@app.route('/')
def hello_world():
    print('root called')
    return render_template('socketTest.html')

@app.route('/cook/', methods=['GET'])
def cook():
    type = request.args.get('type')
    print("TYPE: %s"%type)
    print("Cook Egg Before")
    global cook
    cook = True
    arduino_conn.write("1")
    print("Cook Egg After")
    return {"message":"Cooking an Egg"}

def serial_comm():
    global cook
    while True:
        if cook:
            print "Writing to pi"
            arduino_conn.write("1")
            cook = False
        else:
            time.sleep(2)

# t1 = Thread(target=main_routine)
#t2 = Thread(target=serial_comm)

# t1.start()
#t2.start()
#
if not arduino_conn.is_open:
    arduino_conn.open()
socketio.run(app, host='0.0.0.0')
