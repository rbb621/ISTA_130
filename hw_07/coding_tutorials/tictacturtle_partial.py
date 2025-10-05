'''
Author: Rich
Date: Today
Class: ISTA 130
Section Leader: me

Description:
This module plays tic-tac-turtle.  This version does not check for 
tie games, full boards, or incorrect user input.  It illustrates the 
use of if-elif-else statements and while loops.

It uses the following functions to draw the board:
    draw_grid(azt)
    draw_A(azt, x, y)
    draw_B(azt, x, y)
    draw_C(azt, x, y)
    draw_1(azt, x, y)
    draw_2(azt, x, y)
    draw_3(azt, x, y)
    draw_board(azt)
    
It uses the following functions to draw during play:
    draw_x(azt, x, y)
    draw_0(azt, x, y)
    
It uses the following functions during play:
    x_wins(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    o_wins(a1, a2, a3, b1, b2, b3, c1, c2, c3)
'''

import turtle
import math

def draw_grid(azt):
    '''
    This function uses turtle azt to draw a pound sign centered
    at (0, 0) with line segments of length 300.
    
    Returns None.
    '''
    
    azt.penup()
    azt.goto(-150, -50)
    azt.pendown()
    azt.setheading(0)
    azt.forward(300)    
    
    azt.penup()
    azt.goto(-150, 50)
    azt.pendown()
    azt.setheading(0)
    azt.forward(300)    
    
    azt.penup()
    azt.goto(-50, 150)
    azt.pendown()
    azt.setheading(270)
    azt.forward(300)    
    
    azt.penup()
    azt.goto(50, 150)
    azt.pendown()
    azt.setheading(270)
    azt.forward(300)
    
def draw_A(azt, x, y):
    '''
    This function uses turtle azt to draw an 'A'.
    The letter has lower left corner at (x, y) and has height 50.
    
    Returns None.
    '''
    
    azt.penup()
    azt.goto(x, y)
    azt.pendown()
    azt.setheading(60)
    length = 25 * math.sqrt(3)
    azt.forward(length)
    azt.right(120)
    azt.forward(length)
    azt.backward(length / 2)
    azt.right(120)
    azt.forward(length / 2)
    
def draw_B(azt, x, y):
    '''
    This function uses turtle azt to draw a 'B'.
    The letter has lower left corner at (x, y) and has height 50.
    
    Returns None.
    '''
    
    azt.penup()
    azt.goto(x, y)
    azt.pendown()
    azt.setheading(90)
    azt.forward(50)
    draw_3(azt, x, y)
    
def draw_C(azt, x, y):
    '''
    This function uses turtle azt to draw a 'C'.
    The letter has lower left corner at (x, y) and has height 50.
    
    Returns None.
    '''
    
    azt.penup()
    azt.goto(x + 35, y)
    azt.pendown()
    azt.setheading(0)
    azt.backward(10)
    azt.circle(25, -180)
    azt.backward(10)
    
def draw_2(azt, x, y):
    '''
    This function uses turtle azt to draw a '2'.
    The numeral has lower left corner at (x, y) and has height 50.
    
    Returns None.
    '''
    
    azt.penup()
    azt.goto(x, y)
    azt.pendown()
    azt.setheading(0)
    azt.forward(35)
    azt.backward(35)
    azt.left(45)
    azt.forward(45)
    azt.circle(10, 135)
    azt.forward(25)
    
def draw_3(azt, x, y):
    '''
    This function uses turtle azt to draw a '3'.
    The numeral has lower left corner at (x, y) and has height 50.
    
    Returns None.
    '''
    azt.penup()
    azt.goto(x, y)
    azt.pendown()
    azt.setheading(0)
    azt.forward(20)
    azt.circle(12, 180)
    azt.forward(20)
    azt.backward(20)
    azt.setheading(0)
    azt.circle(12, 180)
    azt.forward(20)
    
def draw_1(azt, x, y):
    '''
    This function uses turtle azt to draw a '1'.
    The numeral has lower left corner at (x, y) and has height 50.
    
    Returns None.
    '''
    azt.penup()
    azt.goto(x, y)
    azt.pendown()
    azt.setheading(0)
    azt.forward(20)
    azt.backward(10)
    azt.left(90)
    azt.forward(50)
    azt.right(30)
    azt.backward(15)
    
def draw_board(azt):
    '''
    This function uses turtle azt to draw the board for
    a game of tic-tac-turtle.
    
    Returns None.
    '''
    draw_grid(azt)
    draw_A(azt, -200, 75)
    draw_B(azt, -200, -25)
    draw_C(azt, -200, -125)
    draw_1(azt, -110, 165)
    draw_2(azt, -17.5, 165)
    draw_3(azt, 80, 165)
    
def draw_x(azt, x, y):
    '''
    This function uses turtle azt to draw an 'x'.
    The letter has center at (x, y) and has height and width 50.
    
    Returns None.
    '''
    azt.penup()
    azt.goto(x - 25, y - 25)
    azt.pendown()
    azt.setheading(45)
    length = 50 * math.sqrt(2)
    azt.forward(length)
    azt.backward(length / 2)
    azt.left(90)
    azt.forward(length / 2)
    azt.backward(length)
    
def draw_o(azt, x, y):
    '''
    This function uses turtle azt to draw an 'o'.
    The letter has center at (x, y) and has diameter 50.
    
    Returns None.
    '''
    azt.penup()
    azt.goto(x, y - 25)
    azt.pendown()
    azt.setheading(0)
    azt.circle(25)

def x_wins(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    ''' 
    This function checks to see if player1 has won the game of
    tic-tac-turtle.
    
    Parameters a1, a2, a3, b1, b2, b3, c1, c2, c3 represent squares
    on the tic-tac-turtle board.  a1 is upper left, a2 is upper center...
    c3 is lower right.
    
    Returns True if 3 squares in row, column, or diagonally contain x.
    False otherwise.
    '''
    
def o_wins(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    ''' 
    This function checks to see if player2 has won the game of
    tic-tac-turtle.
    
    Parameters a1, a2, a3, b1, b2, b3, c1, c2, c3 represent squares
    on the tic-tac-turtle board.  a1 is upper left, a2 is upper center...
    c3 is lower right.
    
    Returns True if 3 squares in row, column, or diagonally contain o.
    False otherwise.
    '''

    
def main():
    '''
    Play games of tic-tac-turtle until the users elect to quit.
    '''
    azt = turtle.Turtle()
    azt.speed(0)
    azt.pensize(5)
    azt.hideturtle()
    
    turtle.done()
            
if __name__ == "__main__":
    main()
    