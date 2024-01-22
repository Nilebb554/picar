def tank_drive(x, y):
    if x == 0:
        left_speed = y * 100
        right_speed = y * 100
    else:
        left_speed = y * 100 + x * 100
        right_speed = y * 100 - x * 100
    
    left_speed = max(min(left_speed, 100), -100)
    right_speed = max(min(right_speed, 100), -100)
    
    print(right_speed, left_speed)



x = -1
y = 0
tank_drive(x, y)

