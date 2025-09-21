'''
Author: Dan Charbonneau
Date: Feb 4 2022
Class: ISTA 130
Section Leader: NA

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def inches_to_ft_and_inches():
    height_in_inches = input('Enter your height in inches: ')
    total_feet = int(height_in_inches) // 12
    total_inches = int(height_in_inches) % 12
    print('Your height is: ' + str(total_feet) + 'feet, ' + str(total_inches) + ' inches')
    return None
#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    inches_to_ft_and_inches()
    

if __name__ == '__main__':
    main()
