import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
color_list = [(224, 162, 69), (19, 44, 82), (133, 62, 85), (171, 65, 45), (125, 39, 60), (23, 85, 61), (22, 114, 140),
              (58, 46, 35), (244, 197, 53), (194, 138, 160), (60, 136, 75), (225, 83, 45), (230, 174, 191),
              (28, 61, 53), (58, 71, 38), (155, 188, 179), (194, 101, 133), (165, 204, 199), (55, 29, 44),
              (153, 170, 183), (32, 40, 102), (65, 155, 82), (186, 187, 49), (9, 80, 109), (240, 201, 6), (101, 49, 42)]
tim = Turtle()
tim.speed(0)


def change_row(no_of_dots):
    tim.penup()
    for distance in range(no_of_dots):
        tim.backward(50)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.pendown()


def draw_dots(no_of_dots):
    for dots in range(no_of_dots):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    change_row(no_of_dots)


for i in range(10):
    draw_dots(10)

screen = Screen()
screen.exitonclick()
