'''
Author: Dan Charbonneau
Date: 1/21/2022
Class: ISTA 130
Section Leader: ME!

Description:
Draws a house using turtles. Uses functions to draw shapes (square, triangle, rectangle), and implements these into a house() function
'''

# put all of your import statements below this line and then delete this comment
import turtle

# put all of your function definitions below this line and then delete this comment
def triangle(a_turtle, side_len):
    a_turtle.forward(side_len)
    a_turtle.left(120)
    a_turtle.forward(side_len)
    a_turtle.left(120)
    a_turtle.forward(side_len)
    a_turtle.left(120)
    return None

def rectangle(a_turtle, width, height):
    a_turtle.forward(width)
    a_turtle.left(90)
    a_turtle.forward(height)
    a_turtle.left(90)
    a_turtle.forward(width)
    a_turtle.left(90)
    a_turtle.forward(height)
    a_turtle.left(90)
    return None

def square(a_turtle, side_len):
    rectangle(a_turtle, side_len, side_len)

def house(a_turtle, side_len):
    # Draw square (house walls)
    square(a_turtle, side_len)
    
    # Relocate to upper left side of square; positioned to draw roof
    a_turtle.penup()
    a_turtle.left(90)
    a_turtle.forward(side_len)
    a_turtle.right(90)
    a_turtle.pendown()

    # Draw triangle (roof)
    triangle(a_turtle, side_len)
    
    # Relocate to middle bottom of house; positioned to draw door
    a_turtle.penup()
    a_turtle.right(90)
    a_turtle.forward(side_len)
    a_turtle.left(90)
    a_turtle.forward(side_len/2)
    a_turtle.pendown()   
    
    # Draw rectangle (door)
    rectangle(a_turtle, side_len/4, side_len/2)
    
    a_turtle.penup()
    a_turtle.back(side_len/2)
    a_turtle.pendown()
    return None


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    tallulah = turtle.Turtle()

    # modify turtle attributes
    tallulah.shape('turtle')
    tallulah.pencolor('orange')
    tallulah.width(5)

    house(tallulah, 100)
    tallulah.penup()
    tallulah.forward(150)
    tallulah.pendown()
    house(tallulah, 50)
        

    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
