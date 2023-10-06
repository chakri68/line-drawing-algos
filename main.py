import turtle as t
import time
import tkinter as tk
from tkinter import Canvas, Scrollbar, Frame, Label, Entry, Button, Tk, Listbox
from LineDrawing.LineDrawingStrategy import LineDrawingStrategy
from LineDrawing.DDA import DDALineDrawing as DDA
from LineDrawing.FixedPointArithmeticDDA import FixedPointArithmeticDDA as FDDA
from LineDrawing.Bresenhams import BresenhamLineDrawing as Bresenham
from utils import draw_pixel
from ui import ScrollableFrame

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300


def draw_line_on_canvas(canvas, algorithm, color, x1, y1, x2, y2):
    screen = t.TurtleScreen(canvas)
    screen.tracer(0)
    lizzy = t.RawTurtle(screen)
    lizzy.hideturtle()
    lizzy.penup()
    lizzy.color(color)
    points = algorithm.draw((x1, y1), (x2, y2))
    for point in points:
        draw_pixel(lizzy, point, color)
    screen.update()


def draw_from_ui():
    # Get user inputs from the Tkinter UI
    x1 = int(x1_entry.get())
    y1 = int(y1_entry.get())
    x2 = int(x2_entry.get())
    y2 = int(y2_entry.get())

    print(f"Drawing line from ({x1}, {y1}) to ({x2}, {y2})")

    for i, (algorithm, label, color) in enumerate(algorithms):
        canvas = canvases[i]
        print(canvas)
        start_time = time.perf_counter()
        draw_line_on_canvas(canvas, algorithm, color, x1, y1, x2, y2)
        elapsed_time = time.perf_counter() - start_time
        print(f"{label}: {elapsed_time:.6f} seconds")


def on_exit():
    root.destroy()


root = Tk()
root.title("Line Drawing App")

# Create line-drawing algorithms
algorithms = [
    (DDA, "DDA", "green"),
    (FDDA, "FixedPointDDA", "blue"),
    (Bresenham, "Bresenham", "yellow")
]

form_frame = Frame(root)
form_frame.pack(side="top")


# Create UI elements and organize them in a grid layout
x1_label = Label(form_frame, text="X1:")
x1_entry = Entry(form_frame)
y1_label = Label(form_frame, text="Y1:")
y1_entry = Entry(form_frame)
x2_label = Label(form_frame, text="X2:")
x2_entry = Entry(form_frame)
y2_label = Label(form_frame, text="Y2:")
y2_entry = Entry(form_frame)
draw_button = Button(form_frame, text="Draw Line", command=draw_from_ui)
exit_button = Button(form_frame, text="Exit", command=on_exit)

x1_label.grid(row=0, column=0, pady=5, padx=5)
x1_entry.grid(row=0, column=1, pady=5, padx=5)
y1_label.grid(row=0, column=2, pady=5, padx=5)
y1_entry.grid(row=0, column=3, pady=5, padx=5)
x2_label.grid(row=1, column=0, pady=5, padx=5)
x2_entry.grid(row=1, column=1, pady=5, padx=5)
y2_label.grid(row=1, column=2, pady=5, padx=5)
y2_entry.grid(row=1, column=3, pady=5, padx=5)
draw_button.grid(row=4, columnspan=4, sticky=tk.W + tk.E, pady=5, padx=5)
exit_button.grid(row=5, columnspan=4, sticky=tk.W + tk.E, pady=5, padx=5)

# Create separate canvases with scrollbars for each algorithm
canvases = []
canvas_frame = ScrollableFrame(root)
canvas_frame.pack(side="bottom", fill="both", expand=True)

canvas_per_row = 3

for i, (algorithm, label, color) in enumerate(algorithms):
    canvas = Canvas(canvas_frame.scrollable_frame, width=CANVAS_WIDTH,
                    height=CANVAS_HEIGHT, bg="white")
    canvas.grid(row=i // canvas_per_row, column=i % canvas_per_row)
    print(canvas)
    canvases.append(canvas)

root.mainloop()
