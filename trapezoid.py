"""
. If the lengths of the two parallel sides of a trapezoid are X meters and Y meters,
respectively, and the height is H meters, what is the area of the trapezoid? Write Python
code to output the area.
"""

print("This program is made to calculate the area of Trapezoid")

print("Enter the X and Y in meters")
X=int(input())
Y=int(input())

print("Enter the height in meters")
h=int(input())

area=((X+Y)/2*h)

print("The area of trapezoid is ",area)
