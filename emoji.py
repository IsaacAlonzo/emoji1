import turtle

john = turtle.Turtle()
scn = turtle.Screen()
bob = turtle.Turtle()
phil = turtle.Turtle()
sven = turtle.Turtle()


bob.shape("turtle")
phil.shape("arrow")
john.shape("arrow")
sven.shape("arrow")


john.penup()
phil.penup()
sven.penup()

bob.color("yellow")
bob.begin_fill()
bob.circle(150)
bob.end_fill()


phil.left(90)
phil.forward(200)
phil.left(90)
phil.forward(50)
phil.pendown()
phil.begin_fill()
phil.circle(25)
phil.end_fill()

john.goto(50, 150)
john.pendown()
john.begin_fill()
john.circle(25)
john.end_fill()

sven.left(90)
sven.forward(75)
sven.left(90)
sven.pendown()
sven.begin_fill()
sven.forward(75)
sven.right(90)
sven.forward(25)
sven.right(90)
sven.forward(150)
sven.right(90)
sven.forward(25)
sven.right(90)
sven.forward(75)
sven.end_fill()

phil.penup()
phil.goto(-25, 200)
phil.right(45)
phil.pendown()
phil.begin_fill()
phil.forward(50)
phil.right(90)
phil.forward(25)
phil.right(90)
phil.forward(50)
phil.right(90)
phil.forward(25)
phil.end_fill()

def eyebrow():
    john.forward(50)
    john.left(90)
    john.forward(25)
    john.left(90)
    john.forward(50)
    john.left(90)
    john.forward(25)


john.penup()
john.goto(25, 200)
john.left(45)
john.pendown()
john.begin_fill()
eyebrow()
john.end_fill()


















scn.exitonclick()