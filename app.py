from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import RPi.GPIO as GPIO
from control import change_state, power_up, power_down
from camera_pi import Camera

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

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

def gen(camera):
    while True: 
        frame= camera.get_frame()
        yield (b'--frame\r\n' 
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    vs.release()
    cv2.destroyAllWindows()

@app.route('/video_feed')
def video_feed(): 
   return Response(gen(Camera()), 
                    mimetype='multipart/x-mixed-replace; boundary=frame') 

if __name__ == "__main__":
    socketio.run(app,host="0.0.0.0", port=5000, debug=True, threaded=True)
