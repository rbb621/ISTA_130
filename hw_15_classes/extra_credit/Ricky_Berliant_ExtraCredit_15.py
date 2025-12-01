import random

'''
Name: Ricky Berliant
Date: 12/4/2025
Class: ISTA 130
Section Leader: Sungjoon Shin
Assignment: Extra Credit Week 15
'''


# If/Else Get Class Function
def get_class(num):
    if num >= 90:
        return "Senior"
    elif num >= 60:
        return "Junior"
    elif num >= 30:
        return "Sophomore"    
    else:
        return "Freshman"
    


# Uppers Function
def uppers(string):
    new_str = ''
    for char in string:
        if char.isupper():
            new_str += char
    return new_str


# Add Lists Function
def add_lists(list_1, list_2):
    result = []
    
    for i in range(len(list_1)):
        result.append(list_1[i] + list_2[i])
    return result
    

# Using while loop
'''
Skill: while loops. 
Given the following lines of code, 
write a while loop that continues rolling
two dice until they have different values showing:
import random
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
'''
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

while die1 == die2:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)


# Using replace() method
'''
Skills: manipulating sequence types. Given the string " I heart Rocket !!!" 
stored in variable astring, 
write a line of code that creates the string 'I$heart$Rocket$!!!'.
'''

astring = 'I heart Rocket !!!'
updated_string = '$'

new_string = astring.replace(' ', updated_string)
print(new_string)

'''
Write a line of code that grabs the word "heart" from astring. 
'''

astring = 'I heart Rocket !!!'
word = astring[2:7]
print(word)


# Rectangle Class
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        return None
        
    def area(self):
        return self.width *  self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        output = "Width: " + str(self.width) + '\n'
        output += "Height: " + str(self.height) + '\n'
        output += "Area: " + str(self.area()) + '\n'
        output += "Perimeter: " + str(self.perimeter())
        return output


# Lett Dict Function
def letter_dict(filename):
    file = open(filename, 'r')
    rocket_dict = {}

    for line in file: 
        parts = line.strip().split()

        for word in parts:
            if not word:
                continue
            first_letter = word[0].lower()

            if first_letter not in rocket_dict:
                rocket_dict[first_letter] = [word]
                
            elif word not in rocket_dict[first_letter]:
                rocket_dict[first_letter].append(word)

    file.close() 
    return rocket_dict


#*********************************************
#               MAIN FUNCTION
#*********************************************
def main():
    
    # Get Class
    print(get_class(31))
    
    # Upper
    print(uppers('Dragon Ball Z'))
    
    # Add Lists
    print(add_lists([10, 20, 30], [1, 2, 3]))
    
    # Letter Dict
    print(letter_dict('rocket.txt'))
    
    # Rectangle
    rectangle = Rectangle(6,4)
    print(rectangle)

    
if __name__ == '__main__':
    main()
        

'''
Write a line of code that
creates the string ' er okt ! ' from the variable. 
'''

astring = 'I heart Rocket !!!'
print(astring[1:16:2])


'''
Write a few lines of code that creates
the list [' I HEAR', ' ROCKE', ' !!! '].
'''

astring = 'I heart Rocket !!!'

new_list = [
    astring[0:6].upper(),
    astring[6:12].upper(),
    astring[12:17].upper()
]

print(new_list)