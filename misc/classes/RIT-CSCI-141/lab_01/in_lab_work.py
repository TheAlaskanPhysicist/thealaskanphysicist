import turtle as tt
import math

"""
File: write_a_meme.py
STANLEY GOODWIN (1/12/2021)
CSCI 141, 10:00am - 12:00pm

Description:
    Program executes as own console. No return type.
        Meant as standalone project. Not for importation to other files without caution.
    Creates new window under turtle.
    Turtle draws text provided as per instructions of LAB01.
    Default position of each initial text is from the bottom left.

Known issues:
    Turtle definition is not contained to class. All other programs that
        modify the import turtle will be executed on the main screen.
"""

# Control panel
TEXT_HEIGHT = 45*1.5 #  [ UNITS: PIXELS  ] The default height of the text
TEXT_WIDTH  = 30*1.5 #  [ UNITS: PIXELS  ] The default width of the text
TEXT_SPACE  = 10*1.5 #  [ UNITS: PIXELS  ] The default width of space between letters
WORD_SPACE  = 20*1.5 #  [ UNITS: PIXELS  ] The default width of space between words (after implicit text space)



''' Functions for writing letters to the application window '''
''' All letters start at the bottom-left corner, end in the position of the next bottom left corner '''
def letter_T() -> None:
    """
    letter_T takes no input. Writes the letter T to turtle output window.
    Returns nonetype.
    """
    # Draw Letter
    tt.penup()
    tt.forward(TEXT_WIDTH / 2)
    tt.left(90)
    tt.pendown()
    tt.forward(TEXT_HEIGHT)
    tt.left(90)
    tt.penup()
    tt.forward(TEXT_WIDTH / 2)
    tt.left(180)
    tt.pendown()
    tt.forward(TEXT_WIDTH)
    tt.penup()
    tt.right(90)
    tt.forward(TEXT_HEIGHT)
    tt.left(90)

    # Add space
    tt.forward(TEXT_SPACE)

def letter_O() -> None:
    """
    letter_O takes no input. Writes the letter O to turtle output window.
    Returns nonetype.
    """
    # Draw Letter
    tt.penup()
    tt.forward(TEXT_HEIGHT / 2)
    tt.pendown()
    tt.circle(TEXT_HEIGHT / 2)
    tt.penup()
    tt.forward(TEXT_HEIGHT / 2)

    # Add Space
    tt.forward(TEXT_SPACE)

def letter_M() -> None:
    """
    letter_M takes no input. Writes the letter M to turtle output window.
    Returns nonetype.
    """
    # Trig
    _MIDDLE_HEIGHT = TEXT_HEIGHT / 2
    _MIDDLE_LENGTH = (_MIDDLE_HEIGHT ** 2 + (TEXT_WIDTH / 2) ** 2) ** 0.5
    _MIDDLE_ANGLE  = 90 - (180 / math.pi) * math.atan((TEXT_WIDTH / 2) / _MIDDLE_HEIGHT)

    # Draw Leg 1
    tt.penup()
    tt.left(90)
    tt.pendown()
    tt.forward(TEXT_HEIGHT)
    tt.right(90)
    
    # Draw Middle Section
    tt.right(_MIDDLE_ANGLE)
    tt.forward(_MIDDLE_LENGTH)
    tt.left(2 * _MIDDLE_ANGLE)
    tt.forward(_MIDDLE_LENGTH)
    tt.right(_MIDDLE_ANGLE)

    # Draw Leg 2
    tt.right(90)
    tt.forward(TEXT_HEIGHT)
    tt.left(90)
    tt.penup()

    # Add Space
    tt.forward(TEXT_SPACE)

def letter_L() -> None:
    """
    letter_L takes no input. Writes the letter L to turtle output window.
    Returns nonetype.
    """
    # Draw Letter
    tt.pendown()
    tt.left(90)
    tt.forward(TEXT_HEIGHT)
    tt.left(180)
    tt.penup()
    tt.forward(TEXT_HEIGHT)
    tt.left(90)
    tt.pendown()
    tt.forward(TEXT_WIDTH)
    tt.penup()

    # Add space
    tt.forward(TEXT_SPACE)

