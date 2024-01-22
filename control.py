import RPi.GPIO as GPIO
import math
import time

LF = 26
LB = 24
RF = 21
RB = 19

def power_up():
    global lf_pwm, lb_pwm, rf_pwm, rb_pwm
    GPIO.setup(LF, GPIO.OUT)
    lf_pwm = GPIO.PWM(LF, 20)
    lf_pwm.start(0)

    GPIO.setup(LB, GPIO.OUT)
    lb_pwm = GPIO.PWM(LB, 20)
    lb_pwm.start(0)

    GPIO.setup(RF, GPIO.OUT)
    rf_pwm = GPIO.PWM(RF, 20)
    rf_pwm.start(0)

    GPIO.setup(RB, GPIO.OUT)
    rb_pwm = GPIO.PWM(RB, 20)
    rb_pwm.start(0)

def power_down():
    lf_pwm.stop()
    lb_pwm.stop()
    rf_pwm.stop()
    rb_pwm.stop()
    GPIO.cleanup()

def calculate_motor_speeds(x, y): 
    import math

def tank_drive(x, y):
    if x == 0 and y == 0:
        left_speed = 0
        right_speed = 0
    else:
        z = math.sqrt(x * x + y * y)
        rad = math.acos(math.fabs(x) / z)
        angle = rad * 180 / math.pi

        tcoeff = -1 + (angle / 90) * 2
        turn = tcoeff * math.fabs(math.fabs(y) - math.fabs(x))
        turn = round(turn * 100, 0) / 100

        mov = max(math.fabs(y), math.fabs(x))

        if (x >= 0 and y >= 0) or (x < 0 and y < 0):
            left_speed = mov
            right_speed = turn
        else:
            right_speed = mov
            left_speed = turn

        if y < 0:
            left_speed = 0 - left_speed
            right_speed = 0 - right_speed

        left_speed = max(min(left_speed, 100), -100)
        right_speed = max(min(right_speed, 100), -100)

    print("Right Speed:", right_speed*100)
    print("Left Speed:", left_speed*100)


    return left_speed*100, right_speed*100

def change_motor_speeds(state):
    #convert it to number between -100 and 100
    left_speed, right_speed = calculate_motor_speeds(state["x"], state["y"])

    if left_speed > 0:
        lf_pwm.ChangeDutyCycle(left_speed)
        lb_pwm.ChangeDutyCycle(0)
    elif left_speed < 0:
        lf_pwm.ChangeDutyCycle(0)
        lb_pwm.ChangeDutyCycle(left_speed)
    else:
        lf_pwm.ChangeDutyCycle(0)
        lb_pwm.ChangeDutyCycle(0)

    if right_speed > 0:
        rf_pwm.ChangeDutyCycle(right_speed)
        rb_pwm.ChangeDutyCycle(0)
    elif right_speed < 0:
        rf_pwm.ChangeDutyCycle(0)
        rb_pwm.ChangeDutyCycle(right_speed)
    else:
        rf_pwm.ChangeDutyCycle(0)
        rb_pwm.ChangeDutyCycle(0)
