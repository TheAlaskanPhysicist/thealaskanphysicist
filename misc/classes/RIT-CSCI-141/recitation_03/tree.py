"""
CSCI-141 Computer Science 1 Presentation Code
03-Recursion
Tree

This is the tree lecture code modified to add color.  It contains
the initial draw_tree0/1/2/3/4 approach and then the recursive
draw_tree approach which is what is used in the main.
"""

import turtle

def init(depth):
    """
    Write the depth and set up the turtle so it is at the initial state.
    :param depth: the detail of the shape to draw
    :pre turtle is at the center, down and facing east
    :post turtle is at the center, down and facing north
    """
    turtle.pensize(4)
    turtle.speed(0)
    turtle.up()
    turtle.backward(200)
    turtle.write('Depth: ' + str(depth), font = ("Arial", 24, "bold"))
    turtle.forward(200)
    turtle.down()
    turtle.left(90)

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

def draw_tree_0(length):
    """
    At depth 0 there is no tree!
    :param length: the segment length
    :pre turtle is at the center, down and facing north
    :post turtle is at the center, down and facing north
    """
    pass

def draw_tree_1(length):
    """
    A tree of depth 1 is just the trunk.
    :param length:  the segment length
    :pre turtle is at the center, down and facing north
    :post turtle is at the center, down and facing north
    """
    set_color(1)
    turtle.forward(length)
    draw_tree_0(length)
    turtle.backward(length)

def draw_tree_2(length):
    """
    A tree of depth 2 is a trunk and two branches.
    :param length:  the segment length
    :pre turtle is at the center, down and facing north
    :post turtle is at the center, down and facing north
    """
    set_color(2)
    turtle.forward(length)
    turtle.left(45)
    draw_tree_1(length/2)
    turtle.right(90)
    draw_tree_1(length/2)
    turtle.left(45)
    set_color(2)
    turtle.backward(length)

def draw_tree_3(length):
    """
    A tree of depth 2 is a trunk and two branches.
    :param length:  the segment length
    :pre turtle is at the center, down and facing north
    :post turtle is at the center, down and facing north
    """
    set_color(3)
    turtle.forward(length)
    turtle.left(45)
    draw_tree_2(length/2)
    turtle.right(90)
    draw_tree_2(length/2)
    turtle.left(45)
    set_color(3)
    turtle.backward(length)

def draw_tree_4(length):
    set_color(4)
    turtle.forward(length)
    turtle.left(45)
    draw_tree_3(length/2)
    turtle.right(90)
    draw_tree_3(length/2)
    turtle.left(45)
    set_color(4)
    turtle.backward(length)

def draw_tree(length, depth):
    """
    Draw the tree at the current depth of detail.
    :param length: length of the segments
    :param depth: the current level of detail we are at
    :pre turtle is at the center, down and facing north
    :post turtle is at the center, down and facing north
    """
    if depth == 0:                 # the base case is when depth is 0
        pass
    elif depth >= 1:               # the recursive case handles depths 1-N
        set_color(depth)
        turtle.forward(length)
        turtle.left(45)
        draw_tree(length/2, depth-1)
        turtle.right(90)
        draw_tree(length/2, depth-1)
        turtle.left(45)
        set_color(depth)
        turtle.backward(length)

def main():
    """
    The main program prompts for the depth and then calls the recursive
    drawing function, draw_shapes, to draw the complete image.
    """
    depth = int(input('Enter depth: '))
    init(depth)
    draw_tree(200, depth)
    turtle.done()

if __name__ == '__main__':
    main()