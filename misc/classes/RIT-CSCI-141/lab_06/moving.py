"""
File: moving.py
Name: Stanley Goodwin
Date: 3/23/2022

Description:
    Using Dataclasses, we are exploring putting items into boxes efficiently
    whilst also using said dataclasses to be more readable and customizable.
"""
from dataclasses import dataclass
from copy import deepcopy # I had to do this because it was changing my lists


@dataclass
class Item:
    name: str = None  # The name of the item in question
    weight: int = 0  # The weight of that item


@dataclass
class Box:
    capacity_max: int  # The max capacity of the box
    capacity_cur: int  # The current capacity of the box (default matches max)
    contents: dict  # The items stored within the box


def generate_empty_box(max_capacity) -> Box:
    """
    Generates an empty box with max capacity specified in parameters.

    :param max_capacity: The maximum capacity of the box.
    :return Box: The empty box-object
    """
    return Box(max_capacity, max_capacity, [])


def read_file(file_name):

    # Open box and read content
    with open(file_name, "r") as f:
        content = f.readlines()

    # Create boxes
    boxes_max_values = content[0].strip().split()
    boxes = []
    for capacity in boxes_max_values:
        new_box = generate_empty_box(int(capacity))
        boxes.append(new_box)

    # Create items
    items = []
    for line in content[1:]:
        data = line.strip().split()
        name = data[0]
        weight = int(data[1])
        items.append(Item(name, weight))

    # Return data
    return boxes, items


def sort_items_by_decreasing_weight(items: list[Item]) -> list[Item]:
    """
    Sorts an items list by decreasing weight.
    Returns the sorted list to the function (intentional).

    :param items: The list of items to be sorted.
    :return sorted_list: The sorted list.
    """

    # Sort the items by weight (most to least)
    sorted_items = []
    for dummy in range(len(items)):  # Loops as many times as there are items

        # Sets minimum to 0th index item
        max_item = items[0]
        max_weight = max_item.weight

        # Checks if any items weigh more than the item
        for item in items[1:]:
            if item.weight > max_weight:
                max_item = item
                max_weight = item.weight

        # Adds the heaviest item to sorted_items, removes it from items
        sorted_items.append(max_item)
        items.remove(max_item)

    # Return sorted list
    return sorted_items


def greedy_1(boxes: list[Box], items: list[Item]):
    """
    Sorts the items by decreasing weight, and add items to the largest available
    box until none left. Returns the list of filled boxes and remaining items.

    :param boxes: The list of boxes to have the items stored in.
    :param items: The list of items to be stored in the boxes.
    :return boxes, items: The list of boxes and remaining items.
    """

    # Sort the items by weight (most to least)
    sorted_items = sort_items_by_decreasing_weight(items)

    # Assign items to boxes (the heaviest item to the least full box)
    unassigned_items = []
    for item in sorted_items:  # Through the sorted items

        # Find the least filled box
        max_box = boxes[0]
        for box in boxes[1:]:
            if box.capacity_cur > max_box.capacity_cur:
                max_box = box

        # Check if box has room for item
        # Otherwise, give item to the biggest box
        if item.weight > max_box.capacity_cur:
            unassigned_items.append(item)
        else:
            max_box.contents.append(item)
            max_box.capacity_cur -= item.weight

    # Return filled boxes and remaining items
    return boxes, unassigned_items


def greedy_2(boxes: list[Box], items: list[Item]):
    """
    Sorts the items by decreasing weight, and add items to the tightest fit of
    box choices. Returns the list of boxes and remaining items.

    :param boxes: The list of boxes to have the items stored in.
    :param items: The list of items to be stored in the boxes.
    :return boxes, items: The list of boxes and remaining items.
    """

    # Sort the items by weight (most to least)
    sorted_items = sort_items_by_decreasing_weight(items)

    # Assign items to boxes (the heaviest item to the least full box)
    unassigned_items = []
    for item in sorted_items:  # Through the sorted items

        # Avoid boxes that can't contain item
        new_boxes = []
        for box in boxes:
            if box.capacity_cur >= item.weight:
                new_boxes.append(box)

        # Find minimum-sized box
        if len(new_boxes) == 0:
            min_max_box = generate_empty_box(-1)  # The most empty box
        if len(new_boxes) > 0:
            min_max_box = new_boxes[0]
        for box in new_boxes[1:]:
            # If box's capacity is smaller than current best box, select box
            if box.capacity_cur < min_max_box.capacity_cur:
                min_max_box = box

        # Check if box has room for item
        # Otherwise, give item to the biggest box
        if item.weight > min_max_box.capacity_cur:
            unassigned_items.append(item)
        else:
            min_max_box.contents.append(item)
            min_max_box.capacity_cur -= item.weight

    # Return filled boxes and remaining items
    return boxes, unassigned_items


def greedy_3(boxes: list[Box], items: list[Item]):
    """
    Sorts the items by decreasing weight, and add items the current box until
    all items are considered, then moves onto the next box.

    :param boxes: The list of boxes to have the items stored in.
    :param items: The list of items to be stored in the boxes.
    :return boxes, items: The list of boxes and remaining items.
    """

    # Sort the items by weight (most to least)
    unassigned_items = sort_items_by_decreasing_weight(items)

    # Fill box until full (or tried to)
    for box in boxes:
        for item in unassigned_items:
            if box.capacity_cur >= item.weight:
                box.contents.append(item)
                box.capacity_cur -= item.weight

        for item in box.contents:
            unassigned_items.remove(item)

    # Return filled boxes and remaining items
    return boxes, unassigned_items


def print_box(box: Box, index: int):
    """
    Prints the contents of the box to console (repr equiv).

    :param box: The box to print.
    :param index: The index of the box in the list.
    :return None:
    """

    # Header
    print(f"Box {index} of weight capacity {box.capacity_max}")

    # Contents
    for item in box.contents:
        print(f"\t{item.name} of weight {item.weight}")


def main():

    # Initialize program
    # io_input_file = input("Enter data filename: ")
    io_input_file = "data/items5.txt"
    input_boxes, input_items = read_file(io_input_file)

    # Run 1
    boxes, remaining_items = greedy_1(deepcopy(input_boxes), deepcopy(input_items))
    print("\nResults from Greedy Strategy 1")
    if not len(remaining_items):  # If length of remaining_items is 0, print success.
        print("All items successfully packed into boxes!")
    else:
        print("Unable to pack all items!")
    for i, box in enumerate(boxes):
        print_box(box, i + 1)
    for item in remaining_items:
        print(f"{item.name} of weight {item.weight} got left behind.")

    # Run 2
    boxes, remaining_items = greedy_2(deepcopy(input_boxes), deepcopy(input_items))
    print("\nResults from Greedy Strategy 2")
    if not len(remaining_items):  # If length of remaining_items is 0, print success.
        print("All items successfully packed into boxes!")
    else:
        print("Unable to pack all items!")
    for i, box in enumerate(boxes):
        print_box(box, i + 1)
    for item in remaining_items:
        print(f"{item.name} of weight {item.weight} got left behind.")

    # Run 3
    boxes, remaining_items = greedy_3(deepcopy(input_boxes), deepcopy(input_items))
    print("\nResults from Greedy Strategy 3")
    if not len(remaining_items):  # If length of remaining_items is 0, print success.
        print("All items successfully packed into boxes!")
    else:
        print("Unable to pack all items!")
    for i, box in enumerate(boxes):
        print_box(box, i + 1)
    for item in remaining_items:
        print(f"{item.name} of weight {item.weight} got left behind.")


if __name__ == "__main__":
    main()
