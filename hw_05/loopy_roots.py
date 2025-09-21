'''
Author: Duane Bryant
Date: 17 Sept 2025
Class: ISTA 130
Section Leader: Sunghoo

Description:
write a function called loopy_roots that takes no parameters. Using a for loop, print the square root 
of every integer between 1 and 10 in this format: "integer : root".
'''


import math
#imports the math

def loopy_roots():
# going to print SQRT of intergers from 1-10 in interger and root format
    for i in range (1, 11):
        root = math.sqrt(i)
        print(f"{i} : {root}")

def main():
   # calling in the function
    loopy_roots()

if __name__ == '__main__':
    main()
