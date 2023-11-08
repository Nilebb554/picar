from gpiozero import Robot
import time

robot = Robot(left=(19, 21), right=(24, 26))

robot.left()
time.sleep(10)
robot.right()
time.sleep(10)
robot.stop()
time.sleep(1)
