"""
(Perfect numbers). In this chapter is a program that checks for perfect numbers.
If you wanted to check many numbers (a large range of numbers), to see if any
were perfect, then the program we wrote might not be the best. What could we do
to improve it? For example, how would we output only perfect numbers, but just
keep countof the deficient and abundant numbers? Do we need to check every
number from 2 to number-1?
"""

print("Perfect Number")
n=int(input())

counter=int(1)
per=int(0)

while counter<n:
    if n%counter==0:
        per+=counter
    counter+=1

if per==n:
    print("Perfect number")
else :
    print("Not a perfect number")
