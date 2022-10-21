"""
Program to test DNA linked Node functionality.
Date: March 2022
Author:  CS @ RIT
File: dna_tester.py
"""

import dna
import immutable_list  # in case student's dna module didn't import
from node_types import FrozenNode


def test1():
    """
    Tests function to convert a string
    into a DNA linked Node structure.
    :return: None
    """
    print("Test1: testing convert_to_nodes")

    dna_seq1 = dna.convert_to_nodes("")
    print(dna_seq1 is None, end=" ")

    dna_seq2 = dna.convert_to_nodes("A")
    print(dna_seq2.value == "A" and dna_seq2.next is None, end=" ")

    dna_seq3 = dna.convert_to_nodes("GTC")
    print(dna_seq3.value == 'G' and dna_seq3.next.value == 'T'
          and dna_seq3.next.next.value == 'C' and
          dna_seq3.next.next.next is None)


def test2():
    """
    Tests function to convert a DNA linked Node
    structure into a string.
    :return:
    """

    print("Test2: testing convert_to_string")

    dna_str1 = dna.convert_to_string(None)
    print(dna_str1 == "", end=" ")

    dna_seq = None
    dna_seq = immutable_list.insert_before_index(dna_seq, "C", 0)
    dna_str2 = dna.convert_to_string(dna_seq)
    print(dna_str2 == "C", end=" ")

    dna_seq = None
    dna_seq = immutable_list.insert_before_index(dna_seq, 'T', 0)
    dna_seq = immutable_list.insert_before_index(dna_seq, 'A', 1)
    dna_seq = immutable_list.insert_before_index(dna_seq, 'G', 2)
    dna_str3 = dna.convert_to_string(dna_seq)
    print(dna_str3 == "TAG")


def test3():
    """
    Tests function to convert a DNA linked Node
    structure into a string.
    :return:
    """

    print("Test3: testing length_rec")

    dna_len1 = dna.length_rec(None)
    print(dna_len1 == 0, end=" ")

    dna_seq = None
    dna_seq = immutable_list.insert_before_index(dna_seq, "C", 0)
    dna_len2= dna.length_rec(dna_seq)
    print(dna_len2 == 1, end=" ")

    dna_seq = None
    dna_seq = immutable_list.insert_before_index(dna_seq, 'T', 0)
    dna_seq = immutable_list.insert_before_index(dna_seq, 'A', 1)
    dna_seq = immutable_list.insert_before_index(dna_seq, 'G', 2)
    dna_len3 = dna.length_rec(dna_seq)
    print(dna_len3 == 3)


def test4():
    """
    Tests is_match function.
    :return: None
    """
    
    print("Test4: testing is_match")
    
    dna_seq1 = None
    dna_seq2 = None
    
    print(dna.is_match(dna_seq1, dna_seq2) == True, end=" ")
    
    dna_seq2 = immutable_list.insert_before_index(dna_seq2, "A", 0)
    print(dna.is_match(dna_seq1, dna_seq2) == False, end=" ")
    print(dna.is_match(dna_seq2, dna_seq1) == False, end=" ")

    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "A", 0)
    print(dna.is_match(dna_seq1, dna_seq2) == True, end=" ")

    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "T", 1)
    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "G", 2)
    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "C", 3)
    dna_seq2 = immutable_list.insert_before_index(dna_seq2, "T", 1)
    dna_seq2 = immutable_list.insert_before_index(dna_seq2, "G", 2)
    print(dna.is_match(dna_seq1, dna_seq2) == False, end=" ")
    dna_seq2 = immutable_list.insert_before_index(dna_seq2, "C", 3)
    print(dna.is_match(dna_seq1, dna_seq2) == True, end=" ")

    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "A", 2)
    dna_seq2 = immutable_list.insert_before_index(dna_seq2, "G", 2)
    print(dna.is_match(dna_seq1, dna_seq2) == False)


