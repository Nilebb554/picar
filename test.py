from gpiozero import Robot
import time

robot = Robot(left=(24, 26), right=(19, 21))

def test():
    robot.forward()
    time.sleep(3)
    print("DONE")

test()
