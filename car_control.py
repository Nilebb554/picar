import RPi.GPIO as GPIO
import keyboard

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

#When left arrow down
def on_left_arrow(event):
    if event.event_type == keyboard.KEY_DOWN:
        move_left()

#When right arrow down
def on_right_arrow(event):
    if event.event_type == keyboard.KEY_DOWN:
        move_right()

#When up arrow down
def on_up_arrow(event):
    if event.event_type == keyboard.KEY_DOWN:
        move_forward()

#When down arrow down
def on_down_arrow(event):
    if event.event_type == keyboard.KEY_DOWN:
        move_backward()

keyboard.on_press_key("left", on_left_arrow)
keyboard.on_press_key("right", on_right_arrow)
keyboard.on_press_key("up", on_up_arrow)
keyboard.on_press_key("down", on_down_arrow)

keyboard.on_release_key("left", power_off)
keyboard.on_release_key("right", power_off)
keyboard.on_release_key("up", power_off)
keyboard.on_release_key("down", power_off)

keyboard.wait("esc")

power_off()
