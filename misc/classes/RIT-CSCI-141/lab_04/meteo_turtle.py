"""
    meteo_turtle.py
    assignment: lab 4
    language: python3
    author: Stanley Goodwin
    description:
        interprets a string of text as a command
        sequence of turtle draw commands.
"""

import meteo
import turtle as tt



# Interpretter function
def interpretter(command_string: str):
    """
    Takes in a user command and does the actions
    provided from the string.
    A string interpretter, if you will.

    :Param input_string: The command string.
    :pre-conditions: Turtle faces east, pen up, color black.
    :post-conditions: Turtle faces east, pen up, color black.
    :returns input_string: None
    """

    # Add breakline to end of string
    command_string += "\r"

    # Loop until command string is empty
    while True:

        # Check if string complete
        if command_string == "\r":
            tt.color("black")
            break

        # Char at the front
        _char = command_string[0]

        if _char == "S":
            command_string = command_string[1:]
            meteo.draw_sun()
            
        elif _char == "P":
            command_string = command_string[1:]
            meteo.draw_sun()
            meteo.draw_cloud()

        elif _char == "C":
            command_string = command_string[1:]
            meteo.draw_cloud()

        elif _char == "R":
            command_string = command_string[1:]
            meteo.draw_rain()
        
        elif _char == "W":
            command_string = command_string[1:]
            meteo.draw_snow()

        elif _char == "T":
            _temp = _command_T(command_string)
            if _temp is None:
                print("There was an error with T#")
                return None
            command_string = _temp

        elif _char == "A":
            _temp = _command_A(command_string)
            if _temp is None:
                print("There was an error with A#")
                return None
            command_string = _temp

        elif _char == "G":
            _temp = _command_G(command_string)
            if _temp is None:
                print("There was an error with G#,#")
                return None
            command_string = _temp
        
        else:
            print(f"Character {_char} is not defined the scope of this command language.")
            return



# I made these ones separate functions because they were significantly 
# long enough for it to warrent their own function
def _command_T(input_string: str) -> str:
    """
    Draws a rectangle at the turtle's present point with
    the temperature, and returns the command string 
    excluding the T's execution.

    :Param input_string: The original command string.
    :pre-conditions: Turtle faces east, pen up.
    :post-conditions: Turtle faces east, pen up.
    :returns input_string: The modified command string.
    """

    # Remove command letter
    input_string = input_string[1:]

    # Get the temperature and remove from string
    _temperature = _get_number(input_string)
    if _temperature is None:
        return None
    input_string = input_string[len(_temperature):]

    # Command execution
    meteo.draw_temperature(int(_temperature))

    # Return rest of command
    return input_string

def _command_A(input_string: str) -> str:
    """
    Draws a red circle at the turtle's present point
    and returns the command string excluding the A's execution.

    :Param input_string: The original command string.
    :pre-conditions: Turtle faces east, pen up.
    :post-conditions: Turtle faces east, pen up.
    :returns input_string: The modified command string.
    """

    # Remove command letter
    input_string = input_string[1:]

    # Get the radius and remove from string
    _radius = _get_number(input_string)
    if _radius is None:
        return None
    input_string = input_string[len(_radius):]

    # Command execution
    meteo.draw_warning(int(_radius))

    # Return rest of command
    return input_string

def _command_G(input_string: str) -> str:
    """
    Runs through the G command and returns the command
    string excluding the G's execution.

    :Param input_string: The original command string.
    :pre-conditions: Turtle pen up.
    :post-conditions: Turtle moves to _x, _y, pen up.
    :returns input_string: The modified command string.
    """
    
    # Remove command letter
    input_string = input_string[1:]

    # Get first number and remove from string (and comma)
    _x = _get_number(input_string)
    if _x is None:
        return None
    input_string = input_string[len(_x) + 1:]

    # Get second number and remove from string
    _y = _get_number(input_string)
    if _y is None:
        return None
    input_string = input_string[len(_y):]

    # Command execution
    tt.goto(int(_x), int(_y))

    # Return rest of command
    return input_string

def _get_number(command_string: str) -> str:
    """
    Runs through the string and returns the number
    contained in the beginning.

    :Param command_string: The original command string.
    :pre-conditions: N/A
    :post-conditions: N/A
    :returns number: The number from the string.
        returns None if no number is found.
    """

    # If number starts with negative
    if command_string[0] == "-":
        _output = "-"
        command_string = command_string[1:]
    else:
        _output = ""

    # Find digits
    while command_string[0].isdigit():
        _output += command_string[0]
        command_string = command_string[1:]
    
    # Return conditions
    if _output == "":
        return None
    else:
        return _output



def main():
    # Draw background
    meteo.background()

    # Turtle preconditions
    tt.pu()
    tt.speed(0)
    
    # User command string
    _user_command_string = input("Command String: ")

    # Interpret command
    interpretter(_user_command_string)

    # Waits for user to close
    tt.done()



if __name__ == "__main__":
    main()