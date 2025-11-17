'''
Author: <your name>
Date: <the date>
Class: ISTA 130
Section Leader: <your section leader>

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment
def upper_list(some_list):
    '''
    takes a list of stings as its sole argument and
    converts them all to uppercase. The function should alter the
    original list
    '''
    for list_index in range(len(some_list)):
        some_list[list_index] = some_list[list_index].upper()
    return None

def upper_list2(some_list):
    '''
    takes a list of strings as its sole argument. It
    returns a new list containing all of the strings
    from the original list in uppercase.
    '''
    new_list = []
    for list_index in range(len(some_list)):
        new_list.append(some_list[list_index].upper())
    return new_list

def upper_values(some_dict):
    for key in some_dict.keys():
        #some_dict[key] = upper_list2(some_dict[key])
        upper_list(some_dict[key])
    return None

def upper_values2(some_dict):
    new_dict = {}
    for key in some_dict.keys():
        new_dict[key] = upper_list2(some_dict[key])
    return new_dict


# put all of your function definitions below this line and then delete this comment



#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    test_list1 = ['tallulah','chewy','roscoe']
    upper_list(test_list1)
    print('test list 1: ', test_list1, '\n')
    test_list2 = ['tallulah','chewy','roscoe']
    print('output of upper_list2: ', upper_list2(test_list2), '\n')
    print('test list 2: ', test_list2, '\n')

    test_dict1 = {'a':['aardvark','ant'], 'b':['buffalo','bull','bulldog']}
    print('output of upper_values: ', upper_values(test_dict1), '\n')
    print('test_dict1: ', test_dict1, '\n')

    test_dict2 = {'a':['aardvark','ant'], 'b':['buffalo','bull','bulldog']}
    print('output of upper_values2: ', upper_values2(test_dict2), '\n')
    print('test_dict1: ', test_dict2, '\n')
  
  

if __name__ == '__main__':
    main()
