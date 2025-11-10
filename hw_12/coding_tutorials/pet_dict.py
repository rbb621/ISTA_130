'''
Author: <your name>
Date: <the date>
Class: ISTA 130
Section Leader: <your section leader>

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment
def pet_dict_builder():
    pet_dict = {}
    
    while True:
        user_input = input('Please enter your pet name and type... or enter \"q\" to quit ')
        if user_input.lower() == 'q':
            return pet_dict 
        else:
            user_input_split = user_input.split()
            pet_name = user_input_split[0]
            pet_type = user_input_split[1].lower()
            if pet_type in pet_dict:
                pet_dict[pet_type].append(pet_name)
            else:
                pet_dict[pet_type] = [pet_name]

# put all of your function definitions below this line and then delete this comment



#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    pet_dictionary = pet_dict_builder()
    print(pet_dictionary)



if __name__ == '__main__':
    main()
