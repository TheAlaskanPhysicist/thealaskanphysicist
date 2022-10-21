"""
file: quick_sort.py
version: python3
author: Arthur Nunes-Harwitt, Ivona Bezakova
purpose: Implementation of the quick-sort algorithm ( not in-place )
"""
def quick_sort( L ):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        ( less, same, more ) = partition( pivot, L )
        return quick_sort( less ) + same + quick_sort( more )

def partition( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    ( less, same, more ) = ( [], [], [] )
    for e in L:
        if e < pivot:
            less.append( e )
        elif e > pivot:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )

if __name__ == "__main__":
    print( quick_sort( [1, 5, 3, 4, 2, 2, 7, 5, 3, 4, 9, 0, 1, 2, 5, 4, 76, 6] ) )

