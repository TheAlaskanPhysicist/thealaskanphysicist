


def f(x: float) -> float:
    return 5 * x ** 3 + 6 * x ** 2

def F(x: float) -> float:
    return (5 / 4) * x ** 4 + 2 * x ** 3




def left(a: float, b: float, n: int) -> float:
    dx = (b - a) / n
    x = 0
    y = 0
    for i in range(0, n - 1):
        y += f(x) * dx
        x += dx
    return y


def right(a: float, b: float, n: int) -> float:
    dx = (b - a) / n
    x = dx
    y = 0
    for i in range(0, n - 1):
        y += f(x) * dx
        x += dx
    return y


def middle(a: float, b: float, n: int) -> float:
    dx = (b - a) / n
    x = dx / 2
    y = 0
    for i in range(0, n - 1):
        y += f(x) * dx
        x += dx
    return y

def exact(a: float, b: float, n: int) -> float:
    return F(b) - F(a)


def main():
    a = int(input("Left bound: "))
    b = int(input("Right bound: "))
    n = int(input("Number of boxes: "))

    print(f"Left-hand sum: {left(a, b, n)} (Error: {(left(a, b, n) - exact(a, b, n)) / exact(a, b, n)})")
    print(f"Right-hand sum: {right(a, b, n)} (Error: {(right(a, b, n) - exact(a, b, n)) / exact(a, b, n)})")
    print(f"Centerpoint sum {middle(a, b, n)} (Error: {(middle(a, b, n) - exact(a, b, n)) / exact(a, b, n)})")
    print(f"Exact integral: {exact(a, b, n)} ")




if __name__ == "__main__":
    main()