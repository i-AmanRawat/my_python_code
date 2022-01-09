def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
def jump():
    turn_left()
    move()
    turn_right()
 
while (at_goal()!=True):
    
    if (wall_in_front()==True):
        turn_left()
    
    elif (front_is_clear()==True):
        move()
        turn_right()


