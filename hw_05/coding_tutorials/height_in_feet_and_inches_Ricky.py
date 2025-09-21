'''
Exercise: combining input, print, //, and %
Write a function called height that gets the user's height in inches (as input) and
prints it out in feet and inches per the following example:
Enter your height in inches: 69
Your height is: 5.0 feet, 9.0 inches
'''


def height(feet):
    
    inches = input("Enter your height in inches: ")

    person_feet = int(inches) // feet
    
    person_inches = int(inches) % feet
    
    print("Your height is: " + str(person_feet), "feet, " + str(person_inches), "inches")
    

def main():
    height(12)
    

if __name__ == '__main__':
    main()