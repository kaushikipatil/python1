"""
Turtle polygons
Prompt for the desired number of sides for your polygon. Given that the interior
angle of a regular polygon is (sides − 2) × 180◦ )/sides, draw the polygon.
Optional: Prompt for a color and color the interior of your polygon.
"""

import turtle

# creating turtle pen
t = turtle.Turtle()

# taking input for the no of the sides of the polygon
n = int(input("Enter the no of the sides of the polygon : "))

# taking input for the length of the sides of the polygon
l = int(input("Enter the length of the sides of the polygon : "))


for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)
