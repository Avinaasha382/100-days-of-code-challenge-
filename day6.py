# Day-6: I learnt how to declare Python functions and nested functions in Python

#Todays project was through Reeborg's world a online platform where you have to write Python code to navigate through different 
# hurdles and mazes. It was interesting to tackle Hurdle level 1,2,3,4 and the final maze level. Since it was an online page
# I put in this python file the functions I wrote as a practise
# Hurdles 2,3,4:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    '''turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()'''
    count=0
    while front_is_clear()==False:
        turn_left()
        move()
        turn_right()
        count+=1
    move()
    turn_right()
    while count>0:
        move()
        count-=1
    turn_left()
    
while at_goal()==False:
    if right_is_clear()==True:
        turn_right()
        move()
    elif wall_in_front()==False:
        move()
    else:
        turn_left()
        
# Maze 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    '''turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()'''
    count=0
    while front_is_clear()==False:
        turn_left()
        move()
        turn_right()
        count+=1
    move()
    turn_right()
    while count>0:
        move()
        count-=1
    turn_left()
    
while at_goal()==False:
    if right_is_clear()==True:
        turn_right()
        move()
    elif wall_in_front()==False:
        move()
    else:
        turn_left()
        

