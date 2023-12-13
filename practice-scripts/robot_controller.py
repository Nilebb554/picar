from gpiozero import Robot
import time

robot = Robot(left=(19, 21), right=(24, 26))

def move_forward(speed=0.5, duration=1):
    robot.forward(speed)
    time.sleep(duration)
    robot.stop()

def move_backward(speed=0.5, duration=1):
    robot.backward(speed)
    time.sleep(duration)
    robot.stop()

def move_left(speed=0.5, duration=1):
    robot.left(speed)
    time.sleep(duration)
    robot.stop()

def move_right(speed=0.5, duration=1):
    robot.right(speed)
    time.sleep(duration)
    robot.stop()

try:
    while True:
        move = input("Where to move (forward, backward, left, right, stop): ")
        if move == "forward":
            move_forward()
        elif move == "backward":
            move_backward()
        elif move == "left":
            move_left()
        elif move == "right":
            move_right()
        elif move == "stop":
            robot.stop()
finally:
    robot.stop()
