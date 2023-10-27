import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

#Power the car down
def power_off():
    GPIO.output(19, 0)
    GPIO.output(21, 0)
    GPIO.output(24, 0)
    GPIO.output(26, 0)
    GPIO.cleanup()

#Move car right
def move_right():
    GPIO.output(21, 0)
    GPIO.output(19, 1)
    GPIO.output(26, 1)
    GPIO.output(24, 0)

#Move car left
def move_left():
    GPIO.output(21, 1)
    GPIO.output(19, 0)
    GPIO.output(26, 0)
    GPIO.output(24, 1)


#Move car forward
def move_forward():
    GPIO.output(21, 0)
    GPIO.output(19, 1)
    GPIO.output(26, 1)
    GPIO.output(24, 0)

#Move car backward
def move_backward():
    GPIO.output(21, 1)
    GPIO.output(19, 0)
    GPIO.output(26, 0)
    GPIO.output(24, 1)

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
    power_off()
