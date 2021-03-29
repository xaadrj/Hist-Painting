import colorgram
from turtle import Turtle, Screen, colormode
from random import choice
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

color_list = [(233, 239, 246), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148),
              (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71),
              (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49),
              (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159),
              (175, 200, 188), (34, 151, 210), (65, 66, 56)]


tim = Turtle()
colormode(255)
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")


def print_line():
    for _ in range(10):
        tim.dot(20, choice(color_list))
        tim.forward(50)


size = -212.13
for _ in range(10):
    size += 50
    print_line()
    tim.setpos(-212.13, size)

show_screen = Screen()
show_screen.exitonclick()
