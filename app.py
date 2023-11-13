from flask import Flask, render_template
from flask_socketio import SocketIO
try:
    from control import change_state
except (RuntimeError, ImportError) as e:
    print(f"Error importing control module: {e}")
    change_state = None

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

@socketio.on("connect")
def connect():
    print("Client connected")

@socketio.on("disconnect")
def disconnect():
    print("Client disconnected")

@socketio.on("keyState")
def handle_keyState(keyState):
    print(keyState)
    try:
        change_state(keyState)
    except:
        print(keyState)

if __name__ == "__main__":
    socketio.run(app)
