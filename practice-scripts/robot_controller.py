from gpiozero import Robot
import time

robot = Robot(left=(19, 21), right=(24, 26))

# Move backward
robot.backward()
time.sleep(5)  # Adjust the sleep duration as needed

# Stop for a moment
robot.stop()
time.sleep(1)

# Move forward
robot.forward()
time.sleep(5)  # Adjust the sleep duration as needed

# Stop at the end
robot.stop()
