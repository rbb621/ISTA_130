

'''
Write a function called upper list that takes a list of strings as its sole argument
and converts them all to uppercase. The function should alter the original list and return
None.
'''

def upper_list(string):
    for i in range(len(string)):
        string[i] = string[i].upper()
    return None


'''
Write a function called upper list 2 that takes a list of strings as its sole argument.
It returns a new list containing all of the strings from the original list in uppercase. The
function should NOT alter the original list.
'''


def upper_list_2(string):
    new_list = []
    for i in string:
        new_list.append(i.upper())
    return new_list
    

'''
Write a function called upper_values that takes a dictionary as its sole argument. 
This dictionary maps keys, which may be any immutable object, to values, which are lists of
strings. 

The function converts all of the strings in all of the lists to uppercase (ie the
dictionary values). 

It should alter the original lists. What should the function return? 
You may call the previous functions in your code. 

You should start by drawing a picture of the dictionary so its structure 
is clear in your mind.
'''

def upper_values(my_dict):
    for key in my_dict:
        upper_list(my_dict[key]) 
    return my_dict



'''
Write a function called upper values2 that takes a dictionary as its sole argument. 

This dictionary maps keys, which may be any immutable object, to values, which are lists of
strings. It returns a new dictionary. 

The new dictionary is identical to the original dictionary except that all of the strings in all of the lists are 
in uppercase (ie the dictionary values). The function should NOT alter the original dictionary. 
You may call the previous functions in your code.
'''

def upper_values_2(my_dict):
    new_dict = {}
    for key in my_dict:
        new_dict[key] = upper_list_2(my_dict[key])
    return my_dict
    
    
def main():
    
    my_dict = {
        'charmander': ['fire'], 
        'squirtle': ['water'],
        'bulbasaur': ['grass']
    }

    # Modify in-place
    original_dict = upper_values(my_dict)

    # Create new uppercase dictionary
    upper_values_cap = upper_values_2(my_dict)

    types = ['fire', 'water', 'grass']
    upper_types = upper_list_2(types)

    print()
    print('Original list:', types)
    print()
    print('Uppercase list:', upper_types)
    print()
    print('Dictionary after upper_values (modified):', original_dict)
    print()
    print('Dictionary returned by upper_values_2 (new):', upper_values_cap)

    



if __name__ == '__main__':
    main()
    


