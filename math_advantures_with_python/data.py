#### calculate the value of the function for a paticular variable.

import math

def f(x):
    return math.sqrt(x+3) - x + 1
def g(x):
    return math.pow(x, 2) - 1
def h(x):
    math.pow(x, 2) + x ** -1 + 2

# list of values to plug in
for x in [0, 1, math.sqrt(2), math.sqrt(2)-1]:
    print("f({:.3f}) = {:.3f}".format(x, f(x)))
    print("f({:.3f}) = {:.3f}".format(x, g(x)))
    #print("f({:.3f}) = {:.3f}".format(x, h(x)))

#### Simple Tortle:
from turtle import *
forward(100)
shape('turtle') # circle, square, arrow

from turtle import *
forward(100)
shape('triangle')
right(45) # turn to  right with 45 degrees
forward(150) # go forward for 150 pixels.

#### Draw a Square:
from turtle import *
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

#### Drawing a Square using for loop
from turtle import *
shape('turtle')

for i in range(4):
    forward(100)
    right(90)


#### Drawing a Square using function
from turtle import *
shape('turtle')

def square():
    for i in range(4):
        forward(100)
        right(90)

square()



#### Draw 60 Squares, turning right 5 degrees after each square:
from turtle import *
shape('turtle')
speed(0) # 0 -> fast, 1,2,3,4,5 -> slow

# Define the Square
def square(side_length = 100): # putting the default value is called making the program more robust:
    for i in range(4):
        forward(side_length)
        right(90)

# Drawing the Square 60 times:
for i in range(60):
    square()
    right(5)


#### Draw a triangle:
from turtle import *
shape('turtle')
speed(0)

def triangle(side_length = 100):
    for i in range(3):
        forward(side_length)
        right(120) # turtle turns the external angle


triangle(200)


#### POlygon with n-number of sides:
from turtle import *
shape('turtle')
speed(0)

def polygon(sides = 3, length=100):
    for i in range(sides):
        forward(length)
        right(180 - (180 * (sides-2)) / sides) # 180 * (sides-2) / sides; 180 for considering external angle
        #right(60)

length =2
for i in range(50):
    polygon(4, length)
    #length = length + 5
    length += 5



#### POlygon with n-number of sides and changing its position
from turtle import *
shape('turtle')
speed(0)

def polygon(sides = 3, length=100):
    for i in range(sides):
        forward(length)
        right(180 - (180 * (sides-2)) / sides) # 180 * (sides-2) / sides; 180 for considering external angle
        #right(60)

length = 5
for i in range(60):
    polygon(3, length)
    #length = length + 5
    length += 5
    right(5)


#### Star Spiral
from turtle import *
shape('turtle')
speed(0)

def star(sides = 3, length=100):
    for i in range(sides):
        forward(length)
        #right(180 - (180 * (sides-2)) / sides) # 180 * (sides-2) / sides; 180 for considering external angle
        right(180 - (180/sides)) # sum of all interior angles in star is 180

length = 50
for i in range(60):
    star(5, length)
    length = length + 5
    length += 5
    right(5)



