''' In-class examples. '''

import math

def gpa():
    '''
    Calculate and return the GPA (float) for num_classes classes.
    '''
    num_classes = int(input("Enter the number of classes: "))
    grade_points = 0
    units = 0
    for i in range(num_classes):
        grade = int(input("Enter your grade (0 to 4): "))
        class_units = int(input("Enter the number of units: "))
        units = units + class_units
        grade_points += grade * class_units
    return grade_points / units

def bluebird_count(num_observers):
    '''
    Return the number of bluebirds spotted by a team of num_observers observers.
    '''
    total = 0
    for i in range(num_observers):
        print('---- Observer', i + 1, '----')
        bluebirds = input("Enter number spotted by this observer: ")
        print()
        total += int(bluebirds)
    return total
    
def bluebirds_all_teams():
    '''
    Return the total number of bluebirds spotted
    by all teams of observers.
    '''
    num_teams = int(input("Enter the number of teams: "))
    total = 0
    for i in range(num_teams):
        num_observers = int(input("Enter number of observers, team " + 
                                  str(i + 1) + ": "))
        total += bluebird_count(num_observers)
    return total

def number_of_odds(n):
    '''
    Calculate and return the number of odd numbers 
    between 0 and n, inclusive.
    '''
    num_odds = 0
    for i in range(n + 1):
        num_odds += i % 2
    return num_odds
    
def number_of_odds2(n):
    '''
    Calculate and return the number of odd numbers 
    between 0 and n, inclusive.
    '''
    return (n + 1) // 2
    
def dashes(a_string):
    '''
    Create and return a string that has the same characters
    as string a_string, but each one is followed by a dash.
    '''
    dashed = ''
    for i in range(len(a_string)):
        dashed += a_string[i] + '-'
    return dashed
    
def double_str(a_string):
    '''
    Create and return a string that has the same characters
    as string a_string, but each one is repeated twice.
    '''
    dbl = ''
    for i in range(len(a_string)):
        dbl += a_string[i] * 2     # or a_string[i] + a_string[i]
    return dbl
    
def n_str(a_string, n):
    '''
    Create and return a string that has the same characters
    as string a_string, but each one is repeated n times.
    '''
    result = ''
    for i in range(len(a_string)):
        result += a_string[i] * n     
    return result
    
def reverse_str(a_string):
    rev = ''
    for i in range(len(a_string)):
        rev += a_string[len(a_string) - 1 - i]
    return rev
    
#==========================================================
def main():
    '''
    Test the functions.
    '''
    
    print("Your GPA for the semester is", gpa())
    
    print("Total bluebirds spotted, all teams:", 
          bluebirds_all_teams())
    
    print('number_of_odds(6):', number_of_odds(6))
    print('number_of_odds(7):', number_of_odds(7))

    print('number_of_odds2(6):', number_of_odds(6))
    print('number_of_odds2(7):', number_of_odds(7))
    
    print('dashes("Rocket"):', dashes("Rocket"))

    print('double_str("Rocket"):', double_str("Rocket"))

    print('n_str("Rocket", 7):', n_str("Rocket", 7))

    print('reverse_str("Rocket"):', reverse_str("Rocket"))
    
    a_string = 'Rocket'
    x = 55
    y = 11.0
    print('Should be True:', x > y)
    print('Should be True:', x // y == 5)
    print('Should be False:', x // y == a_string)
    print('Should be False:', x <= y)
    print('Should be True:', 'Rock' in a_string)
    print('Should be True:', 't' in a_string)
    print('Should be False:', 'z' in a_string)

if __name__ == '__main__':
    main()
    
