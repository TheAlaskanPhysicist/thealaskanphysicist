def gcd(m: int, n: int) -> int:
    _temp = m % n
    if _temp == 0:
        return n
    else:
        return gcd(n, _temp)