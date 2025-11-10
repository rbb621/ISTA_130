
def pkmn_dictionary_build():
    pkmn_dict = {}
    
    while True:
        user_input = input('Enter a Pokémon name, type, and stage (or "q" to quit): ')
        
        if user_input.lower() == 'q':
            return pkmn_dict
        else:
            # Split the input into three parts
            user_input_split = user_input.split()
            
            # Safety check: Make sure the user entered 3 parts
            if len(user_input_split) != 3:
                print("Please enter Pokémon name, type, and stage separated by spaces.")
                continue
            
            pkmn_name = user_input_split[0].capitalize()
            pkmn_type = user_input_split[1].capitalize()
            pkmn_stage = user_input_split[2].capitalize()
        
            if pkmn_type == "/":
                dual_type = pkmn_type.split("/")
                dual_type = dual_type.capitalize()
            
            # Add to dictionary
            if pkmn_name in pkmn_dict:
                pkmn_dict[pkmn_name].append(pkmn_type, pkmn_stage)
            else:
                pkmn_dict[pkmn_name] = [pkmn_type, pkmn_stage]

                


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    pokedex = pkmn_dictionary_build()
    print(pokedex)


if __name__ == '__main__':
    main()
