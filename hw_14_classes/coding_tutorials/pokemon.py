import random

class Pokemon:
    
    def __init__(self, pkmn_name, type, ability, stage, moves):
        self.pkmn_name = pkmn_name
        self.type = type
        self.ability = ability
        self.stage = stage
        self.moves = moves
        return None
    
    def __repr__(self):
        pokedex = "\nThis Pokémon is " + self.pkmn_name + ".\n"
        pokedex += self.pkmn_name + "'s type is " + self.type + ".\n"
        pokedex += "Ability: " + self.ability + "\n"
        pokedex += self.pkmn_name + " is a " + self.stage + "-stage Pokémon.\n"
        pokedex += self.pkmn_name + "'s moveset:\n"
        
        for move_set in self.moves:
            pokedex += "- " + move_set + "\n"
            
        return pokedex
    
    def choose_move(self):
        return self.moves[random.randrange(len(self.moves))]


def main():
    Pikachu = Pokemon(
        'Pikachu',
        'Electric',
        'Static',
        'Basic',
        ['Thunderbolt', 'Iron Tail', 'Agility', 'Quick Attack']
    )
    print(Pikachu)
    print(Pikachu.pkmn_name + ' used ' + Pikachu.choose_move() + '!')

    
if __name__ == '__main__':
    main()


    # print(Pikachu.pkmn_name, Pikachu.type, Pikachu.ability, Pikachu.stage, Pikachu.moves)
    # print('Pokemon Name:', Pikachu.pkmn_name)
    # print('Type:', Pikachu.type)
    # print('Ability', Pikachu.ability)
    # print('Stage:', Pikachu.stage)
    # print('Moves:', Pikachu.moves)
    # print(type(Pikachu))