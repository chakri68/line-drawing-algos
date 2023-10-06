from typing import Tuple
from turtle import Turtle


def draw_pixel(turtle: Turtle, pixel: Tuple[int, int], color="black"):
    turtle.penup()
    turtle.goto(pixel)
    turtle.color(color)
    turtle.pendown()
    turtle.dot(5)
    return turtle