def test5():
    """
    Tests is_pairing function.
    :return: None
    """

    print("Test5: testing is_pairing")

    dna_seq1 = None
    dna_seq2 = None

    print(dna.is_pairing(dna_seq1, dna_seq2) == True, end=" ")

    dna_seq2 = immutable_list.insert_before_index(dna_seq2, "A",0 )
    print(dna.is_pairing(dna_seq1, dna_seq2) == False, end=" ")
    print(dna.is_pairing(dna_seq2, dna_seq1) == False, end=" ")

    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "T", 0)
    print(dna.is_pairing(dna_seq1, dna_seq2) == True, end=" ")

    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "T", 1)
    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "G", 2)
    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "C", 3)
    dna_seq2 = immutable_list.insert_before_index(dna_seq2, "A", 1)
    dna_seq2 = immutable_list.insert_before_index(dna_seq2, "C", 2)
    print(dna.is_pairing(dna_seq1, dna_seq2) == False, end=" ")
    dna_seq2 = immutable_list.insert_before_index(dna_seq2, "G", 3)
    print(dna.is_pairing(dna_seq1, dna_seq2) == True, end=" ")

    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "A", 2)
    dna_seq2 = immutable_list.insert_before_index(dna_seq2, "A", 2)
    print(dna.is_pairing(dna_seq1, dna_seq2) == False, end=" ")

    test_str1 = "AATTTGC"
    test_str2 = "GCGCTGC"

    for idx in range(len(test_str1)):
        dna_seq1 = immutable_list.remove_at(2, dna_seq1)
        dna_seq2 = immutable_list.remove_at(2, dna_seq2)
        dna_seq1 = immutable_list.insert_before_index(dna_seq1, test_str1[idx], 2)
        dna_seq2 = immutable_list.insert_before_index(dna_seq2, test_str2[idx], 2)
        print(dna.is_pairing(dna_seq1, dna_seq2) == False, end=" ")

    print()


def test6():
    """
    Tests substitution function.
    :return: None
    """

    print("Test6: testing substitution")

    dna_seq = None
    try:
        dna_seq = dna.substitution(dna_seq, 0, "A")
        print("False", end=" ")  # failed to catch exception
    except IndexError as e:
        print("True", end=" ")

    dna_seq = immutable_list.insert_before_index(dna_seq, "A", 0)
    dna_seq2 = dna.substitution(dna_seq, 0, "T")
    print(dna_seq2.value == "T", end=" ")

    dna_seq = immutable_list.insert_before_index(dna_seq, "T", 1)
    dna_seq2 = dna.substitution(dna_seq, 1, "G")
    print(dna_seq2.value == "A" and dna_seq2.next.value == "G", end=" ")

    dna_seq = immutable_list.insert_before_index(dna_seq, "G", 2)
    dna_seq = immutable_list.insert_before_index(dna_seq, "C", 3)
    try:
        dna_seq2 = dna.substitution(dna_seq, 4, "A")
        print("False", end=" ")  # failed to catch exception
    except IndexError as e:
        print("True", end=" ")
    dna_seq2 = dna.substitution(dna_seq, 2, "A")
    print(dna_seq2.value == "A" and dna_seq2.next.value == "T" \
          and dna_seq2.next.next.value == "A")


def test7():
    """
    Tests insertion function.
    :return: None
    """

    print("Test7: testing insertion")

    dna_seq1 = None
    dna_seq2 = None
    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 0)
    print(dna_seq3 is None, end=" ")

    try:
        dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 1)
        print("False", end=" ")  # failed to catch exception
    except IndexError as e:
        print("True", end=" ")

    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "A", 0)
    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 0)
    print(dna_seq3.value == "A" and dna.length_rec(dna_seq3) == 1, end=" ")

    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 1)
    print(dna_seq3.value == "A" and dna.length_rec(dna_seq3) == 1, end=" ")

    dna_seq2 = immutable_list.insert_before_index(dna_seq2, "C", 0)
    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 0)
    print(dna_seq3.value == "C" and dna_seq3.next.value == "A" \
          and dna.length_rec(dna_seq3) == 2, end=" ")

    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 1)
    print(dna_seq3.value == "A" and dna_seq3.next.value == "C" \
          and dna.length_rec(dna_seq3) == 2, end=" ")

    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "T", 0)  # now TA
    dna_seq2 = immutable_list.insert_before_index(dna_seq2, "G", 0)  # now GC

    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 0)
    print(dna_seq3.value == "G" and dna_seq3.next.value == "C" \
        and dna_seq3.next.next.value == "T" \
        and dna_seq3.next.next.next.value == "A"
          and dna.length_rec(dna_seq3) == 4, end=" ")

    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 1)
    print(dna_seq3.value == "T" and dna_seq3.next.value == "G" \
          and dna_seq3.next.next.value == "C" \
          and dna_seq3.next.next.next.value == "A"
          and dna.length_rec(dna_seq3) == 4, end=" ")

    dna_seq3 = dna.insertion(dna_seq1, dna_seq2, 2)
    print(dna_seq3.value == "T" and dna_seq3.next.value == "A" \
          and dna_seq3.next.next.value == "G" \
          and dna_seq3.next.next.next.value == "C"
          and dna.length_rec(dna_seq3) == 4)


