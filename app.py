import json
from flask import Flask, render_template
from threading import Thread
import serial
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
arduino_conn = serial.Serial("/dev/ttyUSB0", 9600, timeout=None)
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
    return json.dumps(message)

def main_routine():
    app.run(app, host='0.0.0.0')

def serial_comm():
    global cook
    while True:
        if cook:
            arduino_conn.write("1")
            cook = False
        else:
            time.sleep(2)

t1 = Thread.join("main_routine", timeout=None)
t2 = Thread.join("serial_comm", timeout=None)

t1.start()
t2.start()
