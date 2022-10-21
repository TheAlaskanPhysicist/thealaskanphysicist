"""
CSCI-141 Computer Science 1 Recitation Exercise
03-Recursion
Hanoi

Towers of Hanoi is a famous puzzle you can read about here:

https://en.wikipedia.org/wiki/Tower_of_Hanoi

The hanoi routine is a way to recursively compute the minimum number of disks
moves it would take to move all the disks from one peg to another, following
the movement rules.

The program is complete and you will simply be using it to verify your
substitution trace is correct.
"""

def hanoi(disks):
    """
    Return the minimum number of moves it takes to move the disks.
    :param disks: number of disks
    :return: the number of moves it takes for this number of disks
    """
    return 2 ** disks - 1


def main():
    """
    The main program prompts for the number of disks and then displays the
    result by using the recursive hanoi function.
    """
    disks = int(input('Number of disks: '))
    print(disks, 'disks takes', hanoi(disks), 'moves')

if __name__ == '__main__':
    main()