from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import picamera
import cv2

from control import change_state, power_up, power_down
from camera_opencv import generate_frames

app = Flask(__name__)
socketio = SocketIO(app)
vc = cv2.VideoCapture(0)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

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
