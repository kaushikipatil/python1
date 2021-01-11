"""
How thick does paper folding get?
Take one sheet out of your newspaper, and fold it in half, then fold it in half
again, and again, and again. Can you fold it 30 times? Pretending that you can
(you probably can’t fold it more than eight times), how thick would it be after
30 times? Assume the paper is 1/200 cm. thick. Write a program to solve this
puzzle. Prompt for the number of folds and output the thickness in meters.
"""

print("We are going to find the thickness of the paper when you fold")

def thickness(fld):
    thickness=((fld*1)/200)
    return print("Thickness will be ",thickness," cm")

print("Enter the the fold")
fold=int(input())

thickness(fold)
