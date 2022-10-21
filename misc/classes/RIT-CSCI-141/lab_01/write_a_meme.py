import turtle as tt
import math



"""
File:   write_a_meme.py
Author: STANLEY GOODWIN (1/12/2021)
Class:  CSCI 141, 10:00am - 12:00pm

Description:
    Using Turtle, a meme-like statement in Tom's name is drafted to the Turtle output screen.
    File executes as a standalone.

Standards:
    Default position of each initial text is from the bottom left.
    Final position after draw should be the bottom left of the next letter.
    Pen Operations come before Rotation comes before Movement.

Known issues:
    Turtle definition is not contained to class. All other programs that...
    modify the import turtle will be executed on the main screen.
"""



# Control Panel [All units are pixels]
SCALE_FACTOR = 1.5
TEXT_HEIGHT = 45 * SCALE_FACTOR # Default height of the text
TEXT_WIDTH  = 30 * SCALE_FACTOR # Default width of the text
TEXT_SPACE  = 10 * SCALE_FACTOR # Default width of space between letters
WORD_SPACE  = 20 * SCALE_FACTOR # Default width of space between words (after implicit text space)



# Letter Functions [Alphabetical Order]
def word_space() -> None:
    tt.forward(WORD_SPACE)

def letter_E() -> None:
    """ Writes the letter E to turtle output window relative to current position. """

    # Init move
    tt.penup()
    tt.left(90)

    # Draw spine
    tt.pendown()
    tt.forward(TEXT_HEIGHT)
    tt.right(90)
    
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

    # Branch 3
    tt.pendown()
    tt.forward(TEXT_WIDTH)
    
    # Move to end
    tt.penup()
    tt.forward(TEXT_SPACE)

def letter_F() -> None:
    """ Writes the letter F to turtle output window relative to current position. """

    # Init move
    tt.penup()
    tt.left(90)

    # Draw spine
    tt.pendown()
    tt.forward(TEXT_HEIGHT)
    tt.right(90)
    
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

    # Move to end
    tt.penup()
    tt.forward(TEXT_WIDTH)
    tt.forward(TEXT_SPACE)

def letter_I() -> None:
    """ Writes the letter I to turtle output window relative to current position. """

    # Init move
    tt.penup()
    tt.forward(TEXT_WIDTH / 2)
    tt.left(90)

    # Draw spine
    tt.pendown()
    tt.forward(TEXT_HEIGHT)

    # Spine to top
    tt.penup()
    tt.left(90)
    tt.forward(TEXT_WIDTH / 2)
    tt.left(180)

    # Draw top
    tt.pendown()
    tt.forward(TEXT_WIDTH)

    # Top to bottom
    tt.penup()
    tt.left(180)
    tt.forward(TEXT_WIDTH)
    tt.left(90)
    tt.forward(TEXT_HEIGHT)
    tt.left(90)

    # Draw bottom
    tt.pendown()
    tt.forward(TEXT_WIDTH)

    # Move to end
    tt.penup()
    tt.forward(TEXT_SPACE)

def letter_L() -> None:
    """ Writes the letter L to turtle output window relative to current position. """

    # Init move
    tt.penup()
    tt.left(90)
    tt.forward(TEXT_HEIGHT)
    tt.left(180)

    # Draw spine
    tt.pendown()
    tt.forward(TEXT_HEIGHT)

    # Draw bottom
    tt.left(90)
    tt.forward(TEXT_WIDTH)

    # Move to end
    tt.penup()
    tt.forward(TEXT_SPACE)

def letter_M() -> None:
    """ Writes the letter M to turtle output window relative to current position. """

    # Local constants
    _MIDDLE_HEIGHT = TEXT_HEIGHT / 2
    _MIDDLE_LENGTH = (_MIDDLE_HEIGHT ** 2 + (TEXT_WIDTH / 2) ** 2) ** 0.5
    _MIDDLE_ANGLE  = 90 - (180 / math.pi) * math.atan((TEXT_WIDTH / 2) / _MIDDLE_HEIGHT)

    # Init move
    tt.penup()
    tt.left(90)

    # Draw Leg 1
    tt.pendown()
    tt.forward(TEXT_HEIGHT)
    tt.right(90)

    # Draw Middle
    tt.right(_MIDDLE_ANGLE)
    tt.forward(_MIDDLE_LENGTH)
    tt.left(2 * _MIDDLE_ANGLE)
    tt.forward(_MIDDLE_LENGTH)
    tt.right(_MIDDLE_ANGLE)

    # Draw Leg 2
    tt.right(90)
    tt.forward(TEXT_HEIGHT)
    tt.penup()
    
    # Move to end
    tt.left(90)
    tt.forward(TEXT_SPACE)

def letter_O() -> None:
    """ Writes the letter O to turtle output window relative to current position. """

    # Init move
    tt.penup()
    tt.forward(TEXT_HEIGHT / 2)

    # Draw circle
    tt.pendown()
    tt.circle(TEXT_HEIGHT / 2)

    # Move to end
    tt.penup()
    tt.forward(TEXT_HEIGHT / 2)
    tt.forward(TEXT_SPACE)

def letter_S() -> None:
    """ Writes the letter S to turtle output window relative to current position. """

    # Init move (Top Right)
    tt.penup()
    tt.forward(TEXT_WIDTH)
    tt.left(90)
    tt.forward(TEXT_HEIGHT)
    tt.left(90)
    
    # Draw Snake (S-curve)
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

    # Move to end
    tt.penup()
    tt.forward(TEXT_WIDTH)
    tt.forward(TEXT_SPACE)

def letter_T() -> None:
    """ Writes the letter T to turtle output window relative to current position. """

    # Init move
    tt.penup()
    tt.forward(TEXT_WIDTH / 2)
    tt.left(90)

    # Draw spine
    tt.pendown()
    tt.forward(TEXT_HEIGHT)

    # Spine to top
    tt.penup()
    tt.left(90)
    tt.forward(TEXT_WIDTH / 2)
    tt.left(180)

    # Draw top
    tt.pendown()
    tt.forward(TEXT_WIDTH)

    # Move to end
    tt.penup()
    tt.right(90)
    tt.forward(TEXT_HEIGHT)
    tt.left(90)
    tt.forward(TEXT_SPACE)



# 2nd-Order Functions
def turtle_canvas_setup():
    ''' The function that sets up the turtle output console. '''

    # Title of the application
    _TITLE = "Tom Meme"
    tt.title(_TITLE)

    # Initial position
    tt.penup()
    tt.backward(300)

    # Speed modifier [Disabled]
    #tt.speed(1)

def draw_message():

    ''' Executes the message to be sent on the turtle output console. '''

    # Message: TOM IS LIFE
    letter_T()
    letter_O()
    letter_M()
    word_space()
    letter_I()
    letter_S()
    word_space()
    letter_L()
    letter_I()
    letter_F()
    letter_E()



# Testing Functions
def test_tom():
    ''' Used for testing the word TOM on screen. '''
    letter_T()
    letter_O()
    letter_M()

def test_space():
    ''' Used for testing the word_space function between 2 letters on screen. '''
    letter_I()
    word_space()
    letter_O()



# The startup program
def main() -> None:

    # Setup function
    turtle_canvas_setup()

    # Draws message
    draw_message()

    # Ends drawing
    tt.done()



# Guard
if __name__ == "__main__":
    main()