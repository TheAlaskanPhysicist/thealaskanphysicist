"""
File:   intercepts.py
Author: STANLEY GOODWIN (1/12/2021)
Class:  CSCI 141, 10:00am - 12:00pm

Description:
    First degree polynomials (linear functions) are generally written in
    the form y = mx + b. Given (m,b), this file provides a few tests and
    algorithms for solving such problems.
"""



def no_x_intercept(m, b) -> bool:
    """
    Takes in slope 'm' and y-intercept 'b'.
    Returns whether or not function crosses the x-axis.
    """

    # If there is no slope and not already on x-axis, return true
    if m == 0 and b != 0:
        return True
    else:
        return False


def x_intercept(m, b):
    """
    Takes in slope 'm' and y-intercept 'b'.
    Returns the x-intercept of the function.
    """

    # Infinities-avoidance case
    if m == 0 and b == 0:
        return 0

    # If intercept exists, return x-value of intercept
    if not no_x_intercept(m, b):
        return -b / m
    else:
        return None


def y_intercept(m, b):
    """
    Takes in slope 'm' and y-intercept 'b'.
    Returns the y-intercept of the function.
    """

    return b


def print_point(x, y) -> None:
    """
    Takes in x & y numerical values.
    Prints ordered pair output to console. Returns none.
    """

    # Print function(s)
    if x is None:
        print("(NONE)", end = " ")
    else:
        print("({:.3f}, {:.3f})".format(x, y), end = " ")


def test_case(m, b) -> None:
    """
    Takes in slope 'm' and y-intercept 'b'.
    Prints equation and points of intercept to console.
    """

    # Print function(s)
    print(f"Equation: Y = {m} X + {b}.  \tIntercepts:", end = "")
    print_point(x_intercept(m, b), 0.0)
    print_point(0.0, y_intercept(m, b))
    print() # Newline


def test_all() -> None:
    """
    Takes in nothing.
    Runs 10 different tests of the test_case.
    """

    # Test cases
    test_case(-1, -1)
    test_case(-1, 0)
    test_case(-1, 1)
    test_case(0, -1)
    test_case(0, 0)
    test_case(0, 1)
    test_case(1, -1)
    test_case(1, 0)
    test_case(1, 1)
    test_case(-2, -5)



def main() -> None:
    test_all()

if __name__ == "__main__":
    main()