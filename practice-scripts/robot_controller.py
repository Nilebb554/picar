from gpiozero import Robot
import time

robot = Robot(left=(19, 21), right=(24, 26))

# Move forward
robot.forward()
time.sleep(5)

# Stop
robot.stop()
