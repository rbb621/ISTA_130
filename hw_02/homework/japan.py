'''
Author: Ricky Berliant
Date: 2/20/2026
Class: APCV 320 - Computational Thinking and Doing
Professor: Atef Abu Ageel

Draw a Japan flag
'''

import turtle

# Drawing Cherry Blossom Petals
def cherry_blossom_petal(cherry_blossom, x, y):
    cherry_blossom.penup()
    cherry_blossom.goto(x, y)
    cherry_blossom.pendown()
    cherry_blossom.pencolor('black')
    cherry_blossom.fillcolor('pink')
    cherry_blossom.begin_fill()
    cherry_blossom.left(120)
    cherry_blossom.forward(40)
    cherry_blossom.left(60)
    cherry_blossom.forward(40)
    cherry_blossom.left(120)
    cherry_blossom.forward(40)
    cherry_blossom.left(60)
    cherry_blossom.forward(40)
    cherry_blossom.end_fill()
    cherry_blossom.setheading(0)  
    
def main():
    
    # Creating a Window Background
    window = turtle.Screen()
    window.bgcolor('white')  

    # Japan Symbol turtle!
    japan = turtle.Turtle()
    japan.speed(0)
    japan.pensize(5)
    
    # Cherry Blossom turtle!
    cherry_blossom = turtle.Turtle()
    cherry_blossom.speed(0)
    cherry_blossom.pensize(5)
    
    # Drawing The Red Circle 
    japan.penup()

    # Location of drawing the red circle
    japan.goto(0, -80)
    japan.pendown()
    
    # Begin drawing the circle
    japan.pencolor("black")
    japan.fillcolor("red")
    japan.begin_fill()
    japan.circle(100)
    japan.end_fill()

    
    # Cherry Blossom Petals!

    # top left corner
    cherry_blossom_petal(cherry_blossom, -220, 72)
    
    # center left side
    cherry_blossom_petal(cherry_blossom, -120, 300)
    
    # bottom-center
    cherry_blossom_petal(cherry_blossom, 72, -220)

    # top center
    cherry_blossom_petal(cherry_blossom, 50, 202)     
    
    # bottom left
    cherry_blossom_petal(cherry_blossom, -220, -150)
    cherry_blossom_petal(cherry_blossom, -130, -270)    

    # right side
    cherry_blossom_petal(cherry_blossom, 250, 60)
    cherry_blossom_petal(cherry_blossom, 250, -100)
    
    # top right corner
    cherry_blossom_petal(cherry_blossom, 220, 300)


    # Once red circle along with the cherry blossoms are all drawn
    japan.pencolor("black")
    japan.shape("circle")
    cherry_blossom.pencolor("black")
    cherry_blossom.shape("square")
    
    # Click the screen to close the window
    turtle.done()
    turtle.getscreen().exitonclick()


if __name__ == '__main__':
    main()