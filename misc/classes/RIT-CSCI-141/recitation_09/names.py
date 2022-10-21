"""
CSCI-141 Computer Science 1 Recitation Exercise
09- Dictionaries and Structures

Using a list of baby names from the file ny.txt, we would like to find
how many unique names there are and what the total number of occurrences
of a given name is.

The format of the file is one record per line:

state,gender,year,name,count

For example:

NY,M,2013,Teddy,5

This is the starter code for the students.  Use the TODO's to guide
you in completing this assignment.
"""

from dataclasses import dataclass

# TODO: Step 1 - Add the fields with the correct types to the Record structure.
@dataclass
class Record:
    pass

def read_file(filename):
    """
    Takes a filename as input and reads each line into a Record structure object
    and adds it to a list.
    :param filename: the file with the names
    :return: a list of Record's
    """
    names = list()
    with open(filename) as file:
        for line in file:
            # extract the fields from the next line
            fields = line.strip().split(',')
            state = fields[0]
            gender = fields[1]
            year = int(fields[2])
            name = fields[3]
            count = int(fields[4])

            # apppend a new Record to the list
            # TODO: Step 2 - create and add a new Record object to the names list

    return names

def build_dictionary(names):
    """
    Create and build a dictionary of names to total occurrences from a list of
    Record's, names.
    :param names: a list of Record's
    :return: dictionary of names to counts
    """
    counts = dict()

    # TODO: Step 3 - build and return the dictionary

    return counts

def main():
    """
    The main program.
    """

    # first read the file into a list of Record's
    names = read_file("ny.txt")

    # next, build a dictionary of names to total counts
    counts = build_dictionary(names)
    print('There are', len(counts), 'unique names!')

    # prompt for a name to search for and retrieve it from the dictionary
    find_name = input("Enter a name to search for: ")
    if find_name in counts:
        print(find_name, 'appeared', counts[find_name], 'times')
    else:
        print(find_name, 'not found!')

if __name__ == '__main__':
    main()
