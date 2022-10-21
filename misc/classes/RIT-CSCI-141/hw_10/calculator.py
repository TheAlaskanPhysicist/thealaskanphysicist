"""
File: calculator.py
Author: Stanley Goodwin
Date: 3/25/2022

Description:
    Using console input, this is a calculator that find a value using stacks and
    queues to find the final values.
"""
from typing import Any, Union
from dataclasses import dataclass


# NODE DEFINITIONS

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

@dataclass(frozen=False)
class Stack:
    size: int
    top: Union[None, FrozenNode]


def make_empty_stack():
    """
    Returns a new stack with size initialized to zero and
    nodes initialed to the empty list.
    """
    return Stack(0, None)


def push(stack, element):
    """
    Add an element to the top of the stack. The stack state changes.
    """
    stack.top = FrozenNode(element, stack.top)
    stack.size = stack.size + 1


def top(stack):
    """
    Return top element on stack.  Does not change stack.
    precondition: stack is not empty
    """
    if is_stack_empty(stack):
        raise IndexError("top of empty stack")
    return stack.top.value


def pop(stack):
    """
    Remove the top element in the stack and returns the removed value.
    The stack state changes.
    precondition: stack is not empty
    """
    if is_stack_empty(stack):
        raise IndexError("pop on empty stack")
    popped = stack.top.value
    stack.top = stack.top.next
    stack.size = stack.size - 1
    return popped


def is_stack_empty(stack):
    """
    Is the stack empty?
    """
    return stack.top is None


def size(stack):
    """
    Return the # of elements
    """
    return stack.size


# QUEUE DEFINITIONS

@dataclass(frozen=False)
class Queue:
    size: int
    front: Union[None, MutableNode]
    back: Union[None, MutableNode]


def make_empty_queue():
    """
    Returns a new queue with size initialized to zero and
    the front and back fields initialized to the empty sequence.
    """
    return Queue(0, None, None)


def enqueue(queue, element):
    """
    Insert an element into the back of the queue. (Returns None)
    """
    new_node = MutableNode(element, None)
    if is_queue_empty(queue):
        queue.front = new_node
    else:
        queue.back.next = new_node
    queue.back = new_node
    queue.size = queue.size + 1


def dequeue(queue):
    """
    Remove the front element from the queue. (returns removed value)
    precondition: queue is not empty.
    """
    if is_queue_empty(queue):
        raise IndexError("dequeue on empty queue")
    removed = queue.front.value
    queue.front = queue.front.next
    if is_queue_empty(queue):
        queue.back = None
    queue.size = queue.size - 1
    return removed


def front(queue):
    """
    Access and return the first element in the queue without removing it.
    precondition: queue is not empty.
    """
    if is_queue_empty(queue):
        raise IndexError("front on empty queue")
    return queue.front.value


def back(queue):
    """
    Access and return the last element in the queue without removing it
    precondition: queue is not empty.
    """
    if is_queue_empty(queue):
        raise IndexError("back on empty queue")
    return queue.back.value


def is_queue_empty(queue):
    """
    Is the queue empty?
    """
    return queue.front is None


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
            push(stack, val)
        else:
            raise ValueError("Illegal character(s) in input string")


def parser_queue(queue: Queue, input_string: str):
    """
    Parses an input string to write to a queue.
    Catches illegals characters and strings on execution.

    :param queue: The queue to have the string added to.
    :param input_string: The 4-function math string.
    :return None:
    """

    # Split string into components
    phonemes = input_string.split()

    # For all components, add to stack frame if valid character/word
    for val in phonemes:
        if val.isdigit() or val in ["+", "-", "*", "/"]:
            enqueue(queue, val)
        else:
            raise ValueError("Illegal character(s) in input string")


def calculate_stack(stack: Stack):
    """
    Calculates the expression of the input stack and returns value.

    :param stack: The stack of mathematics expression.
    :return value: The expression's value.
    """

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
                # output_value = -(output_value - number)  # Corrected value
                output_value = output_value - number  # Manual value
                flag_subtraction = False
            elif flag_multiply:
                output_value = output_value * number
                flag_multiply = False
            elif flag_division:
                # output_value = number // output_value  # Corrected value
                output_value = output_value // number  # Manual value
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


def calculate_queue(queue: Queue):
    """
    Calculates the expression of the input queue and returns value.

    :param queue: The queue of mathematics expression.
    :return value: The expression's value.
    """

    # Flags
    flag_multiply = False
    flag_division = False
    flag_addition = True
    flag_subtraction = False

    # Calculate parameters
    output_value = 0
    item = queue.front
    while item is not None:
        value = item.value

        # If value is digit
        if value.isdigit():
            number = int(value)
            if flag_addition:
                output_value = output_value + number
                flag_addition = False
            elif flag_subtraction:
                # output_value = -(output_value - number)  # Corrected value
                output_value = output_value - number  # Manual value
                flag_subtraction = False
            elif flag_multiply:
                output_value = output_value * number
                flag_multiply = False
            elif flag_division:
                # output_value = number // output_value  # Corrected value
                output_value = output_value // number  # Manual value
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
    stack_frame = make_empty_stack()
    queue_frame = make_empty_queue()

    # Parse Console Input
    console_io = input("Expression: ")
    parser_stack(stack_frame, console_io)
    parser_queue(queue_frame, console_io)

    # Print result
    stack_value = calculate_stack(stack_frame)
    queue_value = calculate_queue(queue_frame)
    print(f"Queue total: {queue_value}")
    print(f"Stack total: {stack_value}")
    print(f'{"They match!" if queue_value == stack_value else "They do not match!"}')


# Main Guard
if __name__ == "__main__":
    main()
