import math
import turtle

def rectangle(torty, width, height):
    torty.forward(height)
    torty.right(90)
    torty.forward(width)
    torty.right(90)
    torty.forward(height)
    torty.right(90)
    torty.forward(width)
    torty.right(90)


def square(torty, size):
    for i in range(size):
        torty.right(size/2)
    

def triangle(torty, size):
    for i in range(size):
        torty.right(45)

def house(torty, size, x, y):
    torty.penup()
    torty.goto(x, y)
    torty.pendown()
    torty.setheading(90)
    square(torty, size)
    torty.forward(size)
    torty.right(30)
    triangle(torty, size)


# def average():

def main():
    tallulah = turtle.Turtle()
    tallulah.pensize(10)
    tallulah.pencolor('orange')
    
    house(tallulah, 90, -250, 0)
    triangle()
    square(tallulah, 90)
    rectangle
    
if __name__ == "__main__":
    main()
    

'''
Write a function called average that takes three numbers as arguments and prints their
average.
The formula for the volume of a cylinder is π * r2 * h, where r is the radius of the circular base
and h is the height. Write a function called cylinder_V that takes the radius and height as
arguments and prints the volume of the cylinder. For π, write math.pi.
import math
Recall from lecture that the formula for the turn angle for a turtle to draw a polygon with n sides
is: angle = 360 / n. Write a function called octadecagon that takes a turtle and a side
length as arguments and draws a 18-sided polygon with sides of the given length. Use a for
loop.
Write a function called polygon that takes a turtle and a number of sides and a side length as
arguments and draws a polygon with the specified number of sides of the given length."
'''