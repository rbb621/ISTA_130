'''
Author: Ricky Berliant
Date: 9/3/2025
Class: ISTA 130
Section Leader: ???

Description:
Problem 3: Players choice!

Draw a Japan flag
'''

import turtle

def cherry_blossom(japan, x, y, size):
    japan.penup()
    japan.goto(x, y)
    japan.pendown()
    japan.pencolor("pink")
    japan.forward(size)
    

def main():
    '''
    Drawing a Japan flag with cherry blossoms
    '''
    
    # create the turtle
    japan = turtle.Turtle()
    japan.speed(0)

    # colors
    japan.pensize(10)
    japan.pencolor("red")
    
    # set position
    japan.goto(0, -80)
    japan.fillcolor("red")
    japan.begin_fill()
    japan.circle(100)
    japan.end_fill()
    

    japan.hideturtle()
    
    cherry_blossom(japan, -220, 72, 40)
    cherry_blossom(japan, 72, -220, 40)
    cherry_blossom(japan, -220, 72, 40)
    cherry_blossom(japan, 72, -220, 40)
    


    turtle.getscreen().exitonclick()  
    turtle.done()


if __name__ == '__main__':
    main()
