"""
File:   baobab.py
Author: STANLEY GOODWIN (1/24/2021)
Class:  CSCI 141, 10:00am - 12:00pm

Description:
    Using recursion in Python combined with turtle drawing in
    order to make a recursive image of houses on houses!
"""
import turtle
import math

PEN_WIDTH = 2
SIDE = 100
ROOT_2 = math.sqrt(2)

def init():
    turtle.up()
    turtle.setpos( -50, -200 )
    turtle.down()
    turtle.speed( 0 )
    turtle.pensize( PEN_WIDTH )
    turtle.down()

########## STUDENTS ####################
#
# You must fill in the code,
# _and_documentation_,
# for the following four functions.
#
########################################

def draw_baobab_1( side ):
    """
    Description :
        Draws the first tree branch in a list of manual branches.
        : param side : ( int ) The length of the current segment(s)

    Preconditions :
        length > 0,
        turtle is facing east,
        turtle pen is down.

    Postconditions :
        Tree is drawn at current level,
        turtle is facing east (returned to initial state),
        turtle pen is down,
        turtle pen color is pink.
    """

    turtle.pencolor("pink")
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(45)
    turtle.forward(side / ROOT_2)
    turtle.left(90)
    turtle.forward(side / ROOT_2)
    turtle.left(135)
    turtle.forward(side)
    turtle.back(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.left(90)


def draw_baobab_2( side ):
    """
    Description :
        Draws the first tree branch in a list of manual branches.
        : param side : ( int ) The length of the current segment(s)

    Preconditions :
        length > 0,
        turtle is facing east,
        turtle pen is down.

    Postconditions :
        Tree is drawn at current level,
        turtle is facing east (returned to initial state),
        turtle pen is down,
        turtle pen color is gray.
    """

    turtle.pencolor("gray")
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(45)
    turtle.forward(side / ROOT_2)

    turtle.left(180)
    draw_baobab_1(side / ROOT_2)
    turtle.pencolor("gray")
    turtle.left(180)

    turtle.left(90)
    turtle.forward(side / ROOT_2)
    
    turtle.left(180)
    draw_baobab_1(side / ROOT_2)
    turtle.pencolor("gray")
    turtle.left(180)

    turtle.left(135)
    turtle.forward(side)
    turtle.back(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.left(90)
    pass



def draw_baobab_3( side ):
    """
    Description :
        Draws the first tree branch in a list of manual branches.
        : param side : ( int ) The length of the current segment(s)

    Preconditions :
        length > 0,
        turtle is facing east,
        turtle pen is down.

    Postconditions :
        Tree is drawn at current level,
        turtle is facing east (returned to initial state),
        turtle pen is down,
        turtle pen color is blue.
    """

    turtle.pencolor("blue")
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(45)
    turtle.forward(side / ROOT_2)

    turtle.left(180)
    draw_baobab_2(side / ROOT_2)
    turtle.pencolor("blue")
    turtle.left(180)

    turtle.left(90)
    turtle.forward(side / ROOT_2)
    
    turtle.left(180)
    draw_baobab_2(side / ROOT_2)
    turtle.pencolor("blue")
    turtle.left(180)

    turtle.left(135)
    turtle.forward(side)
    turtle.back(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.left(90)
    pass



def draw_baobab_rec( side, depth ):
    """
    Description : 
        Recursively draw the tree shape .
        : param depth  : ( int ) The current depth of recursion
        : param length : ( int ) The length of the current segment(s)
    
    Preconditions :
        depth >= 0, length > 0,
        turtle is facing relative east to initial position
        turtle pen is down.

    Postconditions :
        Segment(s) of the tree were drawn for the current depth (and below),
        turtle rotation returned to initial state (east on depth call: 1),
        turtle pen is down.
    """

    if depth == 0:
        return

    # Box Part 1
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(45)
    turtle.forward(side / ROOT_2)

    # Recursion 1
    turtle.left(180)
    draw_baobab_rec(side / ROOT_2, depth - 1)
    turtle.right(90)

    # Box Part 2
    turtle.forward(side / ROOT_2)
    
    # Recursion 2
    turtle.left(180)
    draw_baobab_rec(side / ROOT_2, depth - 1)
    turtle.right(45)

    # Box Part 3
    turtle.forward(side)
    turtle.back(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.left(90)



def main():
    init()
    print( "Drawing a depth-1 baobab drawing." )
    draw_baobab_1( SIDE )
    input( "Hit ENTER to proceed to depth 2:" )
    turtle.clear()
    draw_baobab_2( SIDE )
    input( "Hit ENTER to proceed to depth 3:" )
    turtle.clear()
    draw_baobab_3( SIDE )
    input( "Hit ENTER to proceed to recursive code:" )
    turtle.clear()
    depth = int( input( "depth? " ) )
    draw_baobab_rec( SIDE, depth )
    print( "Close the window to end the program." )
    turtle.done()



if __name__ == '__main__':
    main()