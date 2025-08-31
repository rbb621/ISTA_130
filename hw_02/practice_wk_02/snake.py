'''
Author: Ricky Berliant
Date: 9/1/2025
Class: ISTA 130
Section Leader: NA

Description:
This program will use a turtle from the turtle module to write 'HELLO'
'''

# put all of your import statements below this line and then delete this comment
import turtle

# put all of your function definitions below this line and then delete this comment



#==========================================================

    

def main():
    '''
    Writes the world 'HELLO' using a turtle
    '''
    # Initiate turtle
    solid_snake = turtle.Turtle()
    
    # Change turtle properties
    solid_snake.shape('turtle')
    solid_snake.pensize(10)
    solid_snake.pencolor('black')
    solid_snake.speed(0)

    solid_snake.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
    

def triangle(solid_snake, 100):
def pentagon(solid_snake, 100):
def square(solid_snake, 100):
def hexagon(solid_snake, 100):