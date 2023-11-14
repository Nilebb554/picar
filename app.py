from flask import Flask, render_template
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
url_for('static', filename='style.css')

@app.route('/')
def hello_world():
    return render_template("index.html")

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
