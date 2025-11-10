'''
Author: Jason Pototsky
Date: 11/11/2025
Class: ISTA 130
Section Leader: Davranbek Kadirimbetov

Description:
Dict Discussion — contains two functions:
1) find_key: checks if a key exists in a dictionary.
2) get_keys: returns all keys matching a given value.
'''

def find_key(d, key):
    """
    Return True if key is in dictionary d, otherwise False.
    """
    return key in d


def get_keys(d, value):
    """
    Return a list of all keys whose values include the given value.
    """
    result = []
    for k, v in d.items():
        if value in v:
            result.append(k)
    return result


if __name__ == "__main__":
    rick_dict = {
        'never': ['gonna', 'give', 'you', 'up'],
        'gonna': ['let', 'you', 'down'],
        'give': ['you', 'up'],
        'make': ['you', 'cry'],
        'say': ['goodbye'],
        'tell': ['a', 'lie'],
        'desert': ['you']
    }

    print("Testing find_key:")
    print(find_key(rick_dict, 'never'))
    print(find_key(rick_dict, 'Together Forever'))

    print("\nTesting get_keys:")
    print(get_keys(rick_dict, 'you'))       
    print(get_keys(rick_dict, 'lie'))       
    print(get_keys(rick_dict, 'dance'))     
