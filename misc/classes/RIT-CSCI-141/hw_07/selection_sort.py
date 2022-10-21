"""
File: selection_sort.py
Name: Stanley Goodwin
Date: 2/21/2022
Class: Computer Science I

Description:
    A sorting algorithm that takes input of a file
    and returns the sorted list to console.

Question #1:
    When the array is almost already sorted (or is sorted),
    it runs much faster than selection sort.

Question #2:
    With only a few values to be swapped, insertion sort
    places the values exactly where they need to be in the
    order of the list, while selection sort has to scan every
    element to find the minimum number and place them at the
    beginning from scratch.

    In a precise example, if there is a 2 near the end of a list
    and the beginning looks like [1,4,7,...], insertion sort
    would place 2 in between 1 and 4 no problem, but insertion sort
    would find 2 as a minimum (after "sorting" 1) and swapping with 4,
    which then needs to be moved to where 7 is, which... ad infinitum.

    Insertion: N scannings, 1 insertion
    Selection: n sorts for all numbers less than the new number at the end.
"""

# Find minimum value's index function
def _find_min_from(input_list: list[int]) -> int:
    """
    Given a list of integers, returns the index of the
    smallest value within it.

    :param input_list: A list of integers to be searched.
    :return min_index: The minimum value's index
    """

    # Defines some local variables
    _min_val = input_list[0]
    _min_index = 0

    # Searches for minimum value (and index)
    for i in range(1, len(input_list)):
        _temp_val = input_list[i]
        if _temp_val < _min_val:
            _min_val = _temp_val
            _min_index = i
    
    # Returns the minimum index
    return _min_index

# Swap 2 values in list
def _swap(input_list: list, index_1: int, index_2: int) -> None:
    """
    Swaps the values at the indeces of the input list.
    
    :param input_list: List of anything to have swapped.
    :param index_1: The first index.
    :param index_2: The second index.
    :return None: Modifies the original list (pointer).
    """

    # Swap value at index 1 with index 2
    _temp_val = input_list[index_1]
    input_list[index_1] = input_list[index_2]
    input_list[index_2] = _temp_val

# Sort numbers in the list function
def selection_sort(input_list: list[int]) -> None:
    """
    Sorts values from input list.
    
    :param input_list: List of integers to be sorted.
    :return None: Modifies the original list (pointer).
    """

    # For all values in input list, swap until sorted
    for i in range(len(input_list)):
        
        # Finds minimum index
        _temp_min_index = i + _find_min_from(input_list[i:])

        # Swaps min with i'th index
        _swap(input_list, i, _temp_min_index)

# Read file function
def read_file(directory: str) -> list[int]:
    """
    Reads file from the given directory and returns
    list of integers corresponding to the data from
    the file.
    
    :param directory: The directory of the file.
    :return int_list: returns the list of integers 
        from the file.
    """

    # Open and read file
    with open(directory, "r") as f:
        _file_content = f.read()
    
    # Convert to list
    _string_list = _file_content.split()

    # Convert strings in list to integers
    _int_list = []
    for i in _string_list:
        _int_list.append(int(i))
    
    # Return integer list
    return _int_list

# Main run function
def main() -> None:

    # Console input of file to sort
    _file_name = input("File to be sorted: ")

    # Initial list
    _int_list = read_file(_file_name)
    print(_int_list)

    # Sorted list
    selection_sort(_int_list)
    print(_int_list)

# Main guard
if __name__ == "__main__":
    main()