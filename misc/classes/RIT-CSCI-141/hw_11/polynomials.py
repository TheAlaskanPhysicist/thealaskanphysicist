""" 
Polynomials
In this homework, polynomials are represented using linked lists. Each
term is stored in a node, and the nodes are ordered in descending
order according to their degree. Functions are implemented:
To create a polynomial linked list from file data
To insert a term node to a polynomial linked list
To pretty-print a polynomial
To add two polynomials

Author: RITCS
Author: Stanley Goodwin (3/28/2022)
"""
from typing import Union
from dataclasses import dataclass


@dataclass(frozen=False)
class TermNode:
    """
    A mutable link node containing a coefficient, exponent, and
    reference to next node
    """
    coefficient: int
    exponent: int
    next: Union["TermNode", None]


@dataclass(frozen=False)
class LinkedList:
    """
    For mutable linked lists, we 'encapsulate' the list nodes in a wrapper
    class. This will allow functions that work with mutable lists to not
    worry about whether the list is empty or not. An empty list is still an
    instance of this LinkedList class; it's just that its head is None.
    The size of the list is stored here, too, as an example of the tradeoff
    between computing something every time you need it and using extra
    memory to store the value so that it does not have to be recomputed.
    """
    head: Union["TermNode", None] = None
    size: int = 0


def make_empty_list():
    """
    Make an empty list
    :return: a LinkedList object with next = None
    """
    return LinkedList(None, 0)


def insert_poly(lst, coefficient, exponent):
    """
    Creates a term node with parameter data. Inserts the node in the linked
    list according to its degree.
    :param lst: linked list structure
    :param coefficient: int
    :param exponent: int
    """

    # If list is empty, add to head
    if lst.head is None:
        lst.head = TermNode(coefficient, exponent, None)
        lst.size += 1
        return

    # If new item has the highest degree
    if exponent > lst.head.exponent:
        lst.head = TermNode(coefficient, exponent, lst.head)
        lst.size += 1
        return

    # Loop list for degrees lesser
    term = lst.head
    while term is not None:

        # Exponent Values
        above_e = term.exponent
        try:
            below_e = term.next.exponent
        except AttributeError:
            below_e = None

        # Appending Terms
        if below_e is None:
            term.next = TermNode(coefficient, exponent, None)
            lst.size += 1
            break
        elif above_e > exponent > below_e:
            term.next = TermNode(coefficient, exponent, term.next)
            lst.size += 1
            break
        else:
            term = term.next


def print_poly(lst):
    """
    Pretty-prints the polynomial represented in a linked list
    :param lst: linked list structure
    :return: None
    """

    # Variable
    term = lst.head

    # First entry
    if term is None:
        return
    else:
        print(f"{term.coefficient}x^{term.exponent}", end="")
        term = term.next

    # For the rest of the polynomial
    while term is not None:
        if term.coefficient < 0:
            print(" - ", end="")
        else:
            print(" + ", end="")

        print(f"{abs(term.coefficient)}*x^{term.exponent}", end="")
        term = term.next

    # Finish with print line
    print()


def add_poly(poly1, poly2):
    """
    Creates a linked list that contains the sum of two polynomials
    :param poly1: linked list structure
    :param poly2: linked list structure
    :return: linked list structure
    """
    term_1 = poly1.head
    term_2 = poly2.head
    poly3 = make_empty_list()

    while True:

        # If both polynomials are empty
        if term_1 is None and term_2 is None:
            break

        # Tests for specific cases
        if term_1.exponent > term_2.exponent:
            insert_poly(poly3, term_1.coefficient, term_1.exponent)
            term_1 = term_1.next
        elif term_1.exponent < term_2.exponent:
            insert_poly(poly3, term_2.coefficient, term_2.exponent)
            term_2 = term_2.next
        else:  # When both are the same degree
            coefficient = term_1.coefficient + term_2.coefficient
            if coefficient != 0:
                insert_poly(poly3, coefficient, term_2.exponent)
            term_1 = term_1.next
            term_2 = term_2.next

    # Return final polynomial
    return poly3


def poly_load(filename):
    """
    Creates a linked list to store data from a file containing
    a coefficient and exponent on each line corresponding
    to a term. insert_poly() is called to create a term node
    and to insert it on the list.
    :param filename: string
    :return: linked list structure
    """

    # Linked list
    polynomial = make_empty_list()

    # Loop through lines in file and add to linked list
    with open(filename, "r") as file:
        for line in file:

            # Get data
            split_line = line.strip().split()
            if len(split_line) == 0:
                continue
            else:
                coefficient = int(split_line[0])
                exponent = int(split_line[1])

                # Add to top of brick
                insert_poly(polynomial, coefficient, exponent)

    # Return final polynomial
    return polynomial


def main():
    """
    Main function implements four tasks.
    1)  Prompts for two file names
    2)  Creates two polynomial linked lists from files
    3)  Pretty-prints the polynomials
    4)  Adds the polynomials 
    5)  Pretty-prints the result polynomial
    :return: None
    """

    file1 = input('Enter name of first file: ')
    file2 = input('Enter name of second file: ')

    poly1 = poly_load(file1)
    poly2 = poly_load(file2)

    print(poly1)
    print(poly2)

    print("Polynomial in", file1, ":")
    print_poly(poly1)
    print("Polynomial in", file2, ":")
    print_poly(poly2)

    poly3 = add_poly(poly1, poly2)

    print("Sum polynomial:")
    print_poly(poly3)


if __name__ == "__main__":
    main()
