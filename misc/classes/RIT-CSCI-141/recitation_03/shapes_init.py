"""
CSCI-141 Computer Science 1 Recitation Exercise
03-Recursion
Shapes

With the initial non-recursive program, we have separate drawing
functions for depths 1-4 that reuse each other to handle the lower
depths.

This program is complete and should not be changed.  You are just using it
for reference when you implement shapes.py.
"""

import turtle

def init(depth):
    """
    Write the depth and set up the turtle so it is at the initial state.
    :param depth: the detail of the shape to draw
    :pre turtle is at the center, down and facing east
    :post turtle is at the center, down and facing east
    """
    turtle.pensize(4)
    turtle.speed(0)
    turtle.up()
    turtle.backward(200)
    turtle.write('Depth: ' + str(depth), font = ("Arial", 24, "bold"))
    turtle.forward(200)
    turtle.down()

def set_color(depth):
    """
    Change the color of what the turtle draws based on the depth.
    :param depth: the detail of the shape to draw
    """
    if depth == 1:
        turtle.color('green')
    elif depth == 2:
        turtle.color('blue')
    elif depth == 3:
        turtle.color('red')
    elif depth == 4:
        turtle.color('purple')
    else:
        turtle.color('black')

def draw_shapes_1(length):
    """
    Draw the shape at depth 1
    :param length: length of the segments
    :pre turtle is at the center, down and facing east
    :post turtle is at the center, down and facing east
    """
    set_color(1)
    turtle.circle(length/2)

def draw_shapes_2(length):
    """
    Draw the shape at depth 2
    :param length: length of the segments
    :pre turtle is at the center, down and facing east
    :post turtle is at the center, down and facing east
    """
    set_color(2)
    turtle.forward(length)
    draw_shapes_1(length/2)
    turtle.left(120)
    set_color(2)
    turtle.forward(length)
    draw_shapes_1(length/2)
    turtle.left(120)
    set_color(2)
    turtle.forward(length)
    draw_shapes_1(length/2)
    turtle.left(120)

def draw_shapes_3(length):
    """
    Draw the shape at depth 3
    :param length: length of the segments
    :pre turtle is at the center, down and facing east
    :post turtle is at the center, down and facing east
    """
    set_color(3)
    turtle.forward(length)
    draw_shapes_2(length/2)
    turtle.left(120)
    set_color(3)
    turtle.forward(length)
    draw_shapes_2(length/2)
    turtle.left(120)
    set_color(3)
    turtle.forward(length)
    draw_shapes_2(length/2)
    turtle.left(120)

def draw_shapes_4(length):
    """
    Draw the shape at depth 4
    :param length: length of the segments
    :pre turtle is at the center, down and facing east
    :post turtle is at the center, down and facing east
    """
    set_color(4)
    turtle.forward(length)
    draw_shapes_3(length/2)
    turtle.left(120)
    set_color(4)
    turtle.forward(length)
    draw_shapes_3(length/2)
    turtle.left(120)
    set_color(4)
    turtle.forward(length)
    draw_shapes_3(length/2)
    turtle.left(120)

def main():
    """
    The main program prompts for the depth and then calls the appropriate top
    level function to draw the image.
    """
    depth = int(input('Enter depth: '))
    init(depth)

    # can only handle depths 1-4
    if depth == 1:
        draw_shapes_1(200)
    elif depth == 2:
        draw_shapes_2(200)
    elif depth == 3:
        draw_shapes_3(200)
    elif depth == 4:
        draw_shapes_4(200)
    else:
        print('Invalid depth!')

    turtle.done()

if __name__ == '__main__':
    main()
