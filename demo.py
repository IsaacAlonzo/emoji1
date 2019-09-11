import turtle

john = turtle.Turtle()
scn = turtle.Screen()
bob = turtle.Turtle()
phil = turtle.Turtle()
sven = turtle.Turtle()


bob.shape("turtle")
phil.shape("classic")
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


















scn.exitonclick()