from turtle import Turtle
from random import randint

matt = Turtle()
meghan = Turtle()
alex = Turtle()
theo = Turtle()

matt.color('blue')
matt.shape('turtle')

meghan.color('yellow')
meghan.shape('turtle')

alex.color('red')
alex.shape('turtle')

theo.color('green')
theo.shape('turtle')


matt.penup()
matt.goto(-260, 50)
matt.pendown()

meghan.penup()
meghan.goto(-260, 150)
meghan.pendown()

alex.penup()
alex.goto(-260, 0)
alex.pendown()

theo.penup()
theo.goto(-260, 100)
theo.pendown()

for movement in range(100):
    matt.forward(randint(1,5))
    meghan.forward(randint(1,5))
    alex.forward(randint(1,5))
    theo.forward(randint(1,5))
