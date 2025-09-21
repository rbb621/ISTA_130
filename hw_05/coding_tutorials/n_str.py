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
def n_str(input_str, num_times_char_repeated):
    string_length = len(input_str)
    final_str = ''
    for i in range(string_length):
        current_str_part = input_str[i]*num_times_char_repeated
        final_str = final_str + current_str_part
    return final_str

#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment

    print(n_str('spaghetti', 3))
 
if __name__ == '__main__':
    main()
