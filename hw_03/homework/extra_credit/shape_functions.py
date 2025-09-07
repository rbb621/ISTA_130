'''
Name: Ricky Berliant
Date: 9/10/25
Class: ISTA130
Section Leader: ???

Description: This module draws a dodecagon shape and nonagon shape using the turtle module.
'''

import turtle

# Dodecagon Shape
def dodecagon(a_turtle, length, angle):
    a_turtle.pendown()
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.penup()

# Nonagon Shape
def nonagon(a_turtle, length, angle):
    a_turtle.pendown()
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.forward(length)
    a_turtle.right(angle)
    a_turtle.penup()

def main():
    tallulah = turtle.Turtle()
    tallulah.pencolor('green')
    tallulah.pensize(10)
    tallulah.speed(0)
    tallulah.shape('turtle')

    # Dodecagon Shape with 12 sides and 30 degrees
    dodecagon(tallulah, 30, 30)
    
    # Moves the turtle, so the shapes don't overlap
    tallulah.goto(150, 0)
    
    # Nonagon Shape with 9 sides and 40 degrees
    nonagon(tallulah, 40, 40)

    # Once both the shapes are drawn
    tallulah.hideturtle()
    turtle.done()
    tallulah.getscreen().exitonclick()

if __name__ == "__main__":
    main()
