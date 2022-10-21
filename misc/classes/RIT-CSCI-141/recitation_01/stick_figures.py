"""
CSCI-141 Computer Science 1 Recitation 02-Presentation
01-Introduction
Stick Figures

Demonstrates using Python and turtle with functions to draw two stick figures
side by side.

We'll assume the turtle always starts at the top of the torso/bottom center of the head,
is up, and is facing east before and after drawing each part of the figure.
"""

import turtle

def init():
    """Initialize the turtle settings"""
    turtle.pensize(4)
    turtle.title("Stick Figures")
    turtle.up()

def draw_torso():
    """Draw the main torso"""
    turtle.color('blue')
    turtle.right(90)
    turtle.down()
    turtle.forward(100)
    turtle.up()
    turtle.back(100)
    turtle.left(90)

def draw_legs():
    """Draw the legs"""
    turtle.color('green')
    turtle.right(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.down()
    turtle.forward(30)
    turtle.back(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.back(30)
    turtle.right(45)
    turtle.up()
    turtle.back(100)
    turtle.left(90)

def draw_arms():
    """Draw the arms"""
    turtle.color('yellow')
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.down()
    turtle.forward(30)
    turtle.back(30)
    turtle.left(180)
    turtle.forward(30)
    turtle.back(30)
    turtle.left(90)
    turtle.up()
    turtle.back(30)
    turtle.left(90)

def draw_head():
    """Draw the head"""
    turtle.color('purple')
    turtle.down()
    turtle.circle(25)
    turtle.up()

def draw_stick_figure():
    """Draw a complete single stick figure"""
    draw_torso()            # task 1 - draw the torso
    draw_legs()             # task 2 - draw the legs
    draw_arms()             # task 3 - draw the arms
    draw_head()             # task 4 - draw the head

def main():
    """Draw the two stick figures, side by side"""
    init()
    draw_stick_figure()     # left stick figure
    turtle.forward(100)
    draw_stick_figure()     # right stick figure
    turtle.hideturtle()
    turtle.done()

main()