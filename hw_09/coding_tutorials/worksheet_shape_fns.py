'''
Author: Rich Thompson
Date: Today
Class: ISTA 130
Section Leader: Me

Description:
This program draws a dodecagon and also includes code for a nonagon.
'''

import turtle
        
def dodecagon(roscoe, side):
    '''
    This function draws a dodecagon with side length side using
    turtle harold.  It leaves the turtle in the same state it was in 
    before the function.  It returns None.
    '''
    roscoe.fd(side)
    roscoe.lt(360 / 12)
    roscoe.fd(side)
    roscoe.lt(30)
    roscoe.fd(side)
    roscoe.lt(30)
    roscoe.fd(side)
    roscoe.lt(30)
    roscoe.fd(side)
    roscoe.lt(30)
    roscoe.fd(side)
    roscoe.lt(30)
    roscoe.fd(side)
    roscoe.lt(30)
    roscoe.fd(side)
    roscoe.lt(30)
    roscoe.fd(side)
    roscoe.lt(30)
    roscoe.fd(side)
    roscoe.lt(30)
    roscoe.fd(side)
    roscoe.lt(30)
    roscoe.fd(side)
    roscoe.lt(30)
    
def nonagon(roscoe, side):
    '''
    This function draws a nonagon with side length side using
    turtle harold.  It leaves the turtle in the same state it was in 
    before the function.  It returns None.
    '''
    roscoe.fd(side)
    roscoe.lt(360 / 9)
    roscoe.fd(side)
    roscoe.lt(360 / 9)
    roscoe.fd(side)
    roscoe.lt(360 / 9)
    roscoe.fd(side)
    roscoe.lt(360 / 9)
    roscoe.fd(side)
    roscoe.lt(360 / 9)
    roscoe.fd(side)
    roscoe.lt(360 / 9)
    roscoe.fd(side)
    roscoe.lt(360 / 9)
    roscoe.fd(side)
    roscoe.lt(360 / 9)
    roscoe.fd(side)
    roscoe.lt(360 / 9)
    
    
#==========================================================
def main():
    ''' Draw a dodecagon '''
    
    rocket = turtle.Turtle()
    rocket.shape('turtle')
    rocket.pensize(5)
    rocket.speed(0)
    turtle.bgcolor('black')
    rocket.pencolor('red')
    
    rocket.fd(300)
    rocket.bk(600)
    rocket.fd(100)
    
    dodecagon(rocket, 20)
    
    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
