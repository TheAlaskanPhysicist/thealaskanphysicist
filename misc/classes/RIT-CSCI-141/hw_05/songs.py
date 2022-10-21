"""
File:   songs.py
Author: Stanley Goodwin (2/10/2022)
Class:  CSCI 141, 10:00am - 12:00pm

Description:
    Using a text file for lyrics, turtle draws the
    lyrics out as a set of colored squares to create
    a graphical representation of the unicode ranges.
"""
import turtle as tt


def square(color: str) -> None:
    """
        Description:
            Takes in a string for color as an input and
            draws a square of that color at the point the
            turtle happens to be at.
        
        Preconditions:
            [Parameter] color, String, the color of the
            square to be drawn.\n
            Turtle is facing east, pen down.

        Postconditions:
            Returns none after execution.\n
            Turtle has pen down, and moved 10 units to the
            east relative to the starting position.
    
    """

    # Color selector [default is white]
    _color_tuple = (255, 255, 255)
    if   color == "red"   : _color_tuple = (255,   0,   0)
    elif color == "green" : _color_tuple = (  0, 255,   0)
    elif color == "blue"  : _color_tuple = (  0,   0, 255)
    elif color == "orange": _color_tuple = (255, 128,   0)
    elif color == "yellow": _color_tuple = (255, 255,   0)
    tt.color(_color_tuple)

    # Draw square
    tt.pd()
    tt.begin_fill()
    for i in range(4):
        tt.forward(10)
        tt.left(90)
    tt.end_fill()
    
    # Move to next corner for square
    tt.pu()
    tt.forward(10)
    tt.pd()


def paint_line(line_from_text_file: str) -> None:
    """
        Description:
            Takes a line in (as string) and draws a row of 
            colored squares who's color is dependent on the 
            unicode of the character.
        
        Preconditions:
            [Parameter] line_from_text_file, String, the line 
            of the lyric that will be drawn.\n
            Turtle is facing east, pen down.
        
        Postconditions:
            Returns none after execution.\n
            Turtle has pen down, and is returned to initial 
            position, then moved down for a new line to be painted.
    """

    # Color constants
    _COLOR_1 = "red"
    _COLOR_2 = "green"
    _COLOR_3 = "blue"
    _COLOR_4 = "orange"
    _COLOR_5 = "yellow"

    # Format line from text file
    _text = line_from_text_file.strip(" \n")

    # Draw square for every character in text
    _accum_x_axis = 0
    for char in _text:
        _unicode = ord(char)
        if   _unicode < 70 : square(_COLOR_1)
        elif _unicode < 100: square(_COLOR_2)
        elif _unicode < 110: square(_COLOR_3)
        elif _unicode < 122: square(_COLOR_4)
        else:                square(_COLOR_5)
        _accum_x_axis += 10
    
    # Return turtle to initial position
    # Moves turtle down to next line for next draw.
    tt.pu()
    tt.back(_accum_x_axis)
    tt.right(90)
    tt.forward(10)
    tt.left(90)
    tt.pd()


def picture(file_name: str) -> None:
    """
        Description:
            Takes in a file with lyrics and draws all the lines
            of the lyrics with colored squares based on their
            unicode ids.

        Preconditions:
            [Parameter] file_name, String, the name of the file
            in the current working directory (local directory).\n
            Turtle is facing east, pen up, and positioned in the
            top-left corner of the canvas.

        Postconditions:
            Returns nothing after execution.\n
            Turtle is facing east, pen up, and moved from top-left 
            to bottom-left corner.
    """
    # The picture() function takes one parameter as input, a file name, opens the file,
    # and draws the picture by calling the paint line() function for each line of text in
    # the file. The picture() starts drawing in the upper left corner of the canvas.

    _file = open(file_name, "r")
    for line in _file:
        paint_line(line)
    _file.close()


def init() -> None:
    """
        Description:
            Initializes some settings for turtle and a few
            other parameters. Normally included in main(),
            but I chose to include them separately.
    """
    
    # Turtle settings
    tt.colormode(255)
    tt.speed(0)
    #tt.tracer(0, 0)

    # Move turtle to top left corner
    tt.pu()
    tt.setpos(-350, 250)


def main():

    # Initial condition stuff
    init()

    # Prompt user for file name
    _file_name = input("File Name: ")

    # Runs picture generation
    picture(_file_name)

    # Stops drawing closure
    tt.done()


# Main guard
if __name__ == "__main__":
    main()