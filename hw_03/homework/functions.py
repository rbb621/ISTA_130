import random
import math

def chases(predator, prey):
    print('The ' + predator + ' chases the '+ prey)
    

def sum3(num1, num2, num3):
    total = num1 + num2 + num3
    print('The sum of the arguments is:', total)
    


def forecast():
    predict = random.randrange(101)
    print('Chance of rain today:', predict, '%')
    

def radians(degrees):
    
    radians = degrees * math.pi/180
    print("The angle in radians is:", round(radians, 3))
    

def decimal(number):
    
    pos_num = math.floor(number)
    decimal = number - pos_num 
    print('Decimal part:', round(decimal, 3))
    

def erf_plus_gamma(number):
    result = round(math.erf(number) + math.gamma(number), 3)
    
    print('Result:', result)