def test8():
    """
    Tests deletion function.
    :return: None
    """

    print("Test8: testing deletion")

    dna_seq1 = None
    dna_seq2 = dna.deletion(dna_seq1, 0, 0)
    print(dna_seq2 is None, end=" ")

    try:
        dna_seq2 = dna.deletion(dna_seq1, 0, 1)
        print("False", end=" ")  # failed to catch exception
    except IndexError as e:
        print("True", end=" ")

    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "A", 0)
    dna_seq2 = dna.deletion(dna_seq1, 2, 0)
    print(dna_seq2.value == "A" and \
          dna.length_rec(dna_seq2) == 1, end=" ")

    dna_seq2 = dna.deletion(dna_seq1, 0, 1)
    print(dna_seq2 is None, end=" ")

    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "T", 1)
    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "G", 2)
    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "C", 3)
    dna_seq2 = dna.deletion(dna_seq1, 0, 1)
    print(dna_seq2.value == "T" and \
          dna.length_rec(dna_seq2) == 3, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 1, 1)
    print(dna_seq2.value == "A" and \
        dna_seq2.next.value == "G" and \
          dna.length_rec(dna_seq2) == 3, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 2, 1)
    print(dna_seq2.value == "A" and \
          dna_seq2.next.value == "T" and \
          dna_seq2.next.next.value == "C" and \
          dna.length_rec(dna_seq2) == 3, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 3, 1)
    print(dna_seq2.value == "A" and \
          dna_seq2.next.value == "T" and \
          dna_seq2.next.next.value == "G" and \
          dna.length_rec(dna_seq2) == 3, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 0, 2)
    print(dna_seq2.value == "G" and \
          dna_seq2.next.value == "C" and \
          dna.length_rec(dna_seq2) == 2, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 1, 2)
    print(dna_seq2.value == "A" and \
          dna_seq2.next.value == "C" and \
          dna.length_rec(dna_seq2) == 2, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 2, 2)
    print(dna_seq2.value == "A" and \
          dna_seq2.next.value == "T" and \
          dna.length_rec(dna_seq2) == 2, end=" ")

    try:
        dna_seq2 = dna.deletion(dna_seq1, 3, 2)
        print("False", end=" ")  # failed to catch exception
    except IndexError as e:
        print("True", end=" ")

    dna_seq2 = dna.deletion(dna_seq1, 0, 3)
    print(dna_seq2.value == "C" and \
          dna.length_rec(dna_seq2) == 1, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 1, 3)
    print(dna_seq2.value == "A" and \
          dna.length_rec(dna_seq2) == 1, end=" ")
    dna_seq2 = dna.deletion(dna_seq1, 0, 4)
    print(dna_seq2 is None)


