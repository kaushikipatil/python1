"""
We are going to write the code to multiply and add the number with the function.
"""

def addition(n1,n2):
    return n1 + n2

def multiplication(n1,n2):
    return n1*n2

print("Enter two number")
no1=int(input())
no2=int(input())

addit=addition(no1,no2)
print("Addition of two munber is: ",addit)

multi=multiplication(no1,no2)
print("Multiplication of two number is: ",multi)
