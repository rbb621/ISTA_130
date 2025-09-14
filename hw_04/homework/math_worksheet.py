import turtle
import math

def rectangle(torty, width, height):
    torty.forward(height)
    torty.right(90)
    torty.forward(width)
    torty.right(90)
    torty.forward(height)
    torty.right(90)
    torty.forward(width)
    torty.right(90)
def house(torty, size, x, y):
    torty.penup()
    torty.goto(x, y)
    torty.pendown()
    torty.setheading(90)
    square(torty, size)
    torty.forward(size)
    torty.right(30)
    triangle(torty, size)

def average(torty):
    
def cylinder_V():
    
def octadecagon():
    
def polygon():
    


def main():
    tallulah = turtle.Turtle()
    tallulah.pencolor('orange')
    tallulah.pensize(10)
    
    rectangle(tallulah, )