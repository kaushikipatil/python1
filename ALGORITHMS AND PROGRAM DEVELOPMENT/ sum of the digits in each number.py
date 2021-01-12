"""
Write an algorithm that will find the sum of the digits in each number between
1 to 350.
"""

def sfdigits():
    number=int()
    for i in range(1,350):
        number+=i
    print("Sum of disgits from 1 to 350 = ",number)

sfdigits()
