from gpiozero import Motor
import RPi.GPIO as GPIO
import time

time.sleep(5)

motor1 = Motor(21, 26)
motor2 = Motor(19, 24)
print("1")
def test():
    print("2")
    motor1.forward()
    print("3")
    time.sleep(3)
    print("DONE")

test()
