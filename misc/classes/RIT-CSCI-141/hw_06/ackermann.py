def ack(m: int, n: int) -> int:
    '''
    :param m: non-negative integer
    :param n: non-negative integer
    :return: Ackmann-resulting integer
    '''

    # Given m, n >= 0, shortcuts can be taken
    if m == 0:
        return n + 1

    else:
        if n == 0:
            return ack(m - 1, 1)
        else:
            return ack(m - 1, ack(m, n - 1))


def main() -> None:

    # User console input
    _user_m = int(input("m: "))
    _user_n = int(input("n: "))

    # Ackmann function
    _ackmann_result = ack(_user_m, _user_n)
    print(f"ack({_user_m}, {_user_n}) = {_ackmann_result}")

if __name__ == "__main__":
    main()