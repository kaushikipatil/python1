"""
Write a program that prompts for a number and checks whether or not it is a positive
number. If it is a negative number, print ‘Negative’, if it is a positive number, print
‘Positive’, and if the input is 0, then print ‘Zero’.
"""

print("Hello, This program will tell you that number is positive, negative and zero")
n=int(input())

if n<0:
    print("Negative")

elif n>0:
    print("Positive")

else:
    print("Zero")
