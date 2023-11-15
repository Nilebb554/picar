from flask import Flask, render_template, Response
import cv2

from flask_socketio import SocketIO
try:
    import RPi.GPIO as GPIO
    from control import change_state, power_up, power_down
except (RuntimeError, ImportError) as e:
    print(f"Error importing control module: {e}")
    change_state = None
    power_up = None
    power_down = None

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

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@socketio.on("connect")
def connect():
    if callable(power_up):
        power_up()
    print("Client connected")

@socketio.on("disconnect")
def disconnect():
    if callable(power_down):
        power_down()
    print("Client disconnected")

@socketio.on("keyState")
def handle_keyState(keyState):
    print(keyState)
    try:
        change_state(keyState)
    except:
        print(keyState)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
