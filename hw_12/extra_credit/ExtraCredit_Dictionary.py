'''
Name: Ricky Berliant
Date: 11/14/2025
Section Leader: Sungjoon Shin (SL)
Homework: Extra Credit Traversing Dictionaries Worksheet
Class: ISTA 130
'''

'''
ISTA 130 Traversing Dictionaries Worksheet
Write a function called pop_empty. This function takes a dictionary as an argument. It
traverses the dictionary, popping (removing) any key-value pair where the value is the empty list.
Do NOT alter the dictionary as you traverse it.
'''


# Pop Empty Function
def pop_empty(anime_dictionary):

    anime_shows_to_remove = []
    for key in anime_dictionary:
        if anime_dictionary[key] == []:
            anime_shows_to_remove.append(key)

    for key in anime_shows_to_remove:
        anime_dictionary.pop(key)

    return anime_dictionary
    


# Reverse Dict Function
def reverse_dict(original_dict):
    reversal_dict = {}
    
    for key, values in original_dict.items():
        
        for value in values:
            if value not in reversal_dict:
                reversal_dict[value] == []
            reversal_dict[value].append(key)
        
    return reversal_dict
    
    

#==================================================================================

def main():
    anime_dictionary = {
        'Hunter x Hunter': ['Shonun'],
        'Demon Slayer': ['Shonun'],
        'Empty Show': []
        }

    print(pop_empty(anime_dictionary))
    print(reverse_dict(anime_dictionary))
    

if __name__ == '__main__':
    main()