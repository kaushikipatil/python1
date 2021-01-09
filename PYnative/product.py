"""
Question 1: Given a two integer numbers return their product and  if the
product is greater than 1000, then return their sum"""

print("Enter in the world of the product")

print("Enter two numbers")
a=int(input())
b=int(input())

multiply=a*b

if multiply>1000:
    print(a+b)
else:
    print(multiply)
