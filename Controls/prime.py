"""
Write a program that checks to see if a number N is prime. A simple approach checks
all numbers from 2 up to N, but after some point numbers are checked that need not be
checked. For example, numbers greater than √N need not be checked. Write a program
that checks for primality and avoids those unnecessary checks. Remember to import the
math module.
"""
import math

print("Prime number")

print("Enter the prime number")
N=int(input())

squareroot=int(math.sqrt(N))

for i in range(2,squareroot):
    if(N<squareroot):
        for i in range(2,N):
            if (N % i) == 0:
                print(N,"is not a prime number")
                break
            else:
                print(N,"is a prime number")
