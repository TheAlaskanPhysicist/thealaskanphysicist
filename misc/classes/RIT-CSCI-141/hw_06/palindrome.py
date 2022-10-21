"""
CSCI-141: Testing & Debugging
Homework 3
Author: RIT CS

A palindrome checker that has a logic error.
"""

def is_palindrome(word):
    """
    A boolean function that recursively tests whether a word is a palindrome
    or not.
    :param word: the word
    :return: whether it is a palindrome or not
    """
    if len(word) < 2:  # Debug: If it is now a single or no character, it will return True.
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])

def main():
    """
    The main prompts for a word and checks whether it is a palindrome or not.
    """
    word = input('Enter word: ')
    if is_palindrome(word):
        print(word, 'is a palindrome')
    else:
        print(word, 'is NOT a palindrome')

if __name__ == '__main__':
    main()