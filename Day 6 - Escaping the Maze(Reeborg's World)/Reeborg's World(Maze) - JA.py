def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()    

def jump():
    turn_left()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() == True:
        move()
    turn_left()
    
    
while at_goal() == False:
    while right_is_clear():
        turn_right()
        move()
    if front_is_clear():
        move()
    else:
        turn_left()
        if front_is_clear():
            move()
        else:
            continue
            
#Day 6
#Escaping the Maze(Reeborg's World)
#100DaysOfCode
#Angela Yu
#Joseph Adoga