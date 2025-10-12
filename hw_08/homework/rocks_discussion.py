'''
Name: Ricky Berliant
Date: 10/17/2025
Section Leader: Sungjoon
Week 9: while Loops 2 Discussion
Test File: rocks_discussion.py
'''


'''
Write a function called price_of_rocks. It has no parameters. In a while loop, get a rock type and a weight from the user. 
Keep a running total of the price for all requested rocks. Repeat until the user wants to quit, which they can do my entering 'q' 
(lowercase, no quotes around it) at any time the user is asked for an input. Quartz crystals cost $23 per pound. Garnets cost 
$160 per pound. Meteorite costs $15.50 per gram. Assume the user enters weights in the units as above. Return the total price of all of the material.

For this discussion, you should first write pseudocode for how you would solve this problem 
(reference pseudocode.py in the Week 7 Coding Tutorials section for an example). 
Then write the code for how you would tackle this function. 
Please submit a Python file called rocks_discussion.py that defines the function (code) and calls it in main().
'''


"PSEUDO CODE" 
'------------------------------------------------------------'
# Create a function price of rocks
# Nothing should be inside the function
# Before creating a while loop, display the rock type and it's value
# Convert the prices into decimals
# Quartz crystal cost $23 per pound
# Garnets cost $160 per pound
# Meteorite costs $15.50 per gram
# Display the total starting at 0
# Create a while loop
# Inside while loop, have the user get type of rock
# After that, type in the weight for the rocks
# Make sure the weight is converted into float
# Calcuate the value of the rock with the weight
# After calcuating add up the total amount until finished
# Ask if they want to continue
# Once finished, type the letter q to quit
# After quitting, return the total price of the rocks
'------------------------------------------------------------'


# Price of Rocks Program

def price_of_rocks():
    quartz_crystal_price = 23
    garnets_price = 160
    meteorite_price = 15.50
    quartz_crystal = 'quartz crystal'
    garnets = 'garnet'
    meteorite = 'meteorite'
    total = 0
    
    print("Quarts Crystals Price: $23.00/per pound")
    print("Garnet Price Price: $160.00/per pound")
    print("Meteorite Price: $15.50/per gram")
    print()    

    while True:
        #User Input
        rock_type_choice = input("Get the rock type from the user (quartz crystals, garnets, or meteorite) \nor (press q to quit): ")
        
        if rock_type_choice.lower() == 'q':
            break

        
        print()
        weight = input("Enter the weight: ")
        
        if weight.lower() == 'q':
            break
        
        weight = float(weight)

        # Rock Types and Weight
        if rock_type_choice == quartz_crystal:
            total += quartz_crystal_price * weight
    
        elif rock_type_choice == garnets:
            total += garnets_price * weight
        
        elif rock_type_choice == meteorite:
            total += meteorite_price * weight
            
        else:
            print("Invalid rock type. Try again.")
            continue
            
        # Total Price
        print()
        print(f'The total value so far is {total:.2f}')

    return total
        

def main():
    print()
    grand_total = price_of_rocks()
    print(f"The grand total of everything is {grand_total}")


if __name__ == '__main__':
    main()
    




