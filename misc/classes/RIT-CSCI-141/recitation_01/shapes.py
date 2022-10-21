"""
CSCI-141 Computer Science 1 Recitation Exercise
01-Introduction
Shapes

Here is code that draw a collection of embedded shapes - a green square,
a red circle inside the square, and a blue triangle in a corner of the square.

This code runs and displays a single set of shapes fine.  Your goal is
to convert this code so that it is more functional, and supports function reuse.

This code is already set up with the pre/post-conditions when you convert things
into functions.  By default, the turtle is at the center, facing east, and is up,
before and after each drawing function is called.
"""

import turtle


def init():
    """Initialize turtle"""
    turtle.up()
    turtle.title("Shapes")
    turtle.pensize(4)

def draw_square():
    # draw square
    turtle.color('green')
    turtle.down()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.up()

def draw_circle():
    # draw circle
    turtle.color('red')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.down()
    turtle.circle(25)
    turtle.up()
    turtle.left(90)
    turtle.back(25)
    turtle.right(90)
    turtle.back(50)

def draw_triangle():
    # draw triangle
    turtle.color('blue')
    turtle.down()
    turtle.forward(25)
    turtle.left(120)
    turtle.forward(25)
    turtle.left(120)
    turtle.forward(25)
    turtle.left(120)
    turtle.up()

def draw_shapes():
    draw_square()
    draw_circle()
    draw_triangle()

def main():
    """Draw one set of embedded shapes"""
    init()
    draw_shapes()
    turtle.left(180)
    draw_shapes()
    turtle.left(180)

    turtle.color('black')
    turtle.done()


if __name__ == "__main__":
    main()