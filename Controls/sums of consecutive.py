"""
Modify your program by enclosing your loop in another loop so that you can find
consecutive sums. For example, if 5 is entered, you will find five sums of consecutive
numbers:
1 =1
1+2 = 3
1+2+3 = 6
1+2+3+4 = 10
1+2+3+4+5 = 15
Print only each sum, not the arithmetic expression
"""

print("This program is going to print the consecutive number for you")

print("Please enter the number of which you want to find the consecutive number")
n=int(input())

counter=int(0)
x=int(0)

for x in range(x,n):
    x+=1
    counter=counter+x
    print(counter)