def test9():
    """
    Tests duplication function.
    :return: None
    """

    print("Test9: testing duplication")

    dna_seq1 = None
    dna_seq2 = dna.duplication(dna_seq1, 0, 0)
    print(dna_seq2 is None, end=" ")

    try:
        dna_seq2 = dna.duplication(dna_seq1, 0, 1)
        print("False", end=" ")  # failed to catch exception
    except IndexError as e:
        print("True", end=" ")

    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "A", 0)
    dna_seq2 = dna.duplication(dna_seq1, 2, 0)
    print(dna_seq2.value == "A" and \
          dna.length_rec(dna_seq2) == 1, end=" ")

    dna_seq2 = dna.duplication(dna_seq1, 0, 1)
    print(dna_seq2.value == "A" and \
        dna_seq2.next.value == "A" and \
          dna.length_rec(dna_seq2) == 2, end=" ")

    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "T", 1)
    dna_seq1 = immutable_list.insert_before_index(dna_seq1, "C", 2)

    dna_seq2 = dna.duplication(dna_seq1, 0, 1)
    print(dna_seq2.value == "A" and \
          dna_seq2.next.value == "A" and \
          dna.length_rec(dna_seq2) == 4, end=" ")

    dna_seq2 = dna.duplication(dna_seq1, 1, 1)
    print(dna_seq2.value == "A" and \
          dna_seq2.next.value == "T" and \
          dna_seq2.next.next.value == "T" and \
          dna.length_rec(dna_seq2) == 4, end=" ")

    dna_seq2 = dna.duplication(dna_seq1, 2, 1)
    print(dna_seq2.value == "A" and \
          dna_seq2.next.value == "T" and \
          dna_seq2.next.next.value == "C" and \
        dna_seq2.next.next.next.value == "C" and \
          dna.length_rec(dna_seq2) == 4, end=" ")

    dna_seq2 = dna.duplication(dna_seq1, 0, 2)
    print(dna_seq2.value == "A" and \
          dna_seq2.next.value == "T" and \
          dna_seq2.next.next.value == "A" and \
          dna_seq2.next.next.next.value == "T" and \
          dna_seq2.next.next.next.next.value == "C" and \
          dna.length_rec(dna_seq2) == 5, end=" ")

    dna_seq2 = dna.duplication(dna_seq1, 1, 2)
    print(dna_seq2.value == "A" and \
          dna_seq2.next.value == "T" and \
          dna_seq2.next.next.value == "C" and \
          dna_seq2.next.next.next.value == "T" and \
          dna_seq2.next.next.next.next.value == "C" and \
          dna.length_rec(dna_seq2) == 5, end=" ")

    try:
        dna_seq2 = dna.duplication(dna_seq1, 2, 2)
        print("False", end=" ")  # failed to catch exception
    except IndexError as e:
        print("True", end=" ")

    print()


def test_all():
    """
    Large test that calls all functions.
    :return: None
    """

    print("Testing all functionality")

    dna_seq1 = dna.convert_to_nodes("ATGCCAATGC")
    dna_seq2 = dna.deletion(dna_seq1, 3, 5)
    dna_seq3 = dna.duplication(dna_seq2, 0, 3)
    dna_seq4 = dna.convert_to_nodes("CC")
    dna_seq5 = dna.insertion(dna_seq3, dna_seq4, 3)
    dna_seq6 = dna.substitution(dna_seq5, 7, "T")
    dna_seq7 = dna.substitution(dna_seq6, 6, "A")

    print(dna.is_match(dna_seq1, dna_seq7), end=" ")

    dna_seq8 = dna.insertion(dna_seq3, dna_seq4, 0)
    dna_seq9 = dna.deletion(dna_seq8, 2, 2)
    dna_seq10 = dna.substitution(dna_seq9, 6, "C")
    dna_seq11 = dna.substitution(dna_seq10, 3, "T")


    dna_seq12 = dna.convert_to_nodes("TACG")
    dna_seq13 = dna.duplication(dna_seq12, 0, 4)
    dna_seq14 = dna.duplication(dna_seq13, 3, 1)
    dna_seq15 = dna.duplication(dna_seq14, 5, 1)

    print(dna.is_pairing(dna_seq1, dna_seq15), end=" ")

    print(dna.convert_to_string(dna_seq11) == "CCGTTGCC")


def test_individual():
    """
    Calls individual test functions.
    :return: None
    """

    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()


test_individual()
test_all()
