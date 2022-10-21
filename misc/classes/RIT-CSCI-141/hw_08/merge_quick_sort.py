"""
File: merge_quick_sort.py
Author: Stanley Goodwin
Date: 3/4/2022

Description:
    Contains a function that utilizes both quicksort
    and mergesort in making a faster algorithm for
    sorting data effectively.

"""
import merge_sort
import quick_sort


def merge_quick_sort(sort_list: list):
    """
    Takes advantage of the pros of both algorithms to sort
    a given list of data.

    :param sort_list: The list to be sorted.

    :return sorted_list: The list after being sorted.
    """

    # Base case
    if len(sort_list) < 2:
        return sort_list
    
    # (a) Split the given list into equal halves.
    _h1, _h2 = merge_sort.split(sort_list)
    if _h1 == [] or _h2 == []:
        return []

    # (b) Partition each half into three sublists.
    _h1_lower, _h1_same, _h1_higher = quick_sort.partition(_h1[0], _h1)
    _h2_lower, _h2_same, _h2_higher = quick_sort.partition(_h2[0], _h2)

    # (c.1) Sort each of the sublists...
    _h1_lower = merge_quick_sort(_h1_lower)
    _h1_higher = merge_quick_sort(_h1_higher)
    _h2_lower = merge_quick_sort(_h2_lower)
    _h2_higher = merge_quick_sort(_h2_higher)

    # (c.2) and concatenate them.
    _h1 = _h1_lower + _h1_same + _h1_higher
    _h2 = _h2_lower + _h2_same + _h2_higher

    # (d) Merge the two sorted halves.
    sorted_list = merge_sort.merge(_h1, _h2)

    # Return sorted list
    return sorted_list
