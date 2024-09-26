import turtle

turtle.Screen().bgcolor("white")

sc=turtle.Screen()
sc.setup(500,500)

turtle.title("Welcome to Turtle window")

board=turtle.Turtle()

for i in range(6):
    board.forward(90)
    board.left(300)

turtle.done()