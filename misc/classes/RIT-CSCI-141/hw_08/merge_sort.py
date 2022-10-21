"""
file: merge_sort.py
language: python3
author: Arthur Nunes-Harwitt
purpose: Implementation of merge sort algorithm
"""


def merge_sort(L):
    """
    mergeSort: List( A ) -> List( A )
       where A is totally ordered
    """
    if L == []:
        return []
    elif len(L) == 1:
        return L
    else:
        ( half1, half2 ) = split(L)
        return merge(merge_sort(half1), merge_sort(half2))


def split(L):
    """
    split: List( A ) -> Tuple( List( A ), List( A ) )
    """
    evens = []
    odds = []
    is_even_index = True
    for e in L:
        if is_even_index:
            evens.append(e)
        else:
            odds.append(e)
        is_even_index = not is_even_index
    return ( evens, odds )


def merge(sorted1, sorted2):
    """
    merge: List( A ) * List( A ) -> List( A )
    precondition: sorted1 and sorted2 are lists whose elements are in order
    """
    result = []
    index1 = 0
    index2 = 0
    while index1 < len(sorted1) and index2 < len(sorted2):
        if sorted1[index1] <= sorted2[index2]:
            result.append(sorted1[index1])
            index1 = index1 + 1
        else:
            result.append(sorted2[index2])
            index2 = index2 + 1
    if index1 < len(sorted1):
        result.extend(sorted1[index1:])
    elif index2 < len(sorted2):
        result.extend(sorted2[index2:])
    return result


if __name__ == "__main__":
    print(merge_sort([1, 5, 3, 4, 2, 2, 7, 5, 3, 4, 9, 0, 1, 2, 5, 4, 76, 6]))
