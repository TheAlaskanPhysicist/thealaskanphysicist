"""
File: calculator.py
Author: Stanley Goodwin
Date: 3/25/2022

"""
from typing import Any, Union
from dataclasses import dataclass


# DATACLASS DEFINITIONS

@dataclass(frozen=True)
class FrozenNode:
    """
    An immutable link node containing a value and a link to the next node.
    """
    value: Any
    next: Union["FrozenNode", None]


@dataclass(frozen=False)
class MutableNode:
    """
    A mutable link node containing a value and a link to the next node.
    """
    value: Any
    next: Union["MutableNode", None]









# STACK DEFINITIONS


@dataclass
class Stack:
    """
    Stack is an object that is the catalyst of immutable nodes in order.
    """
    size: int
    top: Union["ImmutableNode", "None"]


def gen_empty_stack() -> Stack:
    """
    Generates an empty stack object.
    :return Stack: The empty stack object.
    """
    return Stack(0, None)


def s_is_empty(stack: Stack) -> bool:
    """
    Returns a boolean for whether the stack is empty or not.

    :param stack: The stack in question.
    :return boolean: A true/false for if the stack is empty.
    """
    return stack.top is None


def s_pop(stack: Stack) -> any:
    """
    Pops the first node off the top of the list. Returns value of node.

    :param stack: The input stack to pop the item off of.
    :return value: The value of the popped item.
    """

    # Check if stack is empty
    if s_is_empty(stack):
        raise IndexError("The stack is empty.")

    # Get top node's value
    pop_value = stack.top.value

    # Start stack at next node
    stack.top = stack.top.next

    # Return node value
    return pop_value


def s_top(stack: Stack) -> any:
    """
    Reads the value at the top of the stack. Doesn't change stack.

    :param stack: The input stack to read the first item value of.
    :return value: The value of the item.
    """

    # Check if stack is empty
    if s_is_empty(stack):
        raise IndexError("The stack is empty.")

    # Return node value
    return stack.top.value


def s_push(stack: Stack, value: any) -> None:
    """
    Pushes a value onto the top of the parameter stack.

    :param stack: The stack to add the value to.
    :param value: The value to add to the stack.
    :return None:
    """
    stack.top = ImmutableNode(value, stack.top)
    stack.size += 1


def s_size(stack: Stack) -> int:
    """
    Returns the size of the stack queue.

    :param stack: The stack in question.
    :return size: The size of the stack.
    """
    return stack.size


# PROGRAM DEFINITIONS


def parser_stack(stack: Stack, input_string: str):
    """
    Parses an input string to write to the stack.
    Catches illegals characters and strings on execution.

    :param stack: The stack to have the string added to.
    :param input_string: The 4-function math string.
    :return None:
    """

    # Split string into components
    phonemes = input_string.split()

    # For all components, add to stack frame if valid character/word
    for val in phonemes:
        if val.isdigit() or val in ["+", "-", "*", "/"]:
            s_push(stack, val)
        else:
            raise ValueError("Illegal character(s) in input string")


def calculate_stack(stack: Stack):
    """
    Calculates the expression of the input stack and returns value.

    :param stack: The stack of mathematics expression.
    :return value: The expression's value.
    """

    # Check for empty stack
    if stack.size == 0:
        raise ValueError("Input stack was empty.")

    # Flags
    flag_multiply = False
    flag_division = False
    flag_addition = True
    flag_subtraction = False

    # Calculate parameters
    output_value = 0
    item = stack.top
    while item is not None:
        value = item.value

        # If value is digit
        if value.isdigit():
            number = int(value)
            if flag_addition:
                output_value = output_value + number
                flag_addition = False
            elif flag_subtraction:
                output_value = output_value - number
                flag_subtraction = False
            elif flag_multiply:
                output_value = output_value * number
                flag_multiply = False
            elif flag_division:
                output_value = output_value // number
                flag_division = False

        # If value is an operator
        elif value == "+":
            flag_addition = True
        elif value == "-":
            flag_subtraction = True
        elif value == "*":
            flag_multiply = True
        elif value == "/":
            flag_division = True

        # Set next node as next item
        item = item.next

    # Return output
    return output_value


def main():
    """
    Make a queue equivalent.
    Make it solve the problem.
    Check the solutions are the same value.
    PARTY.

    Lecture:
    https://www.cs.rit.edu/~csci141/Lectures/10/StacksQueues-stu.pdf

    Homework:
    https://www.cs.rit.edu/~csci141/Homeworks/10/backwards_calc-stu.pdf

    :return:
    """

    # Empty Stack + Queue Generator
    stack_frame = gen_empty_stack()
    #queue_frame = gen_empty_queue()

    # Parse Console Input
    console_io = input("Expression: ")
    parser_stack(stack_frame, console_io)
    #parser_queue(queue_frame, console_io)

    # Print result
    print(stack_frame)
    print(calculate_stack(stack_frame))


if __name__ == "__main__":
    main()
