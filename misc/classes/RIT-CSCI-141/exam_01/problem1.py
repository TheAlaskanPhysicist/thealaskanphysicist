"""
Author: Stanley Goodwin
Date: 2/18/2022
"""
import turtle as tt



def draw_triangle(side_length):

    # Draw 3 sides to form triangle
    tt.pd()
    for i in range(3):
        tt.forward(side_length)
        tt.left(120)
    tt.pu()
    


def recursive_draw_triangles(side_length, depth):

    draw_triangle(side_length)

    if depth == 1:
        return

    tt.back(0.5 * side_length)
    recursive_draw_triangles(side_length / 2, depth - 1)
    tt.forward(0.5 * side_length)

    tt.forward(side_length)
    recursive_draw_triangles(side_length / 2, depth - 1)
    tt.back(side_length)



def init(size):
    tt.reset()
    tt.setup(600, 600)
    tt.setworldcoordinates(-2 * size, -2 * size, 2 * size, 2 * size)
    tt.speed(0)
    tt.pensize(2)
    tt.up()
    tt.backward(size / 2)



def main():
    _user_input_levels = int(input("Maximum depth: "))
    _user_input_size   = int(input("Largest Side length: "))

    init(_user_input_size)

    recursive_draw_triangles(_user_input_size, _user_input_levels)
    tt.done()


if __name__ == "__main__":
    main()