from turtle import Turtle, Screen
import random, turtle

jay_pet = Turtle()
turtle.colormode(255)

def random_walk():

    direction_array = [0, 90, 180, 360]
    for i in range(0, 100):
        # random_num = str(hex(random.randint(0, 16777215)))
        # jay_pet.pencolor(str('#' + random_num[2:]))
        # jay_pet.pencolor(screen.colormode(float(random.randint(1, 255))),
        # screen.colormode(float(random.randint(1, 255))), screen.colormode(float(random.randint(1, 255))))
        color_tuple = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        jay_pet.pencolor(color_tuple)
        jay_pet.setheading(random.choice(direction_array))
        jay_pet.forward(15)
    return


jay_pet.shape("turtle")
jay_pet.speed("fast")
jay_pet.pensize(10)
random_walk()
screen = Screen()
screen.exitonclick()
