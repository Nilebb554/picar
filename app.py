from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import RPi.GPIO as GPIO
import picamera
import cv2

from control import change_state, power_up, power_down
from camera_opencv import generate_frames

app = Flask(__name__)
socketio = SocketIO(app)
camera = PiCamera()

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

def generate_frames():
    while True:
        # Capture an image from the PiCamera
        frame = capture_frame()

        # Encode the frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # Yield the frame in the required format
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

def capture_frame():
    # Capture an image from the PiCamera
    frame = None
    with PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.capture('/tmp/frame.jpg')  # Capture to a temporary file
        frame = cv2.imread('/tmp/frame.jpg')

    return frame

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
