import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

from gpiozero import Robot
import time

robot = Robot(left=(21, 26), right=(19, 24))

time.sleep(3)

robot.forward()

time.sleep(3)

robot.backward()

time.sleep(3)

robot.stop()

time.sleep(3)

robot.right()

time.sleep(3)

robot.left()

time.sleep(3)

robot.stop()

robot.close()
