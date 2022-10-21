"""
CSCI-141 Computer Science 1 Recitation Exercise
03-Recursion
Shapes

Here is where you write a general recursive solution to the drawing
problem by implementing draw_shapes.
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
    _list = {
        0: "black",
        1: "green",
        2: "blue",
        3: "red",
        4: "purple"
    }

    _color = ""
    try:
        _color = _list[depth]
    except:
        _color = _list[0]
    finally:
        turtle.color(_color)

def draw_shapes(length, depth):
    """
    Draw the shape at the current depth of detail.
    :param length: length of the segments
    :param depth: the current level of detail we are at
    :pre turtle is at the center, down and facing east
    :post turtle is at the center, down and facing east
    """
    set_color(depth)
    if depth == 1:
        turtle.circle(length/2)
    else:
        turtle.forward(length)
        draw_shapes(length/2, depth - 1)
        set_color(depth)

        turtle.left(120)
        turtle.forward(length)
        draw_shapes(length/2, depth - 1)
        set_color(depth)

        turtle.left(120)
        turtle.forward(length)
        draw_shapes(length/2, depth - 1)
        set_color(depth)

        turtle.left(120)

def main():
    """
    The main program prompts for the depth and then calls the recursive
    drawing function, draw_shapes, to draw the complete image.
    """
    depth = int(input('Enter depth: '))
    init(depth)
    draw_shapes(200, depth)
    turtle.done()

if __name__ == '__main__':
    main()
