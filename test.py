from gpiozero import Motor
import time

GPIO.cleanup()

motor1 = Motor(24, 26)
motor2 = Motor(19, 21)

def test():
    motor1.forward()
    time.sleep(3)
    print("DONE")

test()
