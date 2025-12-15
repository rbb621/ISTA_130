''' In-class examples. '''

# build a dictionary by adding key-value pairs one at a time.
state_caps = {}
state_caps['AZ'] = 'Phoenix'
state_caps['CA'] = 'Sacramento'
state_caps['DE'] = 'Dover'
print(state_caps)
print()

# create the same dictionary all at once with a dictionary literal.
state_caps = {'AZ': 'Phoenix', 'CA': 'Sacremento', 'DE': 'Dover'}
state_caps['ID'] = 'Boise'
print(state_caps)
print()

def lists_2_dict(lst1, lst2):
    '''
    This function takes two list arguments and returns a 
    dictionary.  The key value pairs are in the dictionary
    are the corresponding elements of the lists.  Duplicate
    keys overwrite the previous pairs.
    '''
    result = {}
    for i in range(len(lst1)):
        result[lst1[i]] = lst2[i]
    return result
    

bird_weights = {}
bird_weights['Yellow Warbler'] = [18.5, 22.3]
bird_weights['Curve-billed Thrasher'] = []

bird_weights['Curve-billed Thrasher'].append(27.0)

print('Number Yellow Warblers:', len(bird_weights['Yellow Warbler']))

bird_weights['Western Bluebird'] = [45.2]
    
print(bird_weights)    