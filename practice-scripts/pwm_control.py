import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

pwm_motor1_forward = GPIO.PWM(21, 50)
pwm_motor1_backward = GPIO.PWM(19, 50)

pwm_motor2_forward = GPIO.PWM(26, 50)
pwm_motor2_backward = GPIO.PWM(24, 50)

#Power the car down
def power_off():
    GPIO.output(19, 0)
    GPIO.output(21, 0)
    GPIO.output(24, 0)
    GPIO.output(26, 0)

def move_forward(speed=50):
    pwm_motor1_backward.stop()
    pwm_motor1_forward.start(speed)
    pwm_motor2_backward.stop()
    pwm_motor2_forward.start(speed)
    time.sleep(0.2)
    power_off()

def move_backward(speed=50): 
    pwm_motor1_forward.stop()
    pwm_motor1_backward.start(speed)
    pwm_motor2_forward.stop()
    pwm_motor2_backward.start(speed)
    time.sleep(0.2)
    power_off()

def move_right(speed=50):
    pwm_motor1_forward.stop()
    pwm_motor1_backward.start(speed)
    pwm_motor2_forward.start(speed)
    pwm_motor2_forward.stop()
    time.sleep(0.2)
    power_off()

def move_left(speed=50):
    pwm_motor1_forward.start(speed)
    pwm_motor1_backward.stop()
    pwm_motor2_forward.stop()
    pwm_motor2_forward.start(speed)
    time.sleep(0.2)
    power_off()

while True:
    move = input("Where move")
    if move == "left":
        move_left()
    elif move == "right":
        move_right()
    elif move == "forward":
        move_forward()
    elif move == "backward":
        move_backward()

GPIO.cleanup()