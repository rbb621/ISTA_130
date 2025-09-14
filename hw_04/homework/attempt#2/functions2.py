import math

'''
Name: Ricky Berliant
Date: 09/25/2025
Class: ISTA 130
Section Leader: Sungjoon Shin
'''

#1 print_word 
'''
    This function prints a word a given number of times, 
    each preceded by a line number and arrow. 
    
    Parameters:
    number (int): how many times to print the word
    word (str): any word to print
    
    Output: prints each line in the format "n --> word"
'''

def print_word(number, word):
    for i in range(number):
        print(i + 1, "-->", word)


#2 bacteria 
'''
    This function simulates bacteria growth over time.
    
    Parameters:
    num_of_minutes (int): number of minutes that have passed
    generations (int): number of generations to simulate
    
    Output: prints the minute and bacteria for each generation
'''

def bacteria(num_of_minutes, generations):

    for i in range(generations):
        i += 1
        time_passed = num_of_minutes * i
        bacteria_count = 2 ** i 
        print("after", time_passed, "minutes: ", bacteria_count, "bacteria")
    



#3 convert_to_copper 
'''
    This function convert gold and silver coins into copper
    Parameters:
    gold_coins (int) = gold coins
    silver_coins (int) = silver coins
    copper_coins (int) = copper coins
    
    Output: prints the coin breakdown and total in copper
'''  
def convert_to_copper(gold_coins, silver_coins, copper_coins):
    total_copper = (gold_coins * 10 * 5) + (silver_coins * 5) + (copper_coins)

    print(gold_coins, "gp,", silver_coins, "sp,", copper_coins, "cp converted to copper is:", total_copper, "cp")
    


#4 convert_from_copper 
'''
    This function convert all copper coins into gold, silver, and any remaining copper coins

    Parameters:
    copper_pieces (int) = total number copper coins
    
    Output: prints the equivalent number of gold, silver, and copper coins
'''
def convert_from_copper(copper_pieces):

    gold_remainder = (copper_pieces//50)
    remainder = (copper_pieces % 50) 
    silver_remainder = (remainder // 5)
    copper_remainder = (remainder % 5)
    
    print(copper_pieces, "copper pieces is:", gold_remainder, "gp,", silver_remainder, "sp,", copper_remainder, "cp")


#5 repeat_word      
'''
    This function prints a full column and row of repeated words.
    
    Parameters:
    word (str): any word to repeat
    num_of_rows (int): number of rows from top to bottom to print
    num_of_columns (int): number of times the word repeats in each row
    
    Output: prints the word repeated in a grid format
'''
def repeat_word(word, num_of_rows, num_of_columns):
    for i in range(num_of_rows):
        print(word * num_of_columns)


#6 text_triangle 
'''
    This function prints a triangle made out of the letter X.
    
    Parameters:
    num_of_rows (int): number of rows to form a triangle
    
    Output: prints a triangle shape of X letter
'''
def text_triangle(num_of_rows):
    for i in range(num_of_rows - 1):
        print('X' * (i + 1))
    print('X' * (num_of_rows))
        
        
#7 surface_area_of_cylinder    
'''
    This function prints a surface area of cylinder, using the radius and height
    
    Parameters:
    radius (float): radius of the cylinder
    height (float): height of the cylinder
    
    Output: prints the calculated surface area of a cylinder
'''
def surface_area_of_cylinder(radius, height):
    radius_float = float(radius)
    height_float = float(height)
    surface_area = (2 * math.pi * radius_float * height_float) + (2 * math.pi * radius_float**2)
    print("The surface area of a cylinder with radius", radius_float, "and height", height_float, "is", surface_area)
    

# 8 tree_height  
'''
    This function prints the height of a tree, using the pythagorean theorem
    The distance from the tree to find the length of a kite string.

    Parameters:
    distance (int): distance on how far the kite will travel
    length (int): length of the kite string (hypotenuse)
    
    Output: prints the length of the kite string, distance, and height of how far the kite will travel
'''
def tree_height(distance, length):
    
    height = math.sqrt(length ** 2 - distance ** 2)
    
    print("Kite string:", length)
    print("Distance:", distance)
    print("Height:", height)
