'''
Name: Ricky Berliant
Date: 11/5/2025
Section Leader: Sungjoon Shin (SL)
Homework: Extra Credit Dictionaries
'''

'''
ISTA 130 Dictionaries Worksheet

Write code creating a dictionary called state_caps that maps 'AZ' to 'Phoenix', 'CA' to
'Sacramento', and 'DE' to 'Dover' in two ways. 

First, create an empty dictionary and
add each key-value pair individually. Second, create the whole thing in one statement with a
dictionary literal. Finally, add the key value pair 'ID': 'Boise'.
'''

'''
Write a function called lists_2_dict that takes two lists of the same length. 

Return a dictionary that maps each element in the first list to the corresponding element in the second list.
If there are duplicate keys in the first list, overwrite the previous key-value pair in the dictionary.
Given that the following code has been executed:
bird_weights = {}
bird_weights['Yellow Warbler'] = [18.5, 22.3]
bird_weights['Curve-billed Thrasher'] = []

As an ornithologist in the field, you weigh a Curve-billed Thrasher that you catch in your mist
net. It weighs 27.0. Write a line of code to add this weight to the dictionary. First, how do you
access the appropriate list? Then, how do you add this value to it?

Write one line of code that returns the number of Yellow Warblers that you have weighed.
You catch a Western Bluebird and it weighs 45.2. Write a line of code to incorporate this
information into your dictionary.
'''


def main():
    state_caps('AZ', 'CA', 'DE')
    lists_2_dict()
    

if __name__ == '__main__':
    main()