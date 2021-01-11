"""
What is the invention of chess worth?
There is a popular myth about the man who invented chess. The local ruler was so
pleased with the invention that he offered the inventor a great reward in gold.
The inventor suggested an alternative reward: he would get one grain of wheat on
the first square of the chess board, two grains on the second square, four on
the third, eight on the fourth, and so on, doubling the number of grains each
time. The ruler saw that this must be a much better deal for him, and accepted.
The board has 64 squares. Write a
program to determine the following:
(a) How many total grains of wheat did the ruler have to pay the inventor?
(b) A wheat grain weighs approximately 50 mg. How much did the wheat weigh?
(c) Pick a region (state, country, etc.) and determine how deeply that region would be
covered with that quantity of wheat. Prompt for the area of the region and then
output the depth including the units you use.
"""


import math
print("Welcome to the Chess and rice game :P")

"""
We are going to try first how much giain it will be a
"""
def gaintotal():
    adding=int(1)
    for i in range (0,64):
        adding+=adding
    print("Total gain will be ",adding)
    print("Weight is ",adding*50)  #At here we are calulating the wight of gain

    print("We are going to explore Maharashtra")
    print("Consider that grain length is 9mm and width is 1mm")
    areaofgain=1*9
    totalareaneedtocover=((9*adding)/100000)
    print("Total area need to cover in km ",totalareaneedtocover)
    sqareroot=math.sqrt(totalareaneedtocover)
    print("The depth to grain will be to cover the entire Maharashtra will be ",sqareroot/307713," mm")

gaintotal()
