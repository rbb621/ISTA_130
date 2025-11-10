'''
Name: Ricky Berliant
Date: 11/14/2025
Section Leader: Sungjoon Shin (SL)
Homework: Dictionary Discussion
Class: ISTA 130
'''

#==================================================================================
# FIND KEYS FUNCTION

def find_key(flavor_dict, value):
    if value in flavor_dict:
        return True
    else:
        return False
    

#==================================================================================
# GET KEYS FUNCTION

def get_keys(flavor_dict, value):
    result = []
    for key in flavor_dict:
        if value in flavor_dict[key]:
            result.append(key)
    return result

#==================================================================================

def main():
    flavor_dict = {
        'candy': ['sweet'],
        'coffee': ['bitter', 'sweet'],
        'water': ['plain']
    }    
    
    #Find Key
    print(find_key(flavor_dict, 'sweet'))
    print(find_key(flavor_dict, 'plain'))
    
    # Get Keys
    print(get_keys(flavor_dict, 'sweet'))
    

if __name__ == '__main__':
    main()