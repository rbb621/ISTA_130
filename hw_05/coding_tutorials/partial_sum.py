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
def partial_sum(n):
    part_sum = 0 
    for i in range(n):
        current_sum = 1 /(2 ** i)
        part_sum += current_sum
    return part_sum


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    max_exponant = 4
    print('partial sum of max exponant ' + str(max_exponant) + ' = ' + str(partial_sum(max_exponant)))

if __name__ == '__main__':
    main()
