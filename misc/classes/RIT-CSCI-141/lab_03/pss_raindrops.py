import turtle as tt
import random
import math



_POND_SIZE = 200



def turtle_init() -> None:

    # Start defs
    tt.color("light sky blue")
    tt.colormode(255)
    tt.speed(0)

    # Move to corner
    tt.pu()
    tt.back(_POND_SIZE)
    tt.right(90)
    tt.forward(_POND_SIZE)
    tt.left(90)

    # Draw square
    tt.begin_fill()
    tt.forward(2 * _POND_SIZE)
    tt.left(90)
    tt.forward(2 * _POND_SIZE)
    tt.left(90)
    tt.forward(2 * _POND_SIZE)
    tt.left(90)
    tt.forward(2 * _POND_SIZE)
    tt.left(90)
    tt.end_fill()



def draw_raindrop() -> float:
    _radius = random.randint(5, 10)
    _x = random.randint(_radius, 2 * _POND_SIZE - _radius)
    _y = random.randint(_radius, 2 * _POND_SIZE - _radius)
    _color = (
        random.randint(0, 255), 
        random.randint(0, 255), 
        random.randint(0, 255)
    )

    # Move to x, y
    tt.pu()
    tt.forward(_x)
    tt.left(90)
    tt.forward(_y)
    tt.right(90)

    # Move to center of raindrop
    tt.right(90)
    tt.forward(_radius)
    tt.left(90)

    # Draw raindrop
    tt.pd()
    tt.color(_color)
    tt.begin_fill()
    tt.circle(_radius)
    tt.end_fill()

    # Move to center of raindrop
    tt.pu()
    tt.left(90)
    tt.forward(_radius)
    tt.right(90)

    # Move to 0, 0
    tt.left(180)
    tt.forward(_x)
    tt.left(90)
    tt.forward(_y)
    tt.left(90)

    # Return circumference
    return 2 * _radius * math.pi



def recurse_draw_raindrops(n: int) -> float:
    if n == 0:
        return 0
    else:
        _circum = draw_raindrop()
        _prev = recurse_draw_raindrops(n - 1)
        return _circum + _prev



def iterative_draw_raindrops(n: int) -> float:
    _total = 0
    while n > 0:
        _total += draw_raindrop()
        n -= 1
    return _total



def main() -> None:
    turtle_init()
    _val = iterative_draw_raindrops(20)
    print(_val)
    tt.done()



if __name__ == "__main__": 
    main()