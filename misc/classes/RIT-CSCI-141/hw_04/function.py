"""
File:   function.py
Author: Stanley Goodwin (2/1/2022)
Class:  CSCI 141, 10:00am - 12:00pm

Description:
    Using tail-recursion and iteration approaches
    to a piecewise function give in the prompt.
"""



def fun_rec(x: int, y: int) -> int:
    """
    Description :
        Evaluates the given piecewise function from the pdf 
        description of the homework. Uses tail-recursion to
        find the value of the function.

    Preconditions :
        Parameter x: Integer value
        Parameter y: Integer value

    Postconditions :
        returns value at the given x, y of the piecewise
        function.
    """
    if x <= 0 and y <= 0:
        return 1
    elif x > 0 and y <= 0:
        return x
    else:
        return fun_rec(x - 1, y - 1) + x + y

def test_fun_rec() -> None:
    """
    Description :
        Evaluates the given piecewise function using the 
        tail-end recursive approach at multiple points in
        order to verify integrity and accuracy of the 
        fun_rec() function.

    Preconditions :
        Takes no parameters (values are hard-coded)

    Postconditions :
        Prints the evaluated function's value to console.
    """
    print(
        fun_rec(31,  0),
        fun_rec(-2, -1),
        fun_rec(-7,  3),
        fun_rec( 0, -1),
        fun_rec( 0,  4),
        fun_rec( 3, -9),
        fun_rec( 1,  2),
        fun_rec(27,  5),
        fun_rec(14,  8)
    )



def fun_iter(x: int, y: int) -> int:
    """
    Description :
        Evaluates the given piecewise function from the pdf 
        description of the homework. Uses iteration to find
        the value of the function.

    Preconditions :
        Parameter x: Integer value
        Parameter y: Integer value

    Postconditions :
        returns value at the given x, y of the piecewise
        function.
    """
    _temp = 0

    if x <= 0 and y <= 0:
        return 1
    elif x > 0 and y <= 0:
        return x
    
    while y > 0:
        _temp += x; x -= 1
        _temp += y; y -= 1

    return _temp

def test_fun_iter() -> None:
    """
    Description :
        Evaluates the given piecewise function using an 
        iterative approach at multiple points in order 
        to verify integrity and accuracy of the fun_rec() 
        function.

    Preconditions :
        Takes no parameters (values are hard-coded)

    Postconditions :
        Prints the evaluated function's value to console.
    """
    print(
        fun_rec( 31,  0),
        fun_rec(-2, -1),
        fun_rec(-7,  3),
        fun_rec( 0, -1),
        fun_rec( 0,  4),
        fun_rec( 3, -9),
        fun_rec( 1,  2),
        fun_rec(27,  5),
        fun_rec(14,  8)
    )



def main() -> None:

    # Initial console message
    print("Select the function to use:")
    print("1. Recursive")
    print("2. Iterative")

    # Selection phase
    _select_id = int(input("Please select a function: "))

    # Input values for the function to evaluate
    _select_x  = int(input("\nPlease enter the first number: " ))
    _select_y  = int(input(  "Please enter the second number: "))

    # Determines the result
    _output = None
    if _select_id == 1:
        _output = fun_rec(_select_x, _select_y)
    elif _select_id == 2:
        _output = fun_iter(_select_x, _select_y)
    
    # Print resultant value
    print(f"\nThe value of f(x,y) is {_output}")



if __name__ == "__main__":
    main()