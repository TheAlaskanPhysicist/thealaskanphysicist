# If the value converges to 1, all previous values converge to 1
MAX_NUMBER = 10_000_000
MAX_DEPTH  = 100


ALL_TRUES = {1: True}


def collatz(n: int, depth: int) -> None:
    _true_list = []
    while depth > 0:
        # Adds numbers to true list
        _true_list.append(n)

        # If number in known trues
        try:
            if ALL_TRUES[n]:
                break
        except KeyError:
            pass
        
        # Change number
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    
    try:
        ALL_TRUES[n]
    except KeyError:
        print(n)
        return False
    
    # When satisfied
    for i in _true_list:
        ALL_TRUES[i] = True



for i in range(1, MAX_NUMBER + 1):
    collatz(i, MAX_DEPTH)