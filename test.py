from gpiozero import Robot
import time

robot = Robot(left=(21, 26), right=(19,24))

time.sleep(5)

robot.forward()

time.sleep(5)
