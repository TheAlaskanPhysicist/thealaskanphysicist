from turtle import *



# Function to draw petal
def draw_petal() -> None:
    """
    draw_petal() runs through 1 rhombus as defined by the lower parameter constants.
    Function moves the turtle to draw the rhombus, returns none.
    """

    # Constants
    _LINE_LENGTH = 50   # [ UNITS: PIXELS  ] The length (in pixels) of the side of the rhombus
    _ANGLE_INNER = 40   # [ UNITS: DEGREES ] The interior angle of the rhombus 
    _ANGLE_OUTER = 140  # [ UNITS: DEGREES ] The exterior angle of the rhombus
    _NEXT_ANGLE  = 60   # [ UNITS: DEGREES ] The angle between the centers of the rhombuses

    # Movement routine of turtle
    forward(_LINE_LENGTH)
    left(_ANGLE_INNER)
    forward(_LINE_LENGTH)
    left(_ANGLE_OUTER)
    forward(_LINE_LENGTH)
    left(_ANGLE_INNER)
    forward(_LINE_LENGTH)
    left(_ANGLE_OUTER)

    # Angle Offset for next petal
    left(_NEXT_ANGLE)



def draw_flower() -> None:
    """
    draw_flower() draws the 6 petals required for the assignment.
    Function replaces the need for a for-loop executing 6 times.
    """

    # Movement routine for the petals
    draw_petal()
    draw_petal()
    draw_petal()
    draw_petal()
    draw_petal()
    draw_petal()



# The startup program
def main() -> None:

    # Title of the application
    _TITLE = "6-figure Snowflake"
    title(_TITLE)

    # Running the draw function
    draw_flower()
    
    # Awaits input from user on close
    input()



# Guard
if __name__ == "__main__":
    main()