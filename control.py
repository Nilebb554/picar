import RPi.GPIO as GPIO

MOTOR_LEFT_FORWARD = 26
MOTOR_LEFT_BACKWARD = 24
MOTOR_RIGHT_FORWARD = 21
MOTOR_RIGHT_BACKWARD = 19

def change_state(state):
    count_ones = sum(1 for value in state.values() if value == 1)
    if count_ones == 1:
        if state["forward"] == 1:
            GPIO.output(MOTOR_RIGHT_FORWARD, 1)
            GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
            GPIO.output(MOTOR_LEFT_FORWARD, 1)
            GPIO.output(MOTOR_LEFT_BACKWARD, 0)
        elif state["backward"] == 1:
            GPIO.output(MOTOR_RIGHT_FORWARD, 0)
            GPIO.output(MOTOR_RIGHT_BACKWARD, 1)
            GPIO.output(MOTOR_LEFT_FORWARD, 0)
            GPIO.output(MOTOR_LEFT_BACKWARD, 1)
        elif state["right"] == 1:
            GPIO.output(MOTOR_RIGHT_FORWARD, 1)
            GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
            GPIO.output(MOTOR_LEFT_FORWARD, 0)
            GPIO.output(MOTOR_LEFT_BACKWARD, 1)
        elif state["left"] == 1:
            GPIO.output(MOTOR_RIGHT_FORWARD, 0)
            GPIO.output(MOTOR_RIGHT_BACKWARD, 1)
            GPIO.output(MOTOR_LEFT_FORWARD, 1)
            GPIO.output(MOTOR_LEFT_BACKWARD, 0)
    elif count_ones == 2:
        if state["forward"] == 1 and state["left"] == 1:
            GPIO.output(MOTOR_RIGHT_FORWARD, 1)
            GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
            GPIO.output(MOTOR_LEFT_FORWARD, 0)
            GPIO.output(MOTOR_LEFT_BACKWARD, 0)
        elif state["forward"] == 1 and state["right"] == 1:
            GPIO.output(MOTOR_RIGHT_FORWARD, 0)
            GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
            GPIO.output(MOTOR_LEFT_FORWARD, 1)
            GPIO.output(MOTOR_LEFT_BACKWARD, 0)
        elif state["backward"] == 1 and state["left"] == 1:
            GPIO.output(MOTOR_RIGHT_FORWARD, 0)
            GPIO.output(MOTOR_RIGHT_BACKWARD, 1)
            GPIO.output(MOTOR_LEFT_FORWARD, 0)
            GPIO.output(MOTOR_LEFT_BACKWARD, 0)
        elif state["backward"] == 1 and state["right"] == 1:
            GPIO.output(MOTOR_RIGHT_FORWARD, 0)
            GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
            GPIO.output(MOTOR_LEFT_FORWARD, 0)
            GPIO.output(MOTOR_LEFT_BACKWARD, 1)
        else:
            GPIO.output(MOTOR_RIGHT_FORWARD, 0)
            GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
            GPIO.output(MOTOR_LEFT_FORWARD, 0)
            GPIO.output(MOTOR_LEFT_BACKWARD, 0)
    elif count_ones == 3:
        print("count_ones = 3")
        if state["forward"] == 1 and state["backward"] == 1:
            if state["right"] == 1:
                GPIO.output(MOTOR_RIGHT_FORWARD, 1)
                GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
                GPIO.output(MOTOR_LEFT_FORWARD, 0)
                GPIO.output(MOTOR_LEFT_BACKWARD, 1)
            elif state["left"] == 1:
                GPIO.output(MOTOR_RIGHT_FORWARD, 0)
                GPIO.output(MOTOR_RIGHT_BACKWARD, 1)
                GPIO.output(MOTOR_LEFT_FORWARD, 1)
                GPIO.output(MOTOR_LEFT_BACKWARD, 0)
        elif state["right"] == 1 and state["left"] == 1:
            if state["forward"] == 1:
                GPIO.output(MOTOR_RIGHT_FORWARD, 1)
                GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
                GPIO.output(MOTOR_LEFT_FORWARD, 1)
                GPIO.output(MOTOR_LEFT_BACKWARD, 0)
            elif state["backward"] == 1:
                GPIO.output(MOTOR_RIGHT_FORWARD, 0)
                GPIO.output(MOTOR_RIGHT_BACKWARD, 1)
                GPIO.output(MOTOR_LEFT_FORWARD, 0)
                GPIO.output(MOTOR_LEFT_BACKWARD, 1) 
    elif count_ones == 4:
        GPIO.output(MOTOR_RIGHT_FORWARD, 0)
        GPIO.output(MOTOR_RIGHT_BACKWARD, 0)
        GPIO.output(MOTOR_LEFT_FORWARD, 0)
        GPIO.output(MOTOR_LEFT_BACKWARD, 0)
