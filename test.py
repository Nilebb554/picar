import time, RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

time.sleep(3)
#19 = Motor1 backward
#21 = Motor1 forward

#24 = Motor0 backward
#26 = Motor0 forward



GPIO.output(19, 0)
GPIO.output(21, 0)

GPIO.output(24, 0)
GPIO.output(26, 0)

time.sleep(3)

GPIO.cleanup()
