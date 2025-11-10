'''
Author: Edwin Bazan
Date: 11NOV25
Class: ISTA 130
Section Leader: Sungjoon Shin

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def find_key(dict, key):
    for ch in dict:
        if key in dict:
            return True
        else:
            return False


def get_keys(dict2, value):
    new_list = []
    for ch in dict2:
        if value in dict2[ch]:
            new_list += [ch]
    return new_list

#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment



if __name__ == '__main__':
    main()
