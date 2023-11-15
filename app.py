from flask import Flask, render_template,Response
from flask_socketio import SocketIO
import cv2


app = Flask(__name__)
socketio = SocketIO(app)

camera = None  # Initialize the camera as None

def init_camera():
    global camera
    try:
        camera = cv2.VideoCapture(0)
        # Additional camera initialization code if needed
    except:
        print("Error initializing camera")

def generate_frames():
    while True:
        if camera:
            # If the camera is initialized, read frames
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
        else:
            # If the camera is not available, create a placeholder frame
            frame = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00\x96\x00\x96\x00\x00'

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@socketio.on("connect")
def connect():
    print("Client connected")

@socketio.on("disconnect")
def disconnect():
    print("Client disconnected")



if __name__ == "__main__":
    init_camera()  # Initialize the camera before running the app
    socketio.run(app)
