import math

def advanced_tank_drive(x, y):
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

def simple_tank_drive(x, y): 
    
    max_speed = 100 
    left_speed = max_speed * (y + x)
    right_speed = max_speed * (y - x)

    left_speed = max(min(left_speed, max_speed), -max_speed)
    right_speed = max(min(right_speed, max_speed), -max_speed)

    print("Right Speed:", right_speed)
    print("Left Speed:", left_speed)


x = 1
y =1
simple_tank_drive(x, y)