from flask import Flask, render_template, Response
import cv2

from flask_socketio import SocketIO
import RPi.GPIO as GPIO
from control import change_state, power_up, power_down

app = Flask(__name__)
socketio = SocketIO(app)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
 
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@socketio.on("connect")
def connect():
    #power_up()
    print("Client connected")

@socketio.on("disconnect")
def disconnect():
    #power_down()
    print("Client disconnected")

@socketio.on("keyState")
def handle_keyState(keyState):
    print(keyState)
    #change_state(keyState)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
