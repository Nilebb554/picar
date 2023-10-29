import socketio


sio = socketio.Server()
app = socketio.WSGIApp(sio) #run with gunicorn --threads 50 robot_controller:app maybe
robot_state = {
    "left": 0,
    "right": 0,
    "forward": 0,
    "backward": 0
}

@sio.event
def connect(sid, environ):
    print(sid, "connected")

@sio.event
def connect_error(sid):
    print(sid, "connection failed")

@sio.event
def disconnect(sid):
    print(sid, "disconnected")


@sio.on("get_robot_state")
def get_robot_state(sid, data):
    global robot_state
    robot_state = data
    print(robot_state)