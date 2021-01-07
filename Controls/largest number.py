"""
Write a program that will print the largest among three numbers
"""

print("Hello we are going to find the largest number among three numbers")

print("Please enter three numbers")
n1=int(input())
n2=int(input())
n3=int(input())

if n1>=n2 and n1>=n3:
    print(n1," is greater number")

elif n2>=n3 and  n2>=n1:
    print(n2," is greater number")

elif n3>=n1 and n3>=n2:
    print(n3," is greater number")

else:
    print("All are equal number")
