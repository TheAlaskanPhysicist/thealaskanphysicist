"""
CSCI-141 Optimal Sorting Homework
Merge Quick Sort

A test unit for merge_quick_sort.
"""

import merge_quick_sort
import random


def test_merge_quick_sort(msg, lst, expected):
    """
    Run a single test of the merge_quick_sort function.
    :param msg a message to be printed with the test results
    :param lst the list of data to be sorted
    :param expected the expected result (a sorted list)
    """
    result = merge_quick_sort.merge_quick_sort(lst)
    if result == expected:
        print(msg, 'passed')
    else:
        print(msg, 'failed; expected', expected, 'but got', result)


def run_tests():
    """
    The test cases for the merge_quick_sort_function are here.
    """
    test_merge_quick_sort('empty list', [], [])
    test_merge_quick_sort('single element list', [0], [0])
    test_merge_quick_sort('two element list sorted', [0, 1], [0, 1])
    test_merge_quick_sort('two element list unsorted', [1, 0], [0, 1])

    # larger tests
    for num in (10, 100, 1000, 10000):
        # build the list of numbers
        lst = []
        for i in range(num):
            lst.append(i)

        # shuffle the numbers
        random.shuffle(lst)

        # copy the list and sort it for the expected result
        expected = lst[:]
        expected.sort()

        # test it
        test_merge_quick_sort('random ' + str(num) + ' element list', lst, expected)


if __name__ == '__main__':
    run_tests()
