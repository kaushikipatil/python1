"""
For our rainfall problem, how can we develop our algorithm? First, we observe that the
problem statement is a combination of linear measurement (inches) and square measurement (acres), but the desired result is in volume (gallons). We must find some intermediate
unit for the conversion process. Representing volume in cubic feet is one way; metric units
would work as well.
Our algorithm starts with these steps:
1. Prompt the user for the number of inches that have fallen.
2. Find the volume (in cubic feet) of water (where volume = depth * area).
3. Convert the volume (in cubic feet) to gallons.
The Internet can provide the conversion formulas:
1 acre = 43,560 square feet
1 cubic foot = 7.48051945 gallons
With this information, we can start on our algorithm. Let’s begin parts two and three,
assuming just one inch of rain on one acre:
1. Find the volume in cubic feet of water of one inch over one acre
1 inch is equivalent to 1/12 foot
volume = depth * area = (1/12)*43560 cubic feet
2. Convert the volume in cubic feet to gallons
gallons = volume * 7.48051945
Now let’s try this in Python
"""


print("How many inches rain have falen")
inches=int(input())

volume=float(inches/12*43560)
gallons=volume*7.48051945
