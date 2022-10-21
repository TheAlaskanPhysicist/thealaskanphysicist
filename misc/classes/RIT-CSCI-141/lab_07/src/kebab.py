"""
The main module for running the Shish Kebab program.  It contains the main
loop for the program.  It filters the command line input and then calls on
the Skewer to deal with the appropriate action.

author: RITCS
author: Stanley Goodwin
"""

import sys
from food import FOODS, food_create
from skewer import skewer_create, skewer_close, skewer_add, skewer_front, \
    skewer_remove, skewer_has, skewer_size, skewer_capacity, skewer_string_em, \
    skewer_calories, skewer_vegan
from skewer_exception import SkewerException
from dataclasses import dataclass
from typing import Union

@dataclass
class Kebab:
    """
    Class: Kebab
    Description: A Kebab is composed of a skewer that holds the food
    """
    skewer: Union[None, 'Skewer']

def kebab_create():
    """
    Create and return a new Kebab.
    :return: A new empty kebab
    """
    return Kebab(None)

def kebab_usage():
    """
    Displays the valid commands and their usage.
    :return: None
    """
    print("Kebab commands:")
    print("add item - adds an item to the skewer")
    print("create N - creates a skewer to hold N items")
    print("destroy - destroys the current skewer")
    print("display - displays all the items on the skewer, in order")
    print("eat - eat the front item on the skewer")
    print("foods - display the food items that can be added to the skewer")
    print("front - the front item on the skewer")
    print("has item - is an item on the skewer?")
    print("quit - exit the program")
    print("status - the capacity and current number of items on the skewer")
    print("calories - the total calories of the items on the skewer")
    print("vegan - determines if the items on the skewer are all vegan")

def kebab_create_skewer(kebab, args):
    """
    Create the skewer that will hold the food.
    :param kebab (Kebab): this kebab
    :param args: a string containing the size to create
    :return: None
    """
    try:
        # make sure the capacity is valid
        if len(args) == 0 or int(args[0]) < 1:
            raise SkewerException("Skewer capacity must be greater than 0")
        elif kebab.skewer is not None:
            raise SkewerException("Skewer has already been created")

        # convert it from string to int
        capacity = int(args[0])

        # now make the skewer
        kebab.skewer = skewer_create(capacity)
        print("Skewer created.")
    except SkewerException as e:
        print(e)
        kebab.skewer = None
    except Exception as e:
        sys.stderr.write(e)
        kebab_usage()
        return

def kebab_add(kebab, args):
    """
    Add a specified item to the skewer.
    :param kebab (Kebab): this kebab
    :param args: the name of the item to add
    :return: None
    """
    # the item to add must be provided as the first argument to the list
    if len(args) < 1:
        kebab_usage()
        return

    # the name of the food item is extracted from the front of the list
    name = args[0]

    # check that the name is in the list of valid foods
    if name not in FOODS:
        print("Skewer can only hold these kinds of food: ", FOODS)
        return
    try:
        skewer_add(kebab.skewer, name)
        print(name, "successfully added to the skewer.")
    except SkewerException as e:
        print(e)
        
def kebab_eat(kebab, args):
    """
    Eat the front item on the skewer.
    :param kebab (Kebab): this kebab
    :param args: ignored
    :return: None
    """
    try:
        name = skewer_front(kebab.skewer)
        skewer_remove(kebab.skewer)
        print("Ate", name + ". Yum!")
    except SkewerException as e:
        print(e)

def kebab_has(kebab, args):
    """
    Checks if the skewer holds a certain item.
    :param kebab (Kebab): this kebab
    :param args: the name of the item to search for
    :return: None
    """
    if len(args) < 1:
        kebab_usage()
        return

    name = args[0]
    if skewer_has(kebab.skewer, name):
        print(name, "does exist on the Skewer.")
    else:
        print(name, "doesn't exist on the Skewer.")

