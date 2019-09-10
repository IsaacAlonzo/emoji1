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


john.left(270)
john.forward(200)
john.left(270)
john.forward(50)
john.pendown()
john.begin_fill()
john.circle(25)
john.end_fill()

















scn.exitonclick()