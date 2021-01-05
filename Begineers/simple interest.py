"""
Simple interest is calculated by the product of the principal,
number of years, and interest, all divided by 100. Write code
to calculate the simple interest on a principal amount of $10,000
for a duration of 5 years with the rate of interest equal to 12.5%.
"""

print("Hey, this program will help you to find the simple interest")

print("Please Enter your principal Amount, numbers of years and interest repectively")
prin=int(input())
year=int(input())
interest=float(input())

sim_interest= prin*year*interest/100

print("Your Simple interest will be ",sim_interest)
