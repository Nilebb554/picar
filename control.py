import RPi.GPIO as GPIO

MOTOR_LEFT_FORWARD = 26
MOTOR_LEFT_BACKWARD = 24
MOTOR_RIGHT_FORWARD = 21
MOTOR_RIGHT_BACKWARD = 19

def power_up():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)

def power_down():
    GPIO.output(19, 0)
    GPIO.output(21, 0)
    GPIO.output(24, 0)
    GPIO.output(26, 0)
    GPIO.cleanup()

def change_state(state):
    if state["y"] == 1 and state["x"] == 0:
        GPIO.output(MOTOR_RIGHT_FORWARD, 1)
        GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
        GPIO.output(MOTOR_LEFT_FORWARD, 1)
        GPIO.output(MOTOR_LEFT_BACKWARD, 0)
    elif state["y"] == -1 and state["x"] == 0:
        GPIO.output(MOTOR_RIGHT_FORWARD, 0)
        GPIO.output(MOTOR_RIGHT_BACKWARD, 1)
        GPIO.output(MOTOR_LEFT_FORWARD, 0)
        GPIO.output(MOTOR_LEFT_BACKWARD, 1)
    elif state["y"] == 0 and state["x"] == 1:
        GPIO.output(MOTOR_RIGHT_FORWARD, 0)
        GPIO.output(MOTOR_RIGHT_BACKWARD, 1)
        GPIO.output(MOTOR_LEFT_FORWARD, 1)
        GPIO.output(MOTOR_LEFT_BACKWARD, 0)
    elif state["y"] == 0 and state["x"] == -1:
        GPIO.output(MOTOR_RIGHT_FORWARD, 1)
        GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
        GPIO.output(MOTOR_LEFT_FORWARD, 0)
        GPIO.output(MOTOR_LEFT_BACKWARD, 1)
    elif state["y"] == 1 and state["x"] == 1:
        GPIO.output(MOTOR_RIGHT_FORWARD, 0)
        GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
        GPIO.output(MOTOR_LEFT_FORWARD, 1)
        GPIO.output(MOTOR_LEFT_BACKWARD, 0)
    elif state["y"] == 1 and state["x"] == -1:
        GPIO.output(MOTOR_RIGHT_FORWARD, 1)
        GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
        GPIO.output(MOTOR_LEFT_FORWARD, 0)
        GPIO.output(MOTOR_LEFT_BACKWARD, 0)
    elif state["y"] == -1 and state["x"] == 1:
        GPIO.output(MOTOR_RIGHT_FORWARD, 0)
        GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
        GPIO.output(MOTOR_LEFT_FORWARD, 0)
        GPIO.output(MOTOR_LEFT_BACKWARD, 1)
    elif state["y"] == -1 and state["x"] == -1:
        GPIO.output(MOTOR_RIGHT_FORWARD, 0)
        GPIO.output(MOTOR_RIGHT_BACKWARD, 1)
        GPIO.output(MOTOR_LEFT_FORWARD, 0)
        GPIO.output(MOTOR_LEFT_BACKWARD, 0)
    else:
        GPIO.output(MOTOR_RIGHT_FORWARD, 0)
        GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
        GPIO.output(MOTOR_LEFT_FORWARD, 0)
        GPIO.output(MOTOR_LEFT_BACKWARD, 0)
