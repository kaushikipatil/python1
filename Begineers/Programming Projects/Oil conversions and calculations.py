"""
Write a program that will prompt the user for a floating-point number that stands for
gallons of gasoline. You will reprint that value along with other information about gasoline and gasoline usage:
 Number of liters
 Number of barrels of oil required to make this amount of gasoline
 Number of pounds of CO2 produced
 Equivalent energy amount of ethanol gallons
 Price in U.S. dollars
Here are some approximate conversion values:
 1 barrel of oil produces 19.5 gallons of gasoline.
 1 gallon of gasoline produces 20 pounds of CO2 gas when burned.
 1 gallon of gasoline contains 115,000 BTU (British Thermal Units) of energy.
 1 gallon of ethanol contains 75,700 BTU of energy.
 1 gallon of gasoline costs $3.00/gallon.
Look on the Internet for some interesting values for input such as the average number of gallons consumed per person per year,
 or consumed by the country per day, or
consumed per year.
"""

print("Welcome to the oil conversion and calculations")
print("Please enter the gallons of gasoline in float")
gallons=float(input())

print("Number of liters of gasoline ",gallons*3.785)

bar_oil=float(gallons/19.5)
print("Number of barrels of oil required to make this amount of gasoline ",bar_oil)

co2=float(gallons*20)
print("Number of pounds of CO2 produced ",co2)

energy=float(gallons*75700)
print(energy," BTU Equivalent energy amount of ethanol gallons")

cost=float(gallons*3)
print("Price in U.S. dollars ",cost, " $")
