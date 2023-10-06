from typing import Tuple
from turtle import Turtle


def drawPixel(turtle: Turtle, pixel: Tuple[int, int]):
    turtle.penup()
    turtle.goto(pixel)
    turtle.pendown()
    turtle.dot(5)
    return turtle
