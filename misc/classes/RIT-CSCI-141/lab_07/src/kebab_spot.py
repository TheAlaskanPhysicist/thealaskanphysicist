"""
A dataclass that represents "spots" on the skewer and functions that work
with it.

author: RITCS
author: Stanley Goodwin
"""

from dataclasses import dataclass
from typing import Union
from food import Food, veggies_set


@dataclass
class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a Food 'item',
        and a reference to the 'next' spot.
    """
    item: Food
    next: Union[None, "KebabSpot"]


def spot_create(item, next):
    """
    Create a new food item spot on the skewer
    :param item: new food item (Food)
    :param next: next spot
    :return: new spot
    """
    return KebabSpot(item, next)


def spot_name(spot):
    """
    Return the name of the food item in this spot.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: food name
    """
    return spot.item.name


def spot_size(spot):
    """
    Return the number of elements from this KebabSpot instance to the end
    of the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: the number of elements (int)
    """
    temp = 0
    item0 = spot
    while item0 is not None:
        temp += 1
        item0 = item0.next
    return temp


def spot_has(spot, name):
    """
    Return whether there are is a food item from this spot to the end of
    the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :param name: the name (string) being searched for.
    :return True if any of the spots hold a Food item that equals the
    name, False otherwise.
    """
    exists = False
    item0 = spot
    while item0 is not None:
        if spot_name(item0) == name:
            exists = True
            break
        else:
            item0 = item0.next
    return exists


def spot_string_em(spot):
    """
    Return a string that contains the list of items in the skewer from
    this spot down, with a comma after each entry.
    :param: spot (KebabSpot): the current spot on the skewer
    :return A string containing the names of each of the Food items from
    this spot down.
    """
    item0 = spot
    name_list = []  # I'm using a list here, so I can use .join() for better printing
    while item0 is not None:
        temp = spot_name(spot)
        name_list.append(temp)
        item0 = item0.next
    output = "".join(name_list, ", ")
    print(output)


def spot_calories(spot):
    """
    Return the number of calories from this KebabSpot instance to the end
    of the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: the number of calories (int)
    """
    total_calories = 0
    item0 = spot
    while item0 is not None:
        food = item0.item
        calories = food.calories
        total_calories += calories
        item0 = item0.next
    return total_calories

def spot_vegan(spot):
    """
    Returns if this KebabSpot instance to the end of the skewer is vegan.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: the vegan boolean (bool)
    """
    veggies = veggies_set()

    is_vegan = True
    item0 = spot
    while item0 is not None:
        if spot_name(item0) not in veggies:
            is_vegan = False
            break
        else:
            item0 = item0.next
    return is_vegan