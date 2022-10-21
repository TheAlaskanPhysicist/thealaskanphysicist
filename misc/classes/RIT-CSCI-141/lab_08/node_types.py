""" 
file: node_types.py
description: type definitions for nodes that make linked sequences
author: RIT CS
"""

from typing import Any, Union
from dataclasses import dataclass

@dataclass( frozen=True )
class FrozenNode:
    """
    An immutable link node containing a value and a link to the next node
    """
    value: Any
    next: Union[ "FrozenNode" , None ]

@dataclass( frozen=False )
class MutableNode:
    """
    A mutable link node containing a value and a link to the next node
    """
    value: Any
    next: Union[ "MutableNode" , None ]

# ---------------------- Very Basic Test Code --------------------------------

# A list printer is defined here. It is redundant with the to-string
# functions found in immutable_list.py and mutable_list.py.
# But since we need something for basic testing and we don't want to
# introduce circular dependencies between modules, we put this
# quick-and-dirty function here.

def print_seq( a_list ):
    print( '[', end ="" )
    node = a_list
    while node is not None:
        print( " " + str( node.value ), end="" )
        node = node.next
    print( " ]" )

def test() -> None:
    """
    Let's make some node structures.
    """
    our_list = FrozenNode( 1, FrozenNode( 2, FrozenNode( 3, None ) ) )
    print_seq( our_list )
    print( "Above line should be [ 1 2 3 ]." )

    print_seq( our_list.next )
    print( "Above line should be [ 2 3 ]." )

    our_list = None
    print_seq( our_list )
    print( "Above line should be [ ]." )

    our_list = MutableNode( 1, MutableNode( 2, MutableNode( 3, None ) ) )
    print_seq( our_list )
    print( "Above line should be [ 1 2 3 ]." )

    our_list.next = our_list.next.next
    print_seq( our_list)
    print( "Above line should be [ 1 3 ]." )

if __name__ == '__main__':
    test()
