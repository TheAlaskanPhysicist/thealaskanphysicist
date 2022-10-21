"""
File: compare_sorts.py
Author: Stanley Goodwin
Date: 3/4/2022

Description:
    This is the file that compares the different
    sorting algorithms with the one of my own
    creation.

"""
import merge_quick_sort
import merge_sort
import quick_sort
import sys
import random
import time


def main():
    # User input
    N = int(input("List size: "))

    # Recursion limit workaround
    if N + 10 > sys.getrecursionlimit():
        sys.setrecursionlimit(N + 10)

    # Generate randomized list
    lst = []
    for i in range(N):
        lst.append(i)

    # Run (already sorted) tests
    start = time.perf_counter()
    quick_sort.quick_sort(lst)
    elapsed = time.perf_counter() - start
    print("quick_sort (sorted) elapsed time:", elapsed * 1000, "msec")
    start = time.perf_counter()
    merge_sort.merge_sort(lst)
    elapsed = time.perf_counter() - start
    print("merge_sort (sorted) elapsed time:", elapsed * 1000, "msec")
    start = time.perf_counter()
    merge_quick_sort.merge_quick_sort(lst)
    elapsed = time.perf_counter() - start
    print("merge_quick_sort (sorted) elapsed time:", elapsed * 1000, "msec")

    # Shuffle list
    random.shuffle(lst)

    # Run (shuffled) tests
    start = time.perf_counter()
    quick_sort.quick_sort(lst)
    elapsed = time.perf_counter() - start
    print("quick_sort (random) elapsed time:", elapsed * 1000, "msec")
    start = time.perf_counter()
    merge_sort.merge_sort(lst)
    elapsed = time.perf_counter() - start
    print("merge_sort (random) elapsed time:", elapsed * 1000, "msec")
    start = time.perf_counter()
    merge_quick_sort.merge_quick_sort(lst)
    elapsed = time.perf_counter() - start
    print("merge_quick_sort (random) elapsed time:", elapsed * 1000, "msec")


# Main Guard
if __name__ == '__main__':
    main()
