"""
Weird multiplication
For this assignment, you will be implementing the so-called “Russian Peasant”
or “Ancient Egyptian” method for multiplication. It looks a little odd, but just
think of it as an algorithm, a recipe for doing multiplication in a way other
than what you learned in grade school.
The algorithm is as follows. If A and B are the 2 integers (only integers) to be
multiplied, we repeatedly multiply A by 2 and divide B by 2, until B cannot be
divided any further, that is, until its value becomes 0 (remember, this is integer
division). During each step, whenever B is an odd number, we add the
corresponding A value to the product we are generating. In the end, the sum of
the A values that had corresponding odd B values is the product. Get it?
Here is an example:
If the two integers to be multiplied are 34 and 19, the operations would be:
A   B Comment
34 19 add A to the product, B is odd
68 9 add A to the product, B is odd
136 4 ignore this A value, B is even
272 2 ignore this A value, B is even
544 1 add A to the product, B is odd
Sum up all the A values that had odd B values and you get: 34+68+544 = 646 =>
Final product.
(a) Part 1: Write a program to find the product of two integers.
(b) Part 2: Modify your program so that it repeatedly asks whether you want to
find
another product.
"""
"""
def weird_multiplication(a,b):
    multiplication=a*b
    print(multiplication)

A=int(input("Ente the A integer"))
B=int(input("Ente the B integer"))
weird_multiplication(A,B)
"""


print("Enter A value and the B Value")
A= int(input())
B=int(input())
addition=int(0)
if(B%2):
    addition=A
else:
    addition=int(0)
while B:
    A=A*2
    B=int(B/2)
    if B%2:
        addition+=A
        print(A, B,  addition)
    else:
        continue

print("Addition ",addition)
