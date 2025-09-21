'''
Name: Ricky Berliant
Date: 09/18/2025
Class: ISTA 130
Section Leader: Sungjoon Shin

Drawing a star using a for loop
'''

import turtle
import math

        
def drawing(a_turtle, side_len):
    for i in range(5):
        a_turtle.forward(side_len)
        a_turtle.right(144)
    return None

def loopy_roots():
    for i in range(1, 11):
        square_root = math.sqrt(i)
        print(i, ":", square_root)

def main():
    # create a turtle
    tallulah = turtle.Turtle()
    tallulah.pencolor('red')
    tallulah.pensize(10)

    drawing(tallulah, 90)
    loopy_roots()
    
    # Once the shape is finished
    tallulah.hideturtle()
    turtle.done()
    tallulah.getscreen().exitonclick()
    

if __name__ == "__main__":
    main()