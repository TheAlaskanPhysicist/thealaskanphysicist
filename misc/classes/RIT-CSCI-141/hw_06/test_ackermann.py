"""
CSCI-141: Testing & Debugging
Homework 3
Author: RIT CS

Test module for the ack() function in the ackermann module
"""

import ackermann


def test_ack(name, m, n, expected):
    """
    A single test of the ack() function.
    :param name: a string with the function and arguments being tested
    :param m: first ack() parameter
    :param n: second ack() parameter
    :param expected: the expected result
    """
    result = ackermann.ack(m, n)
    if result == expected:
        print(name, 'passed')
    else:
        print(name, 'failed; expected', expected, 'but got', result)


def run_tests():
    """
    Test cases for ack()
    """
    test_ack('ack(0, 0)', 0, 0, 1)
    test_ack('ack(0, 1)', 0, 1, 2)
    test_ack('ack(1, 0)', 1, 0, 2)
    test_ack('ack(1, 1)', 1, 1, 3)
    test_ack('ack(1, 2)', 1, 2, 4)
    test_ack('ack(1, 3)', 1, 3, 5)
    test_ack('ack(2, 1)', 2, 1, 5)
    test_ack('ack(2, 2)', 2, 2, 7)
    test_ack('ack(2, 3)', 2, 3, 9)
    test_ack('ack(3, 1)', 3, 1, 13)
    test_ack('ack(3, 2)', 3, 2, 29)
    test_ack('ack(3, 3)', 3, 3, 61)
    test_ack('ack(4, 0)', 4, 0, 13)
    test_ack('ack(3, 4)', 3, 4, 125)


if __name__ == '__main__':
    run_tests()
