'''
Name: Ricky Berliant
Date: 09/19/2025
Class: ISTA 130
Section Leader: Sungjoon Shin

Week 4 Extra Credit: ISTA 130 Execution Trace and Functions Worksheet
'''

 
def diff_squares(first_num, second_num):
    difference = (first_num ** 2) - (second_num ** 2)
    print(f"The difference between the squares of {first_num} and {second_num} is:", difference)


def sum_squares(max):
    ''' Print the sum of squares of integers 1 to max. '''
    sum = 0
    print('x - x**2')
    print('--------')
    for i in range(max):
        num = i + 1
        square = num**2
        print(num, '-', square)
        sum = sum + square
        print()
        print('Sum of squares for 1 through', max, ":", sum)   
        
'''
Function Test: sum_squares(3)

sum_squares(3)
x - x**2
--------
1 - 1

Sum of squares for 1 through 3 : 1
2 - 4

Sum of squares for 1 through 3 : 5
3 - 9

Sum of squares for 1 through 3 : 14

Answer: 1 + 4 + 9 = 14
'''
        

def letter_square(letter, num_rows):
    # Print the first line
    print(letter * num_rows)
    
    # Print the middle lines
    for i in range(num_rows - 2):
        print(letter + ' ' * (num_rows - 2) + letter)
    
    # Print the last line
    print(letter * num_rows)
    
    # Line-break  
    print() 
    
    # trying out the another example to manipulate string
    print('$' * 3 + '-' * 5 + '$' * 3)


def main():
    diff_squares(7, 13)
    sum_squares(3)
    letter_square('W', 7)
    

if __name__ == "__main__":
    main()
