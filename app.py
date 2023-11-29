from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import RPi.GPIO as GPIO
import cv2
from control import change_state, power_up, power_down

app = Flask(__name__)
socketio = SocketIO(app)
vc = cv2.VideoCapture(0) 

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/video')
def video_feed(): 
   """Video streaming route. Put this in the src attribute of an img tag.""" 
   return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame') 

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

def gen(): 
   """Video streaming generator function.""" 
   try: 
        import picamera
    except ImportError:
        print("Picamera errror: Help me plz")
        return

   while True: 
       rval, frame = vc.read() 
       cv2.imwrite('pic.jpg', frame) 
       yield (b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' + open('pic.jpg', 'rb').read() + b'\r\n')

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
