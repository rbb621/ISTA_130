'''
BUGS
These functions will run, but they will not do what you want them to do.
Find the bugs in these functions and correct them.
'''
import turtle 

def bug1():
    bit = int(input("Enter a number: "))
    if bit == 0 or bit == 1:
        print(bit, 'is a valid bit.')
    else:
        print(bit, 'is not a valid binary bit.')
        
def bug2():
    name = input('I\'m python, who are you? ')
    print('Hello,', name, 'good to see you!')
    
def bug3():
    maxscore = float(input('How many points can you possibly get? '))
    userscore = float(input('How many points did you get? '))
    percentage = (userscore / maxscore) * 100
    print(percentage)
    if (percentage>=90):
        return "A"
    elif (80<=percentage<90):
        return "B"
    elif (70<=percentage<80):
        return "C"
    elif (60<=percentage<70):
        return "D"
    elif (percentage<60):
        return "F"

def bug4():
    for i in range(10):
        count = 10 - i
        print(count)
    print("Blast off!")   
        
    
'''
CONVERSIONS
These functions will work, but try doing them a different way.
'''

def conversion1():
    
    for i in range(10):
        count = 10 - i
        print(count)
    print('Blast off!')
        
    '''
    after fixing bug4, rewrite it so that it uses a for loop instead of a while loop
    '''
    
def conversion2():
    '''
    convert this code to use complex if statements (using and/or) instead of nested if statements
    '''
    canswim = input('Can this animal swim? ')
    layseggs = input('Does this animal lay eggs? ')
    if canswim == 'yes' and layseggs == 'yes':
        print('It\'s a fish!')
    if canswim == 'yes' and layseggs == 'no':
        print('It\'s a human!')
    if canswim == 'no' and layseggs == 'yes':
            print('It\'s a tortise!')
    if canswim == 'no' and layseggs == 'no':
        print('It\'s a gorilla!')

'''
ERRORS
These functions will not work, and you will get an error message when you try to run them.
Find the errors in these function and fix them.
'''

def error1(hours):
    '''
    this function converts hours to seconds
    hours (int) - an amount of time in hours
    returns - time in seconds
    '''
    minutes = hours * 60
    seconds = minutes * 60
    return seconds
    
def error2():
    num = int(input('Enter a number: '))
    remainder = num % 2 
    if remainder == 1:
        print('This number is odd!')
    else:
        print('This number is even!')
        
def error3():
    age = int(input('Enter your age: '))
    
    if age > 1:
        print('You are ' + str(age) + ' years old!')
    else:
        print('You are only a year old!')

    
'''
OUTPUT
determine the output for this function.
'''

def output1():
    '''
    draw the result of the following turtle.
    '''
    yertle = turtle.Turtle()

    yertle.pensize(10)
    yertle.pencolor('red')
    
    yertle.forward(100)
    yertle.right(90)
    yertle.backward(50)
    yertle.forward(100)

'''
STRINGS
'''
def every_other(word):
    '''
    This function takes a string and returns a new string containing every other letter
    '''
    
    new_word = ""
    
    for i in range (len(word)):
        remainder = i % 2
        if remainder == 0:
            new_word += word[i]
    return new_word
    
def main():
    
    output1()
    error1(8)
    error2()
    error3()
    
    conversion1()
    conversion2()
    
    bug1()
    bug2()
    bug3()
    bug4()
    output1()
    print((every_other('Cookie Monster')))


    #for error 1
    time = int(input('Enter the amount of time in hours: '))
    print(error1(time))
    
    
if __name__ == '__main__':
    main()
    