import turtle
from turtle import Turtle
from turtle import Screen
import random

# Define width and height of screen
WIDTH, HEIGHT = 500, 500

# Function that moves Turtle object.
def draw():
    tim.circle(100)

# Function that passes r,g,b int values to pencolor method
def color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.pencolor(r,g,b)

# Function that moves the tim object angle equal to 360/n
def turn(n):
    tim.right(360/n)

# Create Screen object
screen = Screen()
screen.setup(WIDTH,HEIGHT)

#Prompt user for how many circles to draw
n = int(screen.numinput("Circle Count","How many circles?"))

# Create Turtle Object and call methods
tim = Turtle()
turtle.colormode(255)
turtle.speed("fastest")

# Draw circles in range of n where n equals the user input
for x in range(n):
    draw()
    color()
    turn(n)

# Exit program on click
screen.exitonclick()
