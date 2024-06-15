import turtle

screen = turtle.getscreen()

t = turtle.Turtle()

t.color("blue")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.color("red")
t.goto(100, 100)
t.pendown()
t.circle(90)

t.seth(90)
t.circle(150, 90)

turtle.done()