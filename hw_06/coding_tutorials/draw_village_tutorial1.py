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
import random 

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

def color_chooser():
    possible_colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
    chosen_color = random.choice(possible_colors)
    return chosen_color

def move_between_houses(a_turtle, house_size, dist_between_houses):
    a_turtle.penup()
    a_turtle.forward(house_size + dist_between_houses)
    a_turtle.pendown()

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
    tallulah.speed(0)
    tallulah.width(5)
    tallulah.penup()
    tallulah.back(300)
    tallulah.pendown()

    house_size = 100
    house_spacing = 50
    for i in range(4):
        current_house_size = house_size * random.randrange(1,8,1)/4
        random_color = color_chooser()
        tallulah.pencolor(random_color)
        house(tallulah, current_house_size)
        move_between_houses(tallulah, current_house_size, house_spacing * random.randrange(1,4,1)/2)
    
    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
