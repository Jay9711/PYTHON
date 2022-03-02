from turtle import Turtle, Screen
# def turtle_square():
#      for i in range(0, 3):
#          jay_pet.forward(100)
#          jay_pet.right(90)
#      jay_pet.home()
#      return

#
# def turtle_dashed():
#     for i in range(0, 26):
#         jay_pet.forward(10)
#         jay_pet.pendown()
#         jay_pet.forward(10)
#         jay_pet.penup()


def all_shapes():
    for sides in range(3, 11):
        angle = 360/sides
        for i in range(sides):
            jay_pet.right(angle)
            jay_pet.forward(100)


jay_pet = Turtle()
jay_pet.shape("turtle")
jay_pet.color("light sky blue")
#turtle_square()
#turtle_dashed()
all_shapes()


















screen = Screen()
screen.exitonclick()
