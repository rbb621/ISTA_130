'''
Kenneth Summers
Section Leader: Davranbek Kadirimbetov
Date: 08 November 2025
Week 12 Dictionaries Discussion Post
'''

def find_key(dictionary, key):
    '''
    Returns True if 'key' is a key in dictionary, and False otherwise.
    Returns
        bool 
            True if key is in the dictionary, False otherwise.
    '''
    return key in dictionary


def get_keys(dictionary, value):
    '''
    Returns a list of all keys in dictionary that maps to the given value.
    If the dictionary's values are containers like lists, tuples, or sets,
    this function will check whether 'value' is contained in that collection.
    Otherwise, it checks for simple equality.

    Returns
    list
        A list of keys whose associated value matches or contains 'value'.
    '''
    matching_keys = []
    for key, values in dictionary.items():
        #If the value is a list/tuple/set, look for membership.
        if isinstance(values, (list, tuple, set)):
            if value in values:
                matching_keys.append(key)
        else:
            if values == value:
                matching_keys.append(key)
    return matching_keys
