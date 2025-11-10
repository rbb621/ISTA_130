

def get_keys(Spongebob_Squarepants_dict, value):
    spongebob_cast_list = []
    
    for key in Spongebob_Squarepants_dict:
        if value in Spongebob_Squarepants_dict[key]:
            spongebob_cast_list.append(key)
    return spongebob_cast_list

#==================================================================================

def find_keys(Spongebob_Squarepants_dict, value):
    if value in Spongebob_Squarepants_dict:
        print('That character is part of the show!')
        return value
    else:
        print('That character is not in the show!')
        return value
#==================================================================================
def main():

    Spongebob_Squarepants_dict = {
        'Spongebob': ['Krusty Krab', 'Frycook'],
        'Patrick': ['Lazy'],
        'Squidward': ['Krusty Krab', 'Cashier'],
        'Sandy Cheeks': ['Scientist'],
        'Plankton': ['Chum Bucket', 'Head Chef'],
        'Mr. Krabs': ['Krusty Krab', 'Manager'],
        'Mrs. Puff': ['Drivers Ed Teacher']
        }    
    

    print(find_keys(Spongebob_Squarepants_dict, 'Spongebob'))
    print(find_keys(Spongebob_Squarepants_dict, 'Bulldozer'))
    print(get_keys(Spongebob_Squarepants_dict, 'Krusty Krab'))



if __name__ == '__main__':
    main()

