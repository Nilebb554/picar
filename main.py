from gpiozero import Robot
import time

robot = Robot((24, 26), (19, 21))

def test():
  robot.forward()
  sleep(3)
  robot.backward()
  sleep(3)
  robot.left()
  sleep(3)
  robot.right()
  sleep(3)
  robot.stop()
