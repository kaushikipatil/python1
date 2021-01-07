"""
Write a program that prompts for an integer and prints the integer, but if something
other than an integer is input, the program keeps asking for an integer. Here is a sample
session:
"""

print("Let's check that you have enter integer or not. \
    you have to enter integer to terminate the program")

while True:
    try:
        n=int(input("Enter the integer"))
        print("The integer is ",n)
        break
    except ValueError:
        print("Wrong try again")
