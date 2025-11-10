'''
Author: Will Hancock
Date: 11/10/2025
Class: ISTA 130
Section Leader: Sungjoon

Description:
<ISTA 130 Dictionaries Discussion>

'''

#function definitions

def find_key(dictionary1, key):
    # checks for key in the dictionary
    return key in dictionary1

def get_keys(dictionary2, value):
    list_of_keys = []
    for key in dictionary2:
        if value in dictionary2[key]:
            list_of_keys.append(key)
    return list_of_keys

#==========================================================
def main():

    find_key()
    get_keys()
    
if __name__ == '__main__':
    main()