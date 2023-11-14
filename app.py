from flask import Flask, render_template
from flask_socketio import SocketIO
import RPi.GPIO as GPIO
from control import change_state, power_up, power_down

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

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
