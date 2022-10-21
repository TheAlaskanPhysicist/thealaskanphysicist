import tools
import time


def quick_select(lst, k):
    """
    Finds the k'th smallest value in an unsorted list lst.

    :param lst: The input unsorted list.
    :param k: The index + 1 of the smallest number.
    :return number: The k'th smallest number.
    """
    if len(lst) != 0:
        pivot = lst[len(lst) // 2]
        small_list = []
        large_list = []
        count = 0
        for i in lst:
            if i < pivot:
                small_list.append(i)
            elif i > pivot:
                large_list.append(i)
            else:
                count += 1

        m = len(small_list)
        if m <= k < m + count:  # Pycharm simplification
            return pivot
        if m > k:
            return quick_select(small_list, k)
        else:
            return quick_select(large_list, k - m - count)


def optimal_location(_pos_list):
    """
    Uses quicksort to find the median value of a given list.

    :param _pos_list: The list of building positions.
    :return median: The median value of building positions.
    """

    # Find the median value and return it
    _list_length = len(_pos_list)
    if _list_length % 2:  # Odd length case
        return quick_select(_pos_list, _list_length // 2)
    else:                        # Even length case
        _index = _list_length // 2
        _m1 = quick_select(_pos_list, _list_length // 2 - 1)
        _m2 = quick_select(_pos_list, _list_length // 2)
        return (_m1 + _m2) / 2


# Main function
def main() -> None:

    # Takes file name input from user
    _file_name = input("Enter data file: ")

    # Reads the data file
    _pos_list = tools.read_file(_file_name)

    # Times the runtime of this execution
    new = time.perf_counter()
    _optimal_loc = optimal_location(_pos_list)
    _total_distances = tools.sum_distances(_pos_list, _optimal_loc)
    end = time.perf_counter() - new

    # Prints results
    print(f"Optimum new store location:         {_optimal_loc}")
    print(f"Sum of distances to the new store:  {_total_distances}")
    print(f"\nelapsed time: {end}")


# Main guard
if __name__ == "__main__":
    main()
