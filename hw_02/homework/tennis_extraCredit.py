'''
Author: Ricky Berliant
Date: 9/1/2025
Class: ISTA 130
Section Leader: ???

Description:
The program draws a tennis ball. 
'''

import turtle 

def tennis_ball(tennis, x, y):
    tennis.penup()
    tennis.goto(x, y)
    tennis.pendown()
    tennis.pencolor("black")
    tennis.fillcolor("yellow")
    tennis.begin_fill()
    tennis.circle(100)
    tennis.end_fill()
    
    # grey line left side
    tennis.penup()
    tennis.goto(110, 180)
    tennis.pendown()
    tennis.pencolor("grey")
    tennis.forward(10)
    tennis.right(45)
    tennis.forward(115)
    tennis.right(45)
    tennis.forward(10)
    
    # grey line right side
    tennis.penup()
    tennis.goto(290, 190)
    tennis.pendown()
    tennis.right(45)
    tennis.pencolor("grey")
    tennis.forward(10)
    tennis.right(90)
    tennis.forward(115)
    tennis.right(60)
    tennis.forward(10)

    

def tennis_racket(tennis, x, y):
    
    #tennis grip
    tennis.penup()
    tennis.goto(x, y)
    tennis.pendown()
    tennis.pencolor("black")
    tennis.fillcolor('black')
    tennis.begin_fill()
    tennis.setheading(90)
    tennis.forward(120)
    tennis.right(90)
    tennis.forward(100)
    tennis.right(90)
    tennis.forward(120)
    tennis.right(90)
    tennis.forward(100)
    tennis.right(90)
    tennis.forward(130)
    tennis.end_fill()
    tennis.penup()
    
    #tennis racket net
    tennis.pencolor("aliceblue")
    tennis.pendown()
    tennis.setheading(90)
    
    # left side
    tennis.forward(100)     
    tennis.left(45)
    tennis.forward(70)      
    tennis.right(45)
    tennis.forward(200)    
    tennis.right(45)
    tennis.forward(70)      
    tennis.right(45)
    tennis.forward(100)    

    # right side
    tennis.right(45)
    tennis.forward(70)    
    tennis.right(45)
    tennis.forward(200)     
    tennis.right(45)
    tennis.forward(70)      
    tennis.left(45)
    tennis.forward(100)  
    tennis.penup()



def net_head(tennis):    
    # net head
    
    # horizontal line 1
    tennis.goto(-200, 260)
    tennis.pendown()
    tennis.left(90)
    tennis.forward(130)
    tennis.right(90)

    # horizontal line 2
    tennis.penup()
    tennis.goto(-230, 230)
    tennis.pendown()
    tennis.left(90)
    tennis.forward(170)
    tennis.right(90)
    
    # horizontal line 3
    tennis.penup()
    tennis.goto(-230, 200)
    tennis.pendown()
    tennis.left(90)
    tennis.forward(190)
    tennis.right(90)
    
    # horizontal line 4
    tennis.penup()
    tennis.goto(-230, 170)
    tennis.pendown()
    tennis.left(90)
    tennis.forward(190)
    tennis.right(90)
    
    # horizontal line 5
    tennis.penup()
    tennis.goto(-230, 140)
    tennis.pendown()
    tennis.left(90)
    tennis.forward(190)
    tennis.right(90)
    
    # horizontal line 6
    tennis.penup()
    tennis.goto(-230, 110)
    tennis.pendown()
    tennis.left(90)
    tennis.forward(190)
    tennis.right(90)
    
    # horizontal line 7
    tennis.penup()
    tennis.goto(-230, 80)
    tennis.pendown()
    tennis.left(90)
    tennis.forward(190)
    tennis.right(90)
    
    # horizontal line 7
    tennis.penup()
    tennis.goto(-230, 50)
    tennis.pendown()
    tennis.left(90)
    tennis.forward(190)
    tennis.right(90)
    
    # horizontal line 8
    tennis.penup()
    tennis.goto(-230, 20)
    tennis.pendown()
    tennis.left(90)
    tennis.forward(190)
    tennis.right(90)
    
    # vertical line 1
    tennis.penup()
    tennis.goto(-210, 10)
    tennis.pendown()
    tennis.setheading(90)
    tennis.forward(240)

    # vertical line 2
    tennis.penup()
    tennis.goto(-180, 10)
    tennis.pendown()
    tennis.setheading(90)
    tennis.forward(265)

    # vertical line 3
    tennis.penup()
    tennis.goto(-150, 10)
    tennis.pendown()
    tennis.setheading(90)
    tennis.forward(265)
    
    # vertical line 4
    tennis.penup()
    tennis.goto(-120, 10)
    tennis.pendown()
    tennis.setheading(90)
    tennis.forward(265)

    # vertical line 5
    tennis.penup()
    tennis.goto(-90, 10)
    tennis.pendown()
    tennis.setheading(90)
    tennis.forward(265)
    
    # vertical line 6
    tennis.penup()
    tennis.goto(-60, 10)
    tennis.pendown()
    tennis.setheading(90)
    tennis.forward(240)


def main():
    '''
    Construct a turtle and draw a tennis ball and racket.
    '''    
    # create the turtle
    tennis = turtle.Turtle()
    tennis.shape('turtle')
    tennis.color('black') 
    tennis.speed(0)
    tennis.pensize(10)

    # tennis court background color
    turtle.bgcolor('#6C935C')
    
    # set position
    tennis_ball(tennis, 200, 80)  
    tennis_racket(tennis, -185, -250)
    net_head(tennis)    
    
    tennis.hideturtle()
    turtle.done()
    turtle.getscreen().exitonclick() 
    
if __name__ == '__main__':
    main()