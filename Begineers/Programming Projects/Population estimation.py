"""
The U.S. Census provides information on its web page (http://www.census.gov)
about the current U.S. population as well as approximate rates of change.
Three rates of change are provided:
 a birth every 7 seconds.
 a death every 13 seconds.
 a new immigrant every 35 seconds.

These are obviously approximations of birth, death, and immigration rates, but they
can assist in providing population estimates in the near term.

Write a program that takes years as input (as an integer) and prints out an estimated population (as an integer).
Assume that the current population is 307,357,870, and assume
that there are exactly 365 days in a year.
Hint: Note that the rate units are in seconds.
"""

print("Welcome to the population Estimation of the US")
years=int(input())

birth=float(8.5*60*24*365*years)
print("Birth ", birth)

death=float(4.615*60*24*365*years)
print("Death ",death)

immigrant=float(1.714*60*24*365*years)
print("immigrant ",immigrant)

total=307357870+((birth+immigrant)-death)
print("Population after ",years," years will be ",total)
