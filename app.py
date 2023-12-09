from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import RPi.GPIO as GPIO
from control import change_state, power_up, power_down

from picamera2 import Picamera2
from threading import Condition
import io
import time

app = Flask(__name__)
socketio = SocketIO(app)

class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()

picam2 = None
cameraOutput = StreamingOutput()

def generate_frame(): 
    while True:
        with cameraOutput.condition:
            cameraOutput.condition.wait()
            frame = cameraOutput.frame
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    global picam2
    global cameraOutput

    if picam2 == None:
        picam2 = picamera2.Picamera2()
        picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
        
        cameraOutput = StreamingOutput()
        picam2.start_recording(JpegEncoder(), FileOutput(cameraOutput))

    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

@socketio.on("connect")
def connect():
    power_up()
    print("Client connected")

@socketio.on("disconnect")
def disconnect():
    power_down()
    print("Client disconnected")

@socketio.on("keyState")
def handle_keyState(keyState):
    print(keyState)
    change_state(keyState)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)