from gpiozero import Motor
import RPi.GPIO as GPIO
import time

time.sleep(5)

motor1 = Motor(21, 26)
motor2 = Motor(19, 24)

def test():
    motor1.forward()
    time.sleep(3)
    print("DONE")

test()
