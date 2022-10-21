"""
CSCI-141 Computer Science 1 Recitation Exercise
05-Strings and Files
Reversing Encryption

Here is a skeleton for code that can decrypt the file
your friend sent you. You have to write code inside the
function bodies to solve the problem.
Do NOT add functions or modify the function definitions!
Start with how you would decrypt a single letter. Then,
implement the logic for reading the file and decrypting
the contents
"""

def decrypt_letter(letter):
    """
    Decrypt an individual letter and return it
    :param: the letter to be rotated forward
    """
    return ord(letter)

def read_file(file_path):
    """
    Read the file and decrypt every word,
    printing each word as it is decrypted
    :param: the path to the file containing encrypted message
    """
    with open(file_path) as f:
        for line in f:
            _text = ""
            for i in line:
                _text += decrypt_letter(i)
            print(_text)



def test_decryption():
    """
    Use this function to check your implementation
    of decrypt_letter()
    :return: True if the tests pass, False otherwise
    """
    if decrypt_letter('B') != 'E':
        print("Your result for decrypting B was ", decrypt_letter('B'))
        return False
    if decrypt_letter('Z') != 'C':
        print("Your result for decrypting Z was ", decrypt_letter('Z'))
        return False
    print('All tests passed!')
    return True

def main():
    test_decryption() 
    read_file("encrypted.txt")

if __name__ == '__main__':
    main()
