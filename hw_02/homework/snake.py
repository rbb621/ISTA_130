'''
Author: Ricky Berliant
Date: 9/1/2025
Class: ISTA 130
Section Leader: ???

Description:
This program use the turtle module to draw a snake using four shapes: 
Triangle, Square, Hexagon, and Pentagon.
'''

import turtle

# Draw a Triangle (used as a tail)
def triangle(solid_snake, side):
    solid_snake.pencolor('Teal')
    solid_snake.pendown()
    
    # side 1
    solid_snake.right(90)
    solid_snake.forward(side)
    
    # side 2
    solid_snake.right(120)
    solid_snake.forward(side)
    
    # side 3
    solid_snake.right(120)
    solid_snake.forward(side)


# Draw a Square (body)
def square(solid_snake, side):
    solid_snake.pencolor('Olive')
    solid_snake.pendown()
    
    # side 1
    solid_snake.right(90)
    solid_snake.forward(side)
    
    # side 2
    solid_snake.left(90)
    solid_snake.forward(side)
    
    # side 3
    solid_snake.left(90)
    solid_snake.forward(side)
    
    # side 4
    solid_snake.left(90)
    solid_snake.forward(side)

# Draw a Pentagon (body)
def pentagon(solid_snake, side):
    solid_snake.pencolor('MediumSeaGreen')
    solid_snake.pendown()
    
    # side 1
    solid_snake.right(90)
    solid_snake.forward(side)
    
    # side 2
    solid_snake.left(72)
    solid_snake.forward(side)
    
    # side 3
    solid_snake.left(72)
    solid_snake.forward(side)
    
    # side 4
    solid_snake.left(72)
    solid_snake.forward(side)
    
    # side 5
    solid_snake.left(72)
    solid_snake.forward(side)
    

# Draw a Hexagon (head or face)
def hexagon(solid_snake, side):
    solid_snake.pencolor('DarkViolet')
    solid_snake.pendown()
    
    # side 1
    solid_snake.forward(side)
    solid_snake.left(60)

    # side 2
    solid_snake.forward(side)
    solid_snake.left(60)

    # side 3
    solid_snake.forward(side)
    solid_snake.left(60)

    # side 4
    solid_snake.forward(side)
    solid_snake.left(60)

    # side 5
    solid_snake.forward(side)
    solid_snake.left(60)

    # side 6
    solid_snake.forward(side)
    solid_snake.left(60)

    solid_snake.penup()


# moving the turtle, while connecting the shapes as body parts
def jump(solid_snake, moving):
    
    # Snake always faces east
    solid_snake.setheading(0)
    solid_snake.penup()
    solid_snake.forward(moving)

def main():
    '''
    Setting up the Snake!
    '''
    solid_snake = turtle.Turtle()
    solid_snake.pensize(10)
    solid_snake.speed(0)
    solid_snake.shape('turtle')

    # Move to starting point
    solid_snake.penup()
    solid_snake.goto(-250, 0)

    # Draw snake body in a straight line
    # jump - mainly used for spacing
    # Parameters (solid_snake = turtle, side = length of the sides)
    triangle(solid_snake, 100)
    jump(solid_snake, 10)   

    square(solid_snake, 100)
    jump(solid_snake, 110)

    pentagon(solid_snake, 75)
    jump(solid_snake, 100)

    square(solid_snake, 100)
    jump(solid_snake, 110)

    pentagon(solid_snake, 75)
    jump(solid_snake, 100)

    square(solid_snake, 100)
    jump(solid_snake, 70)

    hexagon(solid_snake, 65)

    # Once I am done with drawing the snake
    solid_snake.hideturtle()
    turtle.done()
    solid_snake.getscreen().exitonclick()

if __name__ == '__main__':
    main()

