"""
    meteo_turtle.py
    assignment: lab 4
    language: python3
    author: Stanley Goodwin

"""
import meteo


def interpretter(command_string: str):

    # Loop until command over
    while command_string != "":

        # Char at the front
        _cmd_char = command_string[0]

        if _cmd_char == "S":
            print("meteo.draw_sun()")
            #meteo.draw_sun()
        elif _cmd_char == "P":
            print("meteo.draw_sun()", "meteo.draw_cloud()")
            #meteo.draw_sun()
            #meteo.draw_cloud()
        elif _cmd_char == "C":
            print("meteo.draw_cloud()")
            #meteo.draw_cloud()
        elif _cmd_char == "R":
            print("meteo.draw_cloud()", "meteo.draw_rain()")
            #meteo.draw_cloud()
            #meteo.draw_rain()
        
        command_string = command_string[1:]



def get_number(command_string: str) -> int:

    # Accumulation output
    _output = ""

    # Find digits
    while command_string[0].isdigit():
        _output += command_string[0]
        command_string = command_string[1:]
    
    # Return conditions
    if _output != "":
        return _output
    else:
        return None



def main():
    _user_command_string = input("Command String: ")
    interpretter(_user_command_string)


if __name__ == "__main__":
    main()