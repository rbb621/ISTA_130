'''
Name: Sarah Stueve
Date: 1/26/20
Class: ISTA130
Section Leader: I'm the (wo)man

Description: This module draws a teal equilateral triangle using the turtle module.
'''

# Make sure to import turtle!
import turtle

# Define your function
def triangle(a_turtle, side_len):
    '''
    This function draws an equilateral triangle.
    Parameters:
        :a_turtle: a turtle object
        :side_len: int, length of a side in triangle
    Returns:
        None
    '''
    a_turtle.forward(120)
    a_turtle.left(120)  
    a_turtle.forward(120)
    a_turtle.left(120)
    a_turtle.forward(120)
    a_turtle.left(120)

# Create your turtle and call your function in main!
def main():
    '''
    This module creates a turtle and draws a teal equilateral triangle.
    '''
    tallulah = turtle.Turtle()
    tallulah.pencolor('teal')
    tallulah.pensize(10)
    triangle(tallulah, 100)

    turtle.getscreen().exitonclick() # Keeps the window open

if __name__ == "__main__":
    main()