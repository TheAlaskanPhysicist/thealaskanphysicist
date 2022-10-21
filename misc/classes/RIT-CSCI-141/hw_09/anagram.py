"""
File: anagram.py
Name: Stanley Goodwin
Date: 3/17/2022

Description:
    This file contains a lot of functions and program for anagrams in American
    English. The main function is a console program where it prompts the user
    for questions regarding anagrams and returns information about it.
"""


def alphabetize(word: str):
    """
    Takes in a word and returns a string of the letters in alphabetical order.

    :param word: The word to be alphabetized.
    :return sorted_word: The word's characters sorted alphabetically as a string.
    """

    # Split word into characters list
    char_list = []
    for i in word:
        char_list.append(i)

    # Sort the list and append word to lexigraph list
    char_list = sorted(char_list)
    sorted_word = "".join(char_list)

    # Return sorted word
    return sorted_word


def load_file():
    """
    Loads the data file and creates a dictionary from the file's content.

    :return anagram_dictionary: The dictionary of anagrams.
    """
    DIRECTORY = "american-english.txt"

    # Load file
    with open(DIRECTORY, "r", encoding="utf-8") as f:
        data = f.readlines()

    # Strip newline
    for i, word in enumerate(data):
        data[i] = word.strip()

    # Lexigraphical ordering
    lexigraph = []
    for word in data:
        sorted_word = alphabetize(word)
        lexigraph.append(sorted_word)

    # Anagram dictionary
    anagram = {}
    for word, key in zip(data, lexigraph):
        if key not in anagram:
            anagram[key] = [word]
        else:
            anagram[key].append(word)

    # Return anagram dictionary
    return anagram


def max_list_of_length(length: int):
    """
    Find the list of max anagrams given a word length.

    :param length: The length of the word.
    :return anagrams: The list of the longest anagrams list.
    """

    # Prepare anagram dictionary
    anagram = load_file()

    # Find max anagram permutations of words of length LENGTH
    current = []
    for key, words in anagram.items():
        if len(key) == length and len(words) > len(current):
            current = words

    # Return longest list of words
    return current


def jumble(length: int):
    """
    Finds the number of jumble words of a given length.

    :param length: The length of the word.
    :return jumble_quantity: The quantity of jumble words.
    """

    # Prepare anagram dictionary
    anagram = load_file()

    # Find max anagram permutations of words of length LENGTH
    jumble_quantity = 0
    for key, words in anagram.items():
        if len(key) == length and len(words) == 1:
            print(key)
            jumble_quantity += 1

    # Return the number of jumble words
    return jumble_quantity


def task2(user_input_find_anagrams):
    """
    The program specified in Task 2 of the homework PDF.

    :param user_input_find_anagrams: The input to find anagrams of.
    :return None:
    """

    # Sort word into lexigraphical order
    user_sorted = alphabetize(user_input_find_anagrams)

    # Prepare anagram dictionary
    anagram = load_file()

    # Print anagrams if key exist, otherwise say doesn't exist
    if user_sorted in anagram:
        words_list = anagram[user_sorted]
        print(f"Corresponding words: {words_list}")
    else:
        print(f"No words can be formed from: {user_input_find_anagrams}")


def task3(user_input_length):
    """
    The program specified in Task 3 of the homework PDF.

    :param user_input_length: Takes an input length for most anagrams of word.
    :return None:
    """

    # Find maximum anagrams of words with the given length
    max_list = max_list_of_length(user_input_length)

    # Print resultant statement
    print(f"Max anagrams for length {user_input_length}: {len(max_list)}")
    print(f"Anagram list: {max_list}")


def task4(user_input_length):
    """
    The program specified in Task 4 of the homework PDF.

    :param user_input_length: Takes an input length to find for jumble words.
    :return None:
    """

    # Find the number of jumble words of given length
    quantity_of_jumble_words = jumble(user_input_length)

    # Print resultant statement
    print(f"Number of jumble usable words of length {user_input_length}: {quantity_of_jumble_words}")


def main():

    # Task 2
    while True:
        user_input = input("Enter input string (hit enter key to go to task 3): ")
        if user_input == "":
            break
        else:
            task2(user_input)

    # Buffer
    print()

    # Task 3
    while True:
        user_input = input("Enter word length (hit enter key to go to task 4): ")
        if user_input == "":
            break
        else:
            task3(int(user_input))

    # Buffer
    print()

    # Task 3
    while True:
        user_input = input("Enter word length (hit enter key to quit): ")
        if user_input == "":
            break
        else:
            task4(int(user_input))

    # Return 0 after execution (without error)
    return 0


if __name__ == "__main__":
    main()
