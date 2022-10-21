""" 
file: immutable_list.py - lab version
description: functions for manipulating immutable linked lists
author: RIT CS
"""

from node_types import FrozenNode


def to_str( head ):
    """
    to_str: FrozenNode -> str
    Convert a sequence of nodes to a string of the nodes' values
    surrounded by brackets and the individual values separated by commas.
    It is a recursive solution.
    :param head: The first node in the list to be converted
    :return: The entire sequence as a legible string, pattern "[a,b,c]"
    """
    result = "["
    result += _to_str_rec( head )
    result += " ]"
    return result


def _to_str_rec( head ):
    """
    to_str_rec: FrozenNode -> str
    Compute a string version of the linked sequence.
    :param head: The first node in the list to be converted
    :return: The entire sequence as a legible string, pattern "a,b,c"
    """
    if head is None:
        result = ""
    else:
        result = ' ' + str( head.value )
        if head.next is not None:
            result += ','
        result += _to_str_rec( head.next )
    return result


def append( head, new_value ):
    """
    append: FrozenNode, Any -> FrozenNode
    Effectively place a new value at the end of a list.
    :param head: the head of the original list
    :param new_value: the value with which to append the list
    :return: a new list containing all of head's values, plus new_value
    """
    if head is None:
        return FrozenNode( new_value, None )
    else:
        return FrozenNode( head.value, append( head.next, new_value ) )


def insert_before_index( head, new_value, index ):
    """
    insert_before_index: FrozenNode, Any, int -> FrozenNode
    Effectively stick a new value in front of the node at a certain ordinal
    position in a list.
    Note that this implementation creates a list that shares any nodes beyond
    the insertion point. That is not a problem because the nodes are immutable.
    :param head: the head of the given list
    :param new_value: the new value to be inserted
    :param index: how far down, starting at head being index 0, to insert
                  the new value. Everything at the given index and later
                  is effectively shifted further down,
    :return: the head of the new list containing all the old values plus
             new_value in the proper place.
    :pre: index >= 0
    :except: IndexError if index is beyond the size of the list
    """
    if index == 0:
        # Note: this case has two perspectives:
        # (1) We are past the end of the list; (2) We are given an empty list.
        return FrozenNode( new_value, head )
    elif head is None: # index > 0
        raise IndexError( "List is shorter than index " + str( index ) + "!" )
    else:
        return FrozenNode(
            head.value,
            insert_before_index( head.next, new_value, index - 1 )
        )


def remove_value( head, value ):
    """
    FrozenNode, Any -> FrozenNode
    Locate a value in a list and effectively remove it.
    Note that this implementation creates a list that shares any nodes beyond
    the insertion point. That is not a problem because the nodes are immutable.
    :param head: the head of the given list
    :param value: the value to search for, starting at head
    :return: the head of the new list containing all the old values minus the
             first node that contained the specified value
    :except: ValueError if the value is not present in the sequence
    """
    if head is None:
        raise ValueError( "No such value " + str( value ) + " in list!" )
    elif head.value == value:
        return head.next
    else:
        return FrozenNode( head.value, remove_value( head.next, value ) )


def to_str_acc( head ):
    """
    to_str_acc: FrozenNode -> str
    Compute a string version of the linked sequence using the
    accumulator pattern.
    :param head: The first node in the list to be converted
    :return: The entire sequence as a legible string, pattern "[a,b,c]"
    """
    return "[" + to_str_acc_rec( head, "" ) + " ]"


def to_str_acc_rec( head, acc ):
    """
    to_str_acc_rec: FrozenNode, str -> str
    """
    if head is None:
        return acc
    else:
        suffix = ' ' + str( head.value )
        if head.next is not None:
            suffix += ","
        return to_str_acc_rec(head.next, acc + suffix)


def remove_at(index, head):
    """ remove_at: NatNum * Linked(T) -> Linked(T)
    Compute removal of value at index from lnk.
    """
    if head is None:
        raise IndexError("index out of bounds in remove_at")
    elif index == 0:
        return head.next
    else:
        return FrozenNode(head.value, remove_at(index-1, head .next))


def concatenate(head1, head2):
    """ concatenate: Linked(T) * Linked(T) -> Linked(T)
    Compute concatenation of head1 and head2.
    """
    if head1 is None:
        return head2
    else:
        return FrozenNode(head1.value, concatenate(head1.next, head2))

# ---------------------------  Test Code -------------------------------------

def test_to_str():
    """
    Make sure both to_str variations return the same result.
    """
    for seq in \
            None, \
            FrozenNode( 10, None ), \
            FrozenNode( "hello", FrozenNode( "world", None ) ), \
            FrozenNode( 10, FrozenNode( 20, FrozenNode( 30, None ) ) ):
        v1 = to_str( seq )
        print( v1, end=" " )
        if v1 == to_str_acc( seq ):
            print( "PASS" )
        else:
            print( "FAIL" )


def test():
    print( "Create list [5,10,15]." )
    lst = FrozenNode( 5, FrozenNode( 10, FrozenNode( 15, None ) ) )
    print( to_str( lst ) )

    print( "Insert 1's everywhere in the list by index." )
    lst = insert_before_index( lst, 1, 3 )
    for i in range( 2, -1, -1 ):
        lst = insert_before_index( lst, 1, i )
        print( to_str( lst ) )

    print( "Append [70,90] to the end of the list." )
    lst = append( lst, 70 )
    print( to_str( lst ) )
    lst = append( lst, 90 )
    print( to_str( lst ) )

    print( "Remove the first 1 by value." )
    lst = remove_value( lst, 1 )
    print( to_str( lst ) )

    print( "Remove 15 by value." )
    lst = remove_value( lst, 15 )
    print( to_str( lst ) )

    print( "Empty the rest of the list!" )
    while lst is not None:
        lst = remove_value( lst, lst.value )
    print( to_str( lst ) )


if __name__ == '__main__':
    test_to_str()
    test()
