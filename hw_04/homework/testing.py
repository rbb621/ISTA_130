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
    
def house(torty, size, x, y):
    torty.penup()
    torty.goto(x, y)
    torty.pendown()
    torty.setheading(90)
    # square(torty, size)
    torty.forward(size)
    torty.right(30)
    # triangle(torty, size)

def triangle(torty, size, x, y):
    torty.goto(x, y)
    torty.right(120)
    torty.forward(size)
    
        

def main():
    tallulah = turtle.Turtle()
    tallulah.pensize(10)
    tallulah.pencolor('orange')

    rectangle(tallulah, 45, 45)
    house(tallulah, 90, 0, 0)
    
    #once done
    turtle.getscreen().exitonclick()
    
if __name__ == "__main__":
    main()
    