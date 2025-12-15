'''
Sarah Stueve
ISTA 130
SL:...
4/10/20

Week 13: Mutable vs Immutable Worksheet
'''

def upper_list(str_lst):
    '''
    Parameter str_lst is a list of strings. Alter the list in place
    by replacing each string with the same string in uppercase. Returns None (why?)
    '''
    for i in range(len(str_lst)):
        str_lst[i] = str_lst[i].upper()
    return None

def upper_list2(str_lst):
    '''
    Parameter str_lst is a list of strings. Return a new list that
    contains the same strings as in str_lst, but in uppercase. Does not alter str_lst.
    '''
    upper_lst = []
    for word in str_lst:
        upper_lst.append(word.upper())
    return upper_lst

def upper_values(word_dict):
    '''
    Parameter word_dict is a dictionary mapping keys to lists of strings. Alter each value in place by replacing each string with the same string in uppercase. Returns None. (why?)
    '''
    for key in word_dict:
        upper_list(word_dict[key])

def upper_values2(word_dict):
    '''
    Parameter word_dict is a dictionary mapping keys to lists of strings. Returns a new dictionary with the same keys and values, except the strings in the values are all uppercase.
    '''
    upper_dict = {}
    for key in word_dict:
        upper_dict[key] = upper_list2(word_dict[key])
    return upper_dict



def main():

    str_lst = ['i', 'heart', 'freya!']
    print(upper_list(str_lst)) # returns None
    print(str_lst)
    print('*' * 25)

    str_lst = ['i', 'heart', 'freya!']
    print(upper_list2(str_lst)) # returns new uppercase list
    print(str_lst) # remains unchanged
    print('*' * 25)

    str_lst = ['i', 'heart', 'freya!']
    str_lst2 = ['i', 'heart', 'rocket!']
    word_dict = {1: str_lst, 2: ['red', 'rocket']}
    dict2 = {1: str_lst2, 2: ['red', 'rocket']}

    print(upper_values(word_dict)) # None
    print(word_dict)
    print(str_lst)
    print('*' * 25)

    print(upper_values2(dict2)) # returns new dictionary
    print(dict2) # unchanged
    print(str_lst2)















if __name__ == '__main__':
    main()