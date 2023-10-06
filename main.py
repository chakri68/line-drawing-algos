import turtle as t
import time
import tkinter as tk
from LineDrawing.LineDrawingStrategy import LineDrawingStrategy
from LineDrawing.DDA import DDALineDrawing as DDA
from LineDrawing.FixedPointArithmeticDDA import FixedPointArithmeticDDA as FDDA
from LineDrawing.Bresenhams import BresenhamLineDrawing as Bresenham
from utils import draw_pixel

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def draw_line(lizzy: t.Turtle, algorithm: LineDrawingStrategy, color, x1, y1, x2, y2):
    lizzy.color(color)
    points = algorithm.draw((x1, y1), (x2, y2))
    for point in points:
        draw_pixel(lizzy, point, color)


def draw_from_ui():
    # Get user inputs from the Tkinter UI
    x1 = int(x1_entry.get())
    y1 = int(y1_entry.get())
    x2 = int(x2_entry.get())
    y2 = int(y2_entry.get())

    print(f"Drawing line from ({x1}, {y1}) to ({x2}, {y2})")

    for algorithm, label, color in algorithms:
        start_time = time.perf_counter()
        draw_line(lizzy, algorithm, color, x1, y1, x2, y2)
        elapsed_time = time.perf_counter() - start_time
        t.update()
        print(f"{label}: {elapsed_time:.6f} seconds")


def on_exit():
    root.destroy()


root = tk.Tk()
root.title("Line Drawing App")

# Disable tracer
t.tracer(0, 0)

# Create a turtle screen
screen = t.Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
lizzy = t.Turtle()
lizzy.hideturtle()
lizzy.penup()

# Create line-drawing algorithms
algorithms = [
    (DDA, "DDA", "green"),
    (FDDA, "FixedPointDDA", "blue"),
    (Bresenham, "Bresenham", "yellow")
]

# Create UI elements
x1_label = tk.Label(root, text="X1:")
y1_label = tk.Label(root, text="Y1:")
x2_label = tk.Label(root, text="X2:")
y2_label = tk.Label(root, text="Y2:")
x1_entry = tk.Entry(root)
y1_entry = tk.Entry(root)
x2_entry = tk.Entry(root)
y2_entry = tk.Entry(root)
draw_button = tk.Button(root, text="Draw Line", command=draw_from_ui)
exit_button = tk.Button(root, text="Exit", command=on_exit)

# Pack UI elements
x1_label.pack()
x1_entry.pack()
y1_label.pack()
y1_entry.pack()
x2_label.pack()
x2_entry.pack()
y2_label.pack()
y2_entry.pack()
draw_button.pack()
exit_button.pack()

root.mainloop()
