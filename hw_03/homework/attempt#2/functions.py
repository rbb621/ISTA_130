'''
Name: Ricky Berliant
Date: 09/10/2025
Class: ISTA 130
Section Leader: ???

Put your header comments here.
'''

""" 
    *********************************
    Answers to questions:
    1) 11034644575 
    2) Chance of rain today: 81 %
    3) Chance of rain today: 14 %
    4) The angle in radians is: 1.571
    5) The angle in radians is: 3.142
    6) Result: 2.293
    7) Result: 3.902
    8) Result: 9.626
    ********************************* 
"""

import math, random

# Put your function definitions below this line:

def chases(predator, prey):
    print('The', predator, 'chases the', prey)
    

def sum3(num1, num2, num3):
    print("The sum of the arguments is:", num1 + num2 + num3)
    
def forecast():
    chance_of_rain = random.randrange(101)
    print("Chance of rain today:", chance_of_rain, "%")


def radians(degrees):        
    radians = round(degrees * math.pi / 180, 3)
    print("The angle in radians is:", radians)
    

def decimal(number):

    integer_part = math.floor(number)
    decimal_part = round(number - integer_part, 3)

    print("Decimal part:", decimal_part)


def erf_plus_gamma(number):
    
    result = round(math.erf(number) + math.gamma(number), 3)

    print("Result:", result)