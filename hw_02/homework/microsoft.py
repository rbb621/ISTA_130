import turtle

#setup
microsoft = turtle.Turtle()
microsoft.pensize(10)
microsoft.shape('turtle')

#draw red square
microsoft.penup()
microsoft.pencolor('#E1341E')
microsoft.goto(-250, 0)
microsoft.pendown()
microsoft.fillcolor('#E1341E')


microsoft.begin_fill()
microsoft.left(90)
microsoft.forward(120)
microsoft.right(90)
microsoft.forward(120)
microsoft.right(90)
microsoft.forward(120)
microsoft.right(90)
microsoft.forward(120)
microsoft.end_fill()


# draw green square
microsoft.penup()
microsoft.pencolor('#7FBA00')
microsoft.backward(150)
microsoft.pendown()
microsoft.fillcolor('#7FBA00')


microsoft.begin_fill()
microsoft.right(90)
microsoft.forward(120)
microsoft.right(90)
microsoft.forward(120)
microsoft.right(90)
microsoft.forward(120)
microsoft.right(90)
microsoft.forward(120)
microsoft.end_fill()


#draw yellow square

microsoft.penup()
microsoft.pencolor('#FFB900')
microsoft.left(90)
microsoft.forward(30)
microsoft.pendown()
microsoft.fillcolor('#FFB900')
microsoft.begin_fill()
microsoft.left(90)
microsoft.forward(120)
microsoft.right(90)
microsoft.forward(120)
microsoft.right(90)
microsoft.forward(120)
microsoft.right(90)
microsoft.forward(120)
microsoft.end_fill()


#draw blue square

microsoft.penup()
microsoft.pencolor("#00A2ED")
microsoft.left(90)
microsoft.forward(30)
microsoft.pendown()
microsoft.fillcolor('#00A2ED')


microsoft.begin_fill()
microsoft.forward(120)
microsoft.left(90)
microsoft.forward(120)
microsoft.left(90)
microsoft.forward(120)
microsoft.left(90)
microsoft.forward(120)
microsoft.end_fill()
microsoft.pencolor("#000000")


#Creat a Twin Turtle
twin = turtle.Turtle()
twin.color("black")
twin.penup()
twin.goto(-250, 0) 
twin.pensize(5)   
twin.setheading(0)  
twin.pendown()


# Twin draws a border/underline
for i in range(4):
    twin.forward(120)
    twin.left(90)
    twin.penup()

    

# Final shape changes
microsoft.shape("square")
twin.shape("circle")

microsoft.getscreen().exitonclick()