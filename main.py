import turtle as t
import time
from utils import drawPixel
from LineDrawing.DDA import DDALineDrawing as DDA
from LineDrawing.FixedPointArithmeticDDA import FixedPointArithmeticDDA as FDDA
from LineDrawing.Bresenhams import BresenhamLineDrawing as Bresenham

# Create a turtle named Lizzy
# Lizzy will draw the lines
lizzy = t.Turtle()

# Disable the tracer and hide the turtle
lizzy.hideturtle()
t.tracer(0, 0)

xOffset = 50

# Using DDA
startT = time.perf_counter()
x = 0
color = "green"
startPoint = (x, 0)
endPoint = (x + 500, 500)
lizzy.color(color)
points = DDA.draw(startPoint, endPoint)
for point in points:
    drawPixel(lizzy, point)
t.update()
print("DDA: " + str(time.perf_counter() - startT))

# Using FixedPointDDA
startT = time.perf_counter()
x += xOffset
color = "blue"
startPoint = (x, 0)
endPoint = (x + 500, 500)
lizzy.color(color)
points = FDDA.draw(startPoint, endPoint)
for point in points:
    drawPixel(lizzy, point)
t.update()
print("FixedPointDDA: " + str(time.perf_counter() - startT))

# Using Bresenham's
startT = time.perf_counter()
x += xOffset
color = "yellow"
startPoint = (x, 0)
endPoint = (x + 500, 500)
lizzy.color(color)
points = Bresenham.draw(startPoint, endPoint)
for point in points:
    drawPixel(lizzy, point)
t.update()
print("Bresenham: " + str(time.perf_counter() - startT))

t.exitonclick()
