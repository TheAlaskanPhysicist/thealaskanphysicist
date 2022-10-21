MAX_NUMBER = 100
MAX_DEPTH  = 20
KNOWN_TRUE = []



def collatz(n: int, depth: int):
    while True:
        if depth == 0: return 0

        if n in KNOWN_TRUE:
            return 1

        if n % 2 == 0:
            return collatz(n / 2, depth - 1)
        else:
            return collatz(3 * n + 1, depth - 1)


_iter_number = 0
for i in range(1, MAX_NUMBER + 1):
    if collatz(i, MAX_DEPTH):
        KNOWN_TRUE.append(i)
        _iter_number += 1
    else:
        print(i)
print("Finished", _iter_number)