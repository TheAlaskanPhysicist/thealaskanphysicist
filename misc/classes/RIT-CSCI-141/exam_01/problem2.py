"""
Author: Stanley Goodwin
Date: 2/18/2022
"""
import turtle as tt



def draw_triangle(side_length):

    # Draw 3 sides to form triangle
    for i in range(3):
        tt.forward(side_length)
        tt.left(120)



def triangles_iter(side, num):
    _total_perimeter = 0
    for i in range(num):
        _side_length = side - 10 * i
        draw_triangle(_side_length)
        tt.forward(_side_length)
        _total_perimeter += 3 * _side_length
    print("Total Length: " + str(_total_perimeter))
    return _total_perimeter



def main():
    tt.color("#009900")

    _user_side_length = int(input("Side length: "))
    _user_depth_num   = int(input("Iterations: "))

    triangles_iter(_user_side_length, _user_depth_num)



if __name__ == "__main__":
    main()
    tt.done()