"""
File:   zigzagBW.py
Author: STANLEY GOODWIN (1/26/2021)
Class:  CSCI 141, 10:00am - 12:00pm

Description:
    Drawing some funky lines with Turtle.
    Uses recursion to make a zigzag
"""
import turtle as tt



def draw_zigzag(length, depth):
    """
    Description : 
        Recursively draw the zig-zag shape.
        : param length : ( int ) The length of the current segment(s)
        : param depth  : ( int ) The current depth of recursion
    
    Preconditions :
        depth >= 0, length > 0,
        turtle is facing relative east to initial position
        turtle pen is down.

    Postconditions :
        Segment(s) of the zig-zag were drawn for the current depth (and below),
        turtle rotation returned to the centroid of the drawn object (east on depth call: 1),
        turtle pen is down.
    """

    # Base case
    if depth == 0:
        return 0

    # Leg 1
    tt.left(90)
    tt.forward(length / 2)
    tt.right(90)
    tt.forward(length)

    # Recursion 1
    _rs = draw_zigzag(length / 2, depth - 1)

    # Centroid
    tt.left(180)
    tt.forward(length)
    tt.left(90)
    tt.forward(length)
    tt.right(90)
    tt.forward(length)

    # Recursion 2
    tt.left(180)
    _ls = draw_zigzag(length / 2, depth - 1)

    # Leg 2
    tt.forward(length)
    tt.left(90)
    tt.forward(length / 2)
    tt.right(90)

    return 3 * length + _rs + _ls



def main():

    # Turtle settings
    tt.speed(0)

    # Local variables
    _length = 100
    _depth = int(input("Enter number of levels: "))

    # Draws zig-zag and returns total segments length.
    # Prints total length to console
    _total = draw_zigzag(_length, _depth)
    print(f"Total length of all the zig-zag segments: {_total}")



if __name__ == "__main__":
    main()
    tt.done()