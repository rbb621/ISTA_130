'''
Name: Ricky Berliant
Date: 9/10/25
Class: ISTA130
Section Leader: ???

Description: This module draws a teal equilateral triangle using the turtle module.
'''

import turtle


def rectangle(a_turtle, width, height):
    a_turtle.pendown()
    a_turtle.fillcolor("orange")
    a_turtle.begin_fill()
    a_turtle.setheading(0)
    a_turtle.forward(width)
    a_turtle.left(90)
    a_turtle.forward(height)
    a_turtle.left(90)
    a_turtle.forward(width)
    a_turtle.left(90)
    a_turtle.forward(height)
    a_turtle.end_fill()
    

def main():
    
    # create a turtle
    tallulah = turtle.Turtle()
    tallulah.pencolor('orange')
    tallulah.pensize(5)
    tallulah.speed(0)
    tallulah.shape('turtle')
    
    rectangle(tallulah, 200, 100)
    
    # once the turtle is finished
    tallulah.hideturtle()
    turtle.done()
    turtle.getscreen().exitonclick()
    

    

if __name__ == "__main__":
    main()

