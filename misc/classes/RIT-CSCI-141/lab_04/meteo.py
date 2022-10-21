"""
    meteo.py
    assignment: lab 4
    language: python3
    author: Stanley Goodwin

"""
import turtle as t

def background():
    screen = t.Screen()
    screen.bgpic("simland.png")
    t.setup(1100, 650, 0, 0)
    
def draw_rectangle(length = 36, width = 16):
    """
    draws a rectangle with the given length and width
    :param length:
    :param width:
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    # Draw rectangle
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)

def snowflake(length = 8):
    """
    draws a 6-arms snowflake
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    t.pencolor("blue")
    t.pd()
    for i in range(6):
        t.forward(length)
        t.back(length)
        t.left(60)
    t.pu()
    t.pencolor("black")

def draw_sun(r = 16):
    """
    draws a sun about the bottom
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    # Draw sun
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def draw_rain(size = 16):
    """
    draws 3 rain streaks and a cloud
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    draw_cloud(size)
    
    t.up()
    t.backward(3 * size)
    t.right(90)
    t.forward(size)
    t.left(90)
    draw_streak(size)
    t.forward(0.75 * size)
    draw_streak(size)
    t.forward(0.75 * size)
    draw_streak(size)
    t.forward(0.75 * size)
    draw_streak(size)
    t.forward(0.75 * size)

def draw_streak(size):
    """
    draws a single rain streak
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    t.pencolor("blue")
    t.pd()

    # Top streak
    t.left(60)
    t.forward(size)
    t.back(size)
    t.right(60)
    
    t.pu()
    t.pencolor("black")
 
def draw_cloud(r = 16):
    """
    draws a pretty cloud as a combination of: 1 circle of radius r,
    2 circles of radius r/2 and a rectangle 2r x r
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up, pencolor black
    """
    t.pencolor("blue")
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(r / 2)
    draw_rectangle(2.2 * r, r)
    t.forward(1.2 * r)
    t.circle(r)
    t.forward(1.2 * r)
    t.circle(r / 2)
    t.end_fill()
    t.pencolor("black")
    
def draw_snow(size=8):
    """
    draws 3 snowflakes and a cloud
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    draw_cloud(2 * size)
    t.up()
    t.backward(4 * size)
    t.right(90)
    t.forward(size)
    t.left(90)
    snowflake(size)
    t.right(45)
    t.forward(2 * size)
    t.left(45)
    snowflake(size)
    t.left(45)
    t.forward(2 * size)
    t.right(45)
    snowflake(size)

def draw_temperature(temperature):
    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    draw_rectangle()
    t.end_fill()
    t.pencolor("black")
    t.write(f"{temperature} F", font = ("Arial", 9, "bold"))

def draw_warning(radius):
    """
    draws a warning circle about the bottom
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    # Draw sun
    t.pd()
    t.pencolor("red")
    t.circle(radius)
    t.pencolor("black")
    t.pu()

if __name__ == "__main__":
    background()
    t.done()