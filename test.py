from gpiozero import Motor
import RPi.GPIO as GPIO
import time

GPIO.cleanup()

motor1 = Motor(21, 26)
motor2 = Motor(19, 24)

def test():
    motor1.forward()
    time.sleep(3)
    print("DONE")

test()
