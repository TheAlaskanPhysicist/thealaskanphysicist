from turtle import *



# Function to draw petal
def draw_petal(line_length: int) -> None:
    """
    draw_petal() runs through 1 rhombus as defined by the lower parameter constants.
        takes input of line_length to define how long the side of the rhombus is.
    Function moves the turtle to draw the rhombus, returns none.
    """

    # Constants
    _ANGLE_INNER = 40
    _ANGLE_OUTER = 140
    _NEXT_ANGLE = 60

    # Movement
    forward(line_length)
    left(_ANGLE_INNER)
    forward(line_length)
    left(_ANGLE_OUTER)
    forward(line_length)
    left(_ANGLE_INNER)
    forward(line_length)
    left(_ANGLE_OUTER)

    # Angle Offset for next petal
    left(_NEXT_ANGLE)



# The startup program (self-descriptive)
def main() -> None:

    # Length of drawn lines as input
    line_length = int(input("How long is the side length? >>> "))

    # Title of the application
    _TITLE = "6-figure Snowflake"
    title(_TITLE)

    # Try to draw the petals, returns error on fail.
    try:
        # Running the draw function 6 times (for 6 petals)
        for i in range(6):
            draw_petal(line_length)
        
    except Exception as error:
        # Prints error to console
        print(error)

    finally:    
        # Awaits input from user on close
        input()



# Guard
if __name__ == "__main__":
    main()