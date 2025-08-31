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
    tallulah = turtle.Turtle()
    
    # Change turtle properties
    tallulah.shape('turtle')
    tallulah.pensize(10)
    tallulah.pencolor('blue')
    
    # Write H
    tallulah.right(90)
    tallulah.forward(100)
    tallulah.back(50)
    tallulah.left(90)
    tallulah.forward(50)
    tallulah.left(90)
    tallulah.forward(50)
    tallulah.back(100)

    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
