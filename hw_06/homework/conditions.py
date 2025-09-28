'''
Name: Ricky Berliant
Date: 09/29/2025
Class: ISTA 130
Section Leader: Sungjoon Shin
'''


'''
Word Length - 

Checks the how many characters are in a word. 
The message will print if it's longer or shorter than the number of characters, 
and the word itself.

However, it it's exactly same length, then it prints 'Exactly' the amount of 
characters in a given word.

'''
def word_length(word, length):
    if len(word) > length:
        print('Longer than', length, 'characters:', word)
    if len(word) < length:
        print('Shorter than', length, 'characters:', word)
    if len(word) == length:
        print('Exactly', length, 'characters:', word)


'''
Stop Light - 

Determines the color on when it's going to change, 
depending on the seconds.
'''

# based on the number of seconds
def stop_light(color, seconds):
    
    # green
    if color == 'green':
         if seconds > 60:
            return 'yellow'
         else:
             return 'green'
        
    # yellow
    elif color == 'yellow':
        if seconds > 5:
            return 'red'
        else:
            return 'yellow'
        
    # red
    elif color == 'red':
        if seconds > 55:
            return 'green'
        else:
            return 'red'

'''
Is Normal Blood Pressure -

If the number of either systolic and diastolic are in the range, 
it will return True.

Otherwise, it will return False if stolic is higher than 120 and diastolic is 
higher than 80
'''

def is_normal_blood_pressure(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return True
    else:
        return False

'''
Doctor -

It asks for the user to input the blood readings. 
If the number is higher than usual, it will print, "Your blood pressure is nomal."
Otherwise, it will print out "Your blood pressure is high."
'''

def doctor():

    # Input reading
    systolic_reading = int(input("Enter your systolic reading: "))
    diastolic_reading = int(input("Enter your diastolic reading: "))
    
    if systolic_reading < 120 and diastolic_reading < 80:
        print("Your blood pressure is normal.")
    else:
        print("Your blood pressure is high.")
        
'''
Pants Size -
The program determines what size the person should wear 
depending on the waist_size.
'''

def pants_size(waist_size):
    if waist_size >= 34:
        return 'large'
    elif waist_size >= 30:
        return 'medium'
    else:
        return 'small'   

'''
Pants Fitter - 
1. This program first asks the user to enter their name
2. then prompts the waist_size, num_of_pants, and fashion_choice. 
3. Price of pants is labeled
4. Then the size of the pants is determined by the waist_size. 
5. Afterwards,the program calculates total_price of the number of pants 
and the type of pants they are wearing.
6. Prints out the number of pants, size, fashion choice, and total price
'''

def pants_fitter():
    
    # Name
    name = input("Enter your name: ")
    print("Greetings", name, 'welcome to Pants-R-Us')
    
    # Size, number of pants, and fasion choice
    waist_size = int(input("Enter your waist size in inches: "))
    num_of_pants = int(input("How many pairs of pants would you like: "))
    fashion_choice = input("Would you like regular or fancy pants? ")
    
    # Price of pants
    regular_pants = 40
    fancy_pants = 100
    
    # Size of pants
    if waist_size >= 34:
        size = 'large'
    elif waist_size >= 30:
        size = 'medium'
    else:
        size = 'small' 

    # Calculating total price of number and type of pants
    
    # Regular
    if fashion_choice == 'regular':
        total_price = num_of_pants * regular_pants
    # Fancy
    elif fashion_choice == 'fancy':
        total_price = num_of_pants * fancy_pants
    else:
        total_price = num_of_pants * regular_pants

    print(num_of_pants, 'pairs of', size, fashion_choice, 'pants: $', total_price)

    return None

'''
Dig Dug -
Prints numbers from 1 to number, 
replacing multiples of 3 with 'dig', 5 with 'dug', 
and both with 'digdug'.
'''

def digdug(number):
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, ': digdug')
        elif i % 3 == 0:
            print(i, ': dig')
        elif i % 5 == 0:
            print(i, ': dug')

'''
Beef Type - 
Depending on the percentage of the percent_lean is what prints out 
the food name. When the program returns 'Unkown' means it's not listed in the
program
'''            
def beef_type(percent_lean):
    if percent_lean < 78:
        return 'Hamburger'
    elif percent_lean >= 78 and percent_lean < 85:
        return 'Chuck'
    elif percent_lean >= 85 and percent_lean < 90:
        return 'Round'
    elif percent_lean >= 90 and percent_lean <= 95:
        return 'Sirloin'
    else:
        return "Unknown"
    
'''
Species Height - 
Prints out the average height of Human and Klingon. 
Then prints out if the species height is below, average, or above average, 
depending on the inches being measured
'''

def species_height(species, inches):
    
    # Species Average height
    if species == "Human":
        average = 67
    elif species == "Klingon":
        average = 71
    
    # Average Scale
    if inches > average:
        print("Above Average")
    elif inches < average:
        print("Below Average")
    else:
        print("Average")

'''
Sooner Date -

Prints out the month numer and day number. If the month smaller is bigger than other 
month number, print out the smaller (earlier) month number. 
Otherwise print out the later month number. Same applies for day as well.
'''        

def sooner_date(month_num_01, day_num_01, month_num_02, day_num_02):
    
    # Comparing Months
    if month_num_01 < month_num_02:
        print(month_num_01, "/", day_num_01)
    elif month_num_01 > month_num_02:
        print(month_num_02, "/", day_num_02)
    
    # Same Month
    elif month_num_01 == month_num_02:
        if day_num_01 < day_num_02:
            print(month_num_01, "/", day_num_01)
            
        # Comparing Days 
        if day_num_02 < day_num_01:
            print(month_num_02, "/", day_num_02)
        
        if day_num_02 == day_num_01:
            print(month_num_01, "/", day_num_01)
    else:
        print(month_num_01, "/", day_num_01)