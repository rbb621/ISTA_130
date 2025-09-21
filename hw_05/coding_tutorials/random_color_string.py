'''
Author: Dan Charbonneau
Date: Feb 4 2022
Class: ISTA 130
Section Leader: NA

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment
import random

# put all of your function definitions below this line and then delete this comment
def random_color_string():
    color_string = '#'
    hex_digit_string = '0123456789ABCDEF'
    for i in range(6):
        current_hex_char = hex_digit_string[random.randrange(16)]
        color_string = color_string + current_hex_char
    return color_string

#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    print(random_color_string())
    

if __name__ == '__main__':
    main()
