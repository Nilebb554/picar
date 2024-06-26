from flask import Flask, render_template, Response
from flask_socketio import SocketIO

import RPi.GPIO as GPIO
from control import change_motor_speeds, power_up, power_down

from threading import Condition
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput
import libcamera

import io
import time

app = Flask(__name__)
socketio = SocketIO(app)

connected_clients = 0
    
class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()
    
    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()
                
picam2 = None
streaming_output = StreamingOutput()
    
def generate_frames():
    while True:
        with streaming_output.condition:
            streaming_output.condition.wait()
            frame = streaming_output.frame
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
     
@app.route('/')
def hello_world():
    return render_template("index.html")
    
@app.route('/video_feed')
def video_feed():
    global picam2
    global streaming_output
    
    if picam2 is None:
        picam2 = Picamera2()
        camera_config = picam2.create_video_configuration(main={"size": (1200, 600)})
        camera_config["transform"] = libcamera.Transform(hflip=1, vflip=1)
        picam2.configure(camera_config)
        picam2.start_recording(JpegEncoder(), FileOutput(streaming_output))
        
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
    
@socketio.on("connect")
def connect():
    global connected_clients
    if connected_clients == 0:
        power_up()
    connected_clients += 1

    
@socketio.on("disconnect")
def disconnect():
    global connected_clients
    connected_clients -= 1
    if connected_clients == 0:
        power_up()

@socketio.on("steeringData")
def handle_keyState(data):
    change_motor_speeds(data)
        
        
if __name__ == "__main__":
    socketio.run(app, ssl_context='adhoc', allow_unsafe_werkzeug=True, port=5000, host='0.0.0.0')
