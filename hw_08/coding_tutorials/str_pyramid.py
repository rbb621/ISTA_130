'''
Author: <your name>
Date: <the date>
Class: ISTA 130
Section Leader: <your section leader>

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment
def str_pyramid(some_string):
    for i in range(len(some_string)):
        print(some_string[i] * (i + 1))
    return None


# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    str_pyramid('Rocket')


if __name__ == '__main__':
    main()
