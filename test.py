from gpiozero import Robot
import time

robot = Robot(left=(24, 26), right=(19, 21))

GPIO
def test():
    robot.forward()
    time.sleep(3)
    robot.backward()
    time.sleep(3)
    robot.left()
    time.sleep(3)
    robot.right()
    time.sleep(3)
    robot.stop()
    print("DONE")

test()
