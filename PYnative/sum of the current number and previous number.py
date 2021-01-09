"""
Question 2: Given a range of first 10 numbers, Iterate from start number to the
end number and print the sum of the current number and previous number
"""
print("Sum of the current number and previous number")

print("Enter the number till you want to print")
n=int(input())

for i in range(1,n+1):
    a=i-1
    print("Current number ",i," Previous number ",i-1, " Sum of number is",i+a)
    #print("Previous number",i-1)
