import RPi.GPIO as GPIO

LF = 26
LB = 24
RF = 21
RB = 19

lf_pwm = None
lb_pwm = None
rf_pwm = None
rb_pwm = None

def power_up():
    global lf_pwm, lb_pwm, rf_pwm, rb_pwm

    GPIO.setmode(GPIO.BOARD)
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
    global lf_pwm, lb_pwm, rf_pwm, rb_pwm
    lf_pwm.stop()
    lb_pwm.stop()
    rf_pwm.stop()
    rb_pwm.stop()
    GPIO.cleanup()

def simple_calculate_motor_speeds(x, y): 
    max_speed = 100

    left_speed = max_speed * y
    right_speed = max_speed * y

    left_speed = max(min(left_speed, max_speed), -max_speed)
    right_speed = max(min(right_speed, max_speed), -max_speed)

    if y == 0:
        if x > 0:
            left_speed = x*100
            right_speed = -x*100
        elif x < 0:
            left_speed = x*100
            right_speed = -x*100
    else:
        if x > 0:
            right_speed *= (1 - x)
        elif x < 0:
            left_speed *= (1 + x)
         
    return left_speed, right_speed

def change_motor_speeds(data):
    global lf_pwm, lb_pwm, rf_pwm, rb_pwm
    
    #convert it to number between -100 and 100
    
    x = data["x"]
    y = data["y"]
    
    left_speed, right_speed = simple_calculate_motor_speeds(x, y)
    
    if left_speed >= 0:
        lf_pwm.ChangeDutyCycle(left_speed)
        lb_pwm.ChangeDutyCycle(0)
    elif left_speed <= 0:
        lf_pwm.ChangeDutyCycle(0)
        lb_pwm.ChangeDutyCycle(-left_speed)
    else:
        lf_pwm.ChangeDutyCycle(0)
        lb_pwm.ChangeDutyCycle(0)

    if right_speed >= 0:
        rf_pwm.ChangeDutyCycle(right_speed)
        rb_pwm.ChangeDutyCycle(0)
    elif right_speed <= 0:
        rf_pwm.ChangeDutyCycle(0)
        rb_pwm.ChangeDutyCycle(-right_speed)
    else:
        rf_pwm.ChangeDutyCycle(0)
        rb_pwm.ChangeDutyCycle(0)
