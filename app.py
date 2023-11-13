from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

def change_state(state):
    if len(state) == 1:
        print("KeyState = 1")
    elif len(state) == 2:
        print("KeyState = 2")
    elif len(state) == 3:
        print("KeyState = 3")
    elif len(state) == 4:
        print("KeyState = 4")


@socketio.on("connect")
def connect():
    print("Client connected")

@socketio.on("disconnect")
def disconnect():
    print("Client disconnected")

@socketio.on("keyState")
def handle_keyState(keyState):
    change_state(keyState)

if __name__ == "__main__":
    socketio.run(app, debug = True)
