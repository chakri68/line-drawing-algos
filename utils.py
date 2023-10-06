from typing import Tuple
from turtle import Turtle, RawTurtle


def draw_pixel(turtle: Turtle | RawTurtle, pixel: Tuple[int, int], color="black"):
    turtle.penup()
    turtle.goto(pixel)
    turtle.color(color)
    turtle.pendown()
    turtle.dot(5)
    return turtle