def letter_I() -> None:
    """
    letter_I takes no input. Writes the letter I to turtle output window.
    Returns nonetype.
    """
    # Draw Letter
    tt.penup()
    tt.forward(TEXT_WIDTH / 2)
    tt.left(90)
    tt.pendown()
    tt.forward(TEXT_HEIGHT)
    tt.left(90)
    tt.penup()
    tt.forward(TEXT_WIDTH / 2)
    tt.left(180)
    tt.pendown()
    tt.forward(TEXT_WIDTH)
    tt.penup()
    tt.left(180)
    tt.forward(TEXT_WIDTH)
    tt.left(90)
    tt.forward(TEXT_HEIGHT)
    tt.left(90)
    tt.pendown()
    tt.forward(TEXT_WIDTH)
    tt.penup()

    # Add space
    tt.forward(TEXT_SPACE)

def letter_F() -> None:
    """
    letter_F takes no input. Writes the letter F to turtle output window.
    Returns nonetype.
    """
    # Draw Spine
    tt.penup()
    tt.left(90)
    tt.pendown()
    tt.forward(TEXT_HEIGHT)
    tt.right(90)
    tt.penup()

    # Branch 1
    tt.pendown()
    tt.forward(TEXT_WIDTH)
    tt.left(180)
    tt.penup()
    tt.forward(TEXT_WIDTH)
    tt.left(90)
    tt.forward(TEXT_HEIGHT / 2)
    tt.left(90)

    # Branch 2
    tt.pendown()
    tt.forward(TEXT_WIDTH)
    tt.left(180)
    tt.penup()
    tt.forward(TEXT_WIDTH)
    tt.left(90)
    tt.forward(TEXT_HEIGHT / 2)
    tt.left(90)

    # Add space
    tt.penup()
    tt.forward(TEXT_WIDTH)
    tt.forward(TEXT_SPACE)

def letter_E() -> None:
    """
    letter_E takes no input. Writes the letter E to turtle output window.
    Returns nonetype.
    """
    # Draw Spine
    tt.penup()
    tt.left(90)
    tt.pendown()
    tt.forward(TEXT_HEIGHT)
    tt.right(90)
    tt.penup()

    # Branch 1
    tt.pendown()
    tt.forward(TEXT_WIDTH)
    tt.left(180)
    tt.penup()
    tt.forward(TEXT_WIDTH)
    tt.left(90)
    tt.forward(TEXT_HEIGHT / 2)
    tt.left(90)

    # Branch 2
    tt.pendown()
    tt.forward(TEXT_WIDTH)
    tt.left(180)
    tt.penup()
    tt.forward(TEXT_WIDTH)
    tt.left(90)
    tt.forward(TEXT_HEIGHT / 2)
    tt.left(90)

    # Branch 2
    tt.pendown()
    tt.forward(TEXT_WIDTH)
    tt.penup()

    # Add space
    tt.forward(TEXT_SPACE)

def letter_S() -> None:
    """
    letter_E takes no input. Writes the letter E to turtle output window.
    Returns nonetype.
    """
    # Move Top Right
    tt.penup()
    tt.forward(TEXT_WIDTH)
    tt.left(90)
    tt.forward(TEXT_HEIGHT)
    tt.left(90)
    
    # Draw S
    tt.pendown()
    tt.forward(TEXT_WIDTH)
    tt.left(90)
    tt.forward(TEXT_HEIGHT / 2)
    tt.left(90)
    tt.forward(TEXT_WIDTH)
    tt.right(90)
    tt.forward(TEXT_HEIGHT / 2)
    tt.right(90)
    tt.forward(TEXT_WIDTH)
    tt.left(180)
    tt.penup()
    tt.forward(TEXT_WIDTH)

    # Add space
    tt.forward(TEXT_SPACE)



# The startup program
def main() -> None:

    # Title of the application
    _TITLE = "Tom Meme"
    tt.title(_TITLE)

    # Set default (Moves cursor over to edge of screen)
    tt.speed(1)
    tt.penup()
    tt.backward(300)

    # Runs the draw functions for the text
    letter_T()
    letter_O()
    letter_M()
    tt.forward(WORD_SPACE)
    letter_I()
    letter_S()
    tt.forward(WORD_SPACE)
    letter_L()
    letter_I()
    letter_F()
    letter_E()

    # Awaits input from user on close (prevents auto-close)
    tt.done()



# Guard
if __name__ == "__main__":
    main()