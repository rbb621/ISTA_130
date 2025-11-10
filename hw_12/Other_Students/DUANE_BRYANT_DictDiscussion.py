"""
Author: Duane Bryant
Date: Nov 10, 2025
Class: ISTA 130
Section Leader: Sungjoon

Description:
Dictionaries Discussion post assignment, week 12

"""


'''Write a function called find_key that takes a dictionary and a key as arguments.
It returns True if that key is in the dictionary and False otherwise.'''
def find_key(d, key):
    return key in d
print(find_key(flavors, 'milk'))     #Not sweet.....False

'''Write a function called get_keys that takes a dictionary and a value as arguments.
It returns a list of every key that maps to the given value.'''
def get_keys(d, value): 
    result = []
    for k, v in d.items():
        if value in v:
            result.append(k)
    return result
print(get_keys(flavors, 'sweet'))     #should spit out candy, coffee etc

'''given this dictionary called flavors, you would want to check if milk is a key in it.
Because the only keys are candy, coffee and water, your function would return False.
flavors = {'candy' : ['sweet'], 'coffee' : ['bitter', 'sweet'], 'water' : ['plain']}'''
flavors = {'candy': ['sweet'], 'coffee': ['bitter', 'sweet'], 'water': ['plain']}

