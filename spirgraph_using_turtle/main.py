import random
from turtle import Turtle,Screen
import turtle
jay_pet = Turtle()
color = turtle
color.colormode(255)


def spirograph():
    head = 0
    while head < 355:
        color_change = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        jay_pet.pencolor(color_change)
        jay_pet.circle(50)
        head = jay_pet.heading()
        head = head+15
        jay_pet.setheading(head)


jay_pet.speed('fast')
spirograph()
screen = Screen()
screen.exitonclick()