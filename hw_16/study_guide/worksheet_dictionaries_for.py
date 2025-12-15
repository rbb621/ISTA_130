''' In-class exercises. '''

my_dict = {'chocolate': ['chip', 'cake']}
my_dict['chocolate'].append('ice cream')
sweet = 'strawberry'
if sweet in my_dict:
    my_dict[sweet].append('mousse')
else:
    my_dict[sweet] = ['mousse']
    
print(my_dict)

def get_keys(a_dict, value):
    '''
    This function takes a dictionary (a_dict) and a value and returns
    a list of all keys that map to that value.
    '''
    key_list = []
    for key in a_dict:
        if a_dict[key] == value:
            key_list.append(key)
    return key_list

d = {'a': 1, 'b': [], 'c': 3, 'd': []}
print(get_keys(d, []))
print(get_keys(d, 3))

def nintendo_keys(a_dict, value):
    '''
    This function takes a dictionary (a_dict) and a value and returns
    a list of all keys that map to that value.
    '''
    key_list = []
    for key in a_dict:
        if a_dict[key] == value:
            key_list.append(key)
    return key_list

d = {'mario': 1, 'link': [], 'pikachu': 3, 'donkey_kong': []}
print(get_keys(d, []))
print(get_keys(d, 3))
    
def pop_empty(a_dict):
    ''' 
    This function removes all key-value pairs from dictionary parameter
    a_dict where the key maps to the empty list.  It returns None.
    '''
    for key in get_keys(a_dict, []): # can't change dict while iterating over it
        a_dict.pop(key) # therefore, for key in adict won't work
            
d = {'a': 1, 'b': [], 'c': 3, 'd': []}
pop_empty(d)
print(d)
            
def reverse_dict_clear(forward):
    '''
    This function takes a dictionary (forward) and returns
    a reverse dictionary that maps old values to lists of
    old keys.
    '''
    backward = {}
    for old_key in forward:
        new_item = old_key # item in the list of old keys
        new_key = forward[old_key] # old value
        if new_key in backward:
            backward[new_key].append(new_item)
        else:
            backward[new_key] = [new_item]
    return backward

d = {'a': 1, 'b': 1, 'c': 3, 'd': 3, 'e': 1}
print(reverse_dict_clear(d))

def reverse_dict(forward):
    backward = {}
    for key in forward:
        if forward[key] in backward:
            backward[forward[key]].append(key)
        else:
            backward[forward[key]] = [key]
    return backward

d = {'a': 1, 'b': 1, 'c': 3, 'd': 3, 'e': 1}
print(reverse_dict(d))


            
