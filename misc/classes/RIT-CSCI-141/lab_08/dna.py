"""
File: dna.py
Author: Stanley Goodwin
Last Updated: 4/13/2022

Description:
    This file contains all the functions in order to do operations on DNA,
    these functions are provided as to read from a string, determine matching
    DNA sequences, insert DNA into other DNA, and many other things.
"""
from immutable_list import FrozenNode


def convert_to_nodes(dna_strand: str) -> FrozenNode or None:
    """
    Convert a string of GCAT DNA into a linked list.

    :param dna_strand: A string of characters corresponding to DNA bases.
    :return FrozenNode or None: The node that the next part goes to.
    """
    if dna_strand == "":
        return None
    else:
        next_node = convert_to_nodes(dna_strand[1:])
        return FrozenNode(dna_strand[0], next_node)


def convert_to_string(dna_seq) -> str:
    """
    Takes in a DNA sequence and returns a string of it.

    :param dna_seq: The DNA sequence (FrozenNode).
    :return string: The DNA sequence string.
    """
    if dna_seq is None:
        return ""
    else:
        return dna_seq.value + convert_to_string(dna_seq.next)


def length_rec(dna_seq) -> int:
    """
    Takes a DNA sequence and finds its length.

    :param dna_seq: The DNA sequence (FrozenNode).
    :return length: The length of the sequence.
    """
    if dna_seq is None:
        return 0
    else:
        return 1 + length_rec(dna_seq.next)


def is_match(dna_seq1: FrozenNode, dna_seq2: FrozenNode) -> bool:
    """
    Determines if 2 DNA sequences are similar.

    :param dna_seq1: A first linked sequence with data nodes representing a DNA sequence.
    :param dna_seq2: A second linked sequence with data nodes representing a DNA sequence.
    :return boolean: True or False.
    """
    if dna_seq1 is None and dna_seq2 is None:  # If both end, must be same.
        return True
    elif dna_seq1 is None or dna_seq2 is None:  # If one ends early, must be different
        return False
    else:  # If both still are not empty
        if dna_seq1.value == dna_seq2.value:  # If same value at place
            return is_match(dna_seq1.next, dna_seq2.next)
        else:  # Not same value at place
            return False


def is_pairing(dna_seq1: FrozenNode, dna_seq2: FrozenNode) -> bool:
    """
    Determines if 2 DNA sequences are conjugate pairs.

    :param dna_seq1: A first linked sequence with data nodes representing a DNA sequence.
    :param dna_seq2: A second linked sequence with data nodes representing a DNA sequence.
    :return boolean: True or False.
    """
    if dna_seq1 is None and dna_seq2 is None:  # If both end, must be same.
        return True
    elif dna_seq1 is None or dna_seq2 is None:  # If one ends early, must be different
        return False
    else:  # If both still are not empty
        val_set = {dna_seq1.value, dna_seq2.value}
        if val_set == {"C", "G"} or val_set == {"A", "T"}:  # If conjugates at place
            return is_pairing(dna_seq1.next, dna_seq2.next)
        else:  # Not conjugates at place
            return False


def substitution(dna_seq1: FrozenNode, idx: int, base: str):
    """
    Replaces a base value at a particular index.

    :param dna_seq1: The sequence that will mutate.
    :param idx: The index where the letter occurs.
    :param base: The DNA letter that will be placed.
    :return dna_sequence: A new DNA sequence with the change.
    """
    dna_1 = convert_to_string(dna_seq1)
    if idx <= len(dna_1) - 1:
        dna_1 = dna_1[:idx] + base + dna_1[idx + 1:]
        return convert_to_nodes(dna_1)
    else:
        raise IndexError("List is shorter than index " + str(idx) + "!")


def insertion(dna_seq1: FrozenNode, dna_seq2: FrozenNode, idx: int) -> FrozenNode:
    """
    Inserts DNA sequence 2 into an index in DNA sequence.

    :param dna_seq1: The first sequence into which the second sequence is inserted.
    :param dna_seq2: The second sequence, which is inserted into the first.
    :param idx: The index before which the insertion occurs.
    :return FrozenNode:
    """
    dna_1 = convert_to_string(dna_seq1)
    dna_2 = convert_to_string(dna_seq2)
    if idx > len(dna_1):
        raise IndexError("List is shorter than index " + str(idx) + "!")
    elif idx == 0:
        return convert_to_nodes(dna_2 + dna_1)
    else:
        combined = dna_1[0:idx] + dna_2 + dna_1[idx:]
        return convert_to_nodes(combined)


def deletion(dna_seq, idx, segment_size):
    """
    Deletes a range of values in a DNA sequence.

    :param dna_seq: The sequence to be indirectly modified.
    :param idx: The index that the removal starts.
    :param segment_size: The amount of letter to remove.
    :return dna_seq2: A new sequence that contains the changes.
    """
    dna = convert_to_string(dna_seq)
    if segment_size == 0:
        return convert_to_nodes(dna)  # Purposely to copy the sequence instead of returning original
    if idx + segment_size > len(dna):
        raise IndexError("List is shorter than index " + str(idx) + "!")
    else:
        new_dna = dna[:idx] + dna[idx + segment_size:]
        return convert_to_nodes(new_dna)


def duplication(dna_seq, idx, segment_size):
    """
    Copies a region of the DNA sequence and returns a copy.

    :param dna_seq: The sequence to be copied from.
    :param idx: The index that the copy starts.
    :param segment_size: The amount of letter to copy.
    :return dna_seq2: A new sequence that contains the changes.
    """
    dna = convert_to_string(dna_seq)
    if segment_size == 0:
        return convert_to_nodes(dna)  # Purposely to copy the sequence instead of returning original
    elif idx + segment_size > len(dna):
        raise IndexError("List is shorter than index " + str(idx) + "!")
    else:
        new_dna = dna[:idx] + dna[idx:idx + segment_size] + dna[idx:]
        return convert_to_nodes(new_dna)
