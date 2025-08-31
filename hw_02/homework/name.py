'''
Author: Ricky Berliant
Date: 9/1/2025
Class: ISTA 130
Section Leader: ???

Description:
The program draws the name "Ricky". 
'''

import turtle 

# draw the letter R
def letter_R(tallulah):
    tallulah.pendown()
    tallulah.setheading(90)
    tallulah.forward(180)
    tallulah.right(90)
    tallulah.forward(100)
    tallulah.right(90)
    tallulah.forward(60) 
    tallulah.right(90) 
    tallulah.forward(90)
    tallulah.left(130)
    tallulah.forward(150)
    tallulah.penup()
            
    # proceed over to the letter I
    tallulah.left(50)
    tallulah.forward(50)


# draw the letter I
def letter_I(tallulah):
    tallulah.pendown()    
    tallulah.left(90)
    tallulah.forward(100)
    tallulah.right(90)
    tallulah.forward(30)
    tallulah.right(90)
    tallulah.forward(100)
    tallulah.right(90)
    tallulah.forward(30)
    tallulah.right(90)
    tallulah.penup()
    tallulah.forward(120)
    
    # draw a small square above the letter I
    tallulah.pendown()    
    tallulah.forward(30)
    tallulah.right(90)
    tallulah.forward(30)
    tallulah.right(90)
    tallulah.forward(30)
    tallulah.right(90)
    tallulah.forward(30)
    tallulah.left(90)
    tallulah.penup() 

    # return to the letter I
    tallulah.forward(120)

    # proceed over to the letter C
    tallulah.left(90)
    tallulah.forward(120)


# draw the letter C
def letter_C(tallulah):
    tallulah.pendown()
    tallulah.left(180)
    tallulah.forward(60)
    tallulah.right(90)
    tallulah.forward(100)
    tallulah.right(90)
    tallulah.forward(60)
    tallulah.right(90)
    tallulah.forward(30)
    tallulah.right(90)
    tallulah.forward(30)
    tallulah.left(90)
    tallulah.forward(40)
    tallulah.left(90)
    tallulah.forward(30)
    tallulah.right(90)
    tallulah.forward(30)

    # proceed over to the letter K
    tallulah.penup() 
    tallulah.left(90)

# draw the letter K
def letter_K(tallulah):
    tallulah.pendown()
    tallulah.left(90)
    tallulah.forward(100)
    tallulah.backward(60)
    tallulah.right(45)
    tallulah.forward(75)
    tallulah.backward(75)
    tallulah.right(90)
    tallulah.forward(60)
    tallulah.left(45)

    # proceed over to the letter Y
    tallulah.penup() 
    tallulah.forward(70)
    


# draw the letter Y
def letter_Y(tallulah):
    tallulah.pendown()
    tallulah.left(90)
    tallulah.forward(60)
    tallulah.right(90)
    tallulah.forward(30)
    tallulah.left(90)
    tallulah.forward(90)
    tallulah.left(90)
    tallulah.forward(30)
    tallulah.left(90)
    tallulah.forward(45)
    tallulah.right(90)
    tallulah.forward(30)
    tallulah.right(90)
    tallulah.forward(45)
    tallulah.left(90)
    tallulah.forward(30)
    tallulah.left(90)
    tallulah.forward(90)
    tallulah.left(90)
    tallulah.forward(30)
    tallulah.right(90)
    tallulah.forward(60)
    tallulah.right(90)


    #exiting the Y
    tallulah.penup()
    tallulah.setheading(0) 


# main function
def main():
    '''
    Construct a turtle and use it write 'Ricky'.
    '''    
        
    # create the turtle
    tallulah = turtle.Turtle()
    tallulah.shape('turtle')
    tallulah.color('orange') 
    tallulah.speed(0)

    # colors
    turtle.bgcolor('black')
    tallulah.pencolor('orange')
    tallulah.pensize(10)
    
    # set position
    tallulah.penup()
    tallulah.goto(-250, 0)
    tallulah.pendown()
    
    # Write Ricky and have the turtle face east and move forward after writing out the letter
    letter_R(tallulah)
    letter_I(tallulah)
    letter_C(tallulah)
    tallulah.forward(30)

    letter_K(tallulah)
    tallulah.forward(30)
    
    letter_Y(tallulah)
    tallulah.forward(60)

    # Once I write out Ricky
    turtle.done()
    turtle.getscreen().exitonclick() 


if __name__ == '__main__':
    main()