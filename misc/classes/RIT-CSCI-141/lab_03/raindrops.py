"""
File:   raindrops.py
Author: Stanley Goodwin (2/3/2022)
Class:  CSCI 141, 10:00am - 12:00pm

Description:
    Drawing raindrops in a "pool" of water using
    recursional and iterational functions.
"""
import turtle as tt
import random
import math



""" The Square Radius of the pond """
POND_RADIUS = 200

""" Maximum number of raindrops """
MAX_RAINDROPS = 100

""" Maximum radius of raindrops """
MAX_RAINDROPS_RADIUS = 20

""" Number of ripples """
MIN_RIPPLE_NUMBER = 3
MAX_RIPPLE_NUMBER = 8



def _init() -> None:
    """
    Description :
        Initializes the turtle. Draws the canvas of the pond
        and changes some turtle properties.

    Preconditions :
        N/A

    Postconditions :
        Places turtle at (0, 0)
        Sets default color to black.
        Sets Turtle speed to 0.
        Hides the turtle from the screen.
    """

    # Turtle initial settings
    tt.speed(0)
    tt.hideturtle()
    tt.color("black")
    tt.pu()
    tt.setpos(-POND_RADIUS, -POND_RADIUS)
    tt.pd()

    # Draw square
    tt.fillcolor("light sky blue")
    tt.begin_fill()
    tt.forward(2 * POND_RADIUS)
    tt.left(90)
    tt.forward(2 * POND_RADIUS)
    tt.left(90)
    tt.forward(2 * POND_RADIUS)
    tt.left(90)
    tt.forward(2 * POND_RADIUS)
    tt.left(90)
    tt.end_fill()

    # Return to center
    tt.pu()
    tt.setpos(0, 0)


def draw_circle(gap: int, radius: int) -> float:
    """
    Description :
        Draws a circle from a center point with
        specified radius.

    Preconditions :
        Parameter gap:    Integer value, The gap between rings of the last position
        Parameter radius: Integer value, The radius of the circle

    Postconditions :
        Turtle is facing left, and moved down by GAP units relative to initial position.
        Returns the circumference of the circle.
    """
    tt.pu()
    tt.right(90)
    tt.forward(gap)
    tt.left(90)
    tt.pd()
    tt.circle(radius)
    return 2 * math.pi * radius


def draw_raindrop() -> float:
    """
    Description :
        Draws a random raindrop within the canvas of the pond.

    Preconditions :
        Note: Relative position is irrelevent due to setpos().
        N/A

    Postconditions :
        Turtle at position _x_pos and _y_pos.
        Returns the sum of the circumferences of the ripples.
    """
    
    # Random number generated values
    _radius = random.randint(1, MAX_RAINDROPS_RADIUS)
    _ripples = random.randint(MIN_RIPPLE_NUMBER, MAX_RIPPLE_NUMBER)
    _x_pos = random.randint(-POND_RADIUS + _radius, POND_RADIUS - _radius)
    _y_pos = random.randint(-POND_RADIUS + _radius, POND_RADIUS - _radius)
    _fill_color = ( random.random(), random.random(), random.random() )

    # Move to position
    tt.pu()
    tt.setpos(_x_pos, _y_pos)
    tt.pd()

    # Draw Raindrop circle
    tt.fillcolor(_fill_color)
    tt.begin_fill()
    _drop_circumference = draw_circle(_radius, _radius)
    tt.end_fill()

    # More conditions
    _bound_limit_x = (POND_RADIUS - abs(_x_pos)) // _radius - 1
    _bound_limit_y = (POND_RADIUS - abs(_y_pos)) // _radius - 1
    _ripples = min(_ripples, _bound_limit_x, _bound_limit_y)

    # Draw ripples
    _accum_radius = _radius
    while _ripples > 0:
        _accum_radius += _radius
        draw_circle(_radius, _accum_radius)
        _ripples -= 1

    # Finalize
    return _drop_circumference


def draw_raindrops_recursive(n: int, above: float) -> float:
    """
    Description :
        Recursively draws raindrops until n = 0.

    Preconditions :
        Parameter n: Integer value, Number of raindrops
        Parameter above: Floating point number, the sum of the previous raindrops

    Postconditions :
        Returns the sum of all the circumferences of the ripples
    """
    if n == 0:
        return above
    else:
        _new = draw_raindrop()
        return draw_raindrops_recursive(n - 1, _new + above)


def main() -> None:

    # Initialize
    _init()

    # Prompt user for raindrop quantity
    _number_of_rain_drops = int(input(f"Raindrops (1-{MAX_RAINDROPS}): "))

    # IF number in allowed range, run program
    if _number_of_rain_drops >= 1 and _number_of_rain_drops <= MAX_RAINDROPS:
        _total = draw_raindrops_recursive(_number_of_rain_drops, 0)
        print(f"The total circumferences of all the ripples is {_total} units.")

    # ELSE print error message and return
    else:
        print("Raindrops must be between 1 and 100 inclusive.")
        return


# Main guard
if __name__ == "__main__":
    main()
    tt.done()