def kebab_status(kebab, args):
    """
    Displays the number of items on the skewer and its capacity.
    :param kebab (Kebab): this kebab
    :param args: ignored
    :return: None
    """

    print(str(skewer_size(kebab.skewer)), "out of", skewer_capacity(kebab.skewer),
        "items on the skewer.")
            
def kebab_front(kebab, args):
    """
    Displays the name of the front item on the skewer.
    :param kebab (Kebab): this kebab
    :param args: ignored
    :return: None
    """
    try:
        print(skewer_front(kebab.skewer), "is on the front of the skewer.")
    except SkewerException as e:
        print(e)
                    
def kebab_display(kebab, args):
    """
    Displays the items on the skewer by name.
    :param kebab (Kebab): this kebab
    :param args: ignored
    :return: None
    """
    print("The skewer contains:", skewer_string_em(kebab.skewer))

def kebab_foods(kebab, args):
    """
    Display the valid food items that can be added to the skewer
    :param kebab (Kebab): this kebab (unused)
    :param args: ignored
    :return: None
    """
    print(FOODS)

def kebab_destroy(kebab, args):
    """
    Destroys the skewer if one was previously created.
    :param kebab (Kebab): this kebab
    :param args: ignored
    :return: None
    """
    if kebab.skewer is not None:
        skewer_close(kebab.skewer)
        kebab.skewer = None

def kebab_quit(kebab, args):
    """
    Exit the program.
    :param kebab (Kebab): this kebab
    :param args: ignored
    :return: None
    """
    if kebab.skewer is not None:
        skewer_close(kebab.skewer)
        kebab.skewer = None
    print("Goodbye!")
    sys.exit(0)

def kebab_calories(kebab: Kebab, args):
    """
    Gets the calories of the entire kebab.
    :param kebab (Kebab): this kebab
    :param args: ignored (intentional)
    :return: None
    """
    if kebab.skewer is not None:
        print(skewer_calories(kebab.skewer))
    else:
        print("0 Calories, the skewer is empty.")

def kebab_vegan(kebab: Kebab, args):
    """
    Returns if the kebab is vegan or not.
    :param kebab (Kebab): this kebab
    :param args: ignored (intentional)
    :return: None
    """
    if kebab.skewer is not None:
        is_vegan = skewer_vegan(kebab.skewer)
        print(f"Kebab is {'vegan' if is_vegan else 'not vegan'}")
    else:
        print("Kebab is vegan, the skewer is empty.")

# Each valid command is stored in a dictionary as string by key.
# The corresponding method to call is stored as the value.
CMDS = {"add": kebab_add,
        "create": kebab_create_skewer,
        "destroy": kebab_destroy,
        "eat": kebab_eat,
        "foods" : kebab_foods,
        "has": kebab_has,
        "status": kebab_status,
        "front": kebab_front,
        "display": kebab_display,
        "quit": kebab_quit,
        "calories": kebab_calories,
        "vegan": kebab_vegan
}

def kebab_main_loop(kebab):
    """
    Runs the main command loop by prompting for input and responding.
    :param kebab (Kebab): this kebab
    :return: None
    """

    # the command line prompt
    PROMPT = "> "

    # the command loop runs until the user enters the quit command
    while sys.stdin:
        line = input(PROMPT).split()
        if len(line) == 0:
            continue
        cmd = line[0]
        if cmd in CMDS:
            # if the skewer does not exist, the only valid commands
            # are to create it, list the food items, or quit
            if kebab.skewer is None and cmd != "create" and cmd != "foods" and cmd != "quit":
                print("Skewer has not been created yet.")
            else:
                # strip off the command and pass the remaining line
                # arguments to the appropriate method
                CMDS[cmd](kebab, line[1:])
        else:
            kebab_usage()

def main():
    """The main routine."""
    
    # create a Kebab instance and invoke the main loop
    kebab = kebab_create()
    kebab_main_loop(kebab)

if __name__ == "__main__":
    main()
