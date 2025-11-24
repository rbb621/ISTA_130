'''
Name: Ricky Berliant
Section Leader: Sungjoon Shin
Date: 12/10/2025
Class: ISTA 130
Homework: Homework Assignment #10
'''

import random

#*********************************
#           FIGHTER
#*********************************

class Fighter:
    
    # __init__ function
    def __init__(self, name):
        self.name = name
        self.hit_points = 10
        return None

    # __repr__ function
    def __repr__(self):
        output = self.name + " (HP: " + str(self.hit_points) + ")"
        return output

    # Take Damage Function
    def take_damage(self, damage_amount):
        self.hit_points -= damage_amount 
        
        if self.hit_points <= 0:
            print('\tAlas,', self.name, 'has fallen!')
        else:
            print('\t' + self.name, 'has', self.hit_points, 'hit points remaining.')            
        return None
    
    # Attack Function
    def attack(self, opponent):
        print(self.name + ' attacks ' + opponent.name + "!")
        
        accuracy = random.randrange(1, 20)
        
        if accuracy >= 12:
            attack_dmg = random.randrange(1, 12)
            print('\tHits for', attack_dmg, 'hit points!')
            opponent.take_damage(attack_dmg)
        else:
            print('\tMisses!')
        
        return None


    def is_alive(self):

        if self.hit_points > 0:
            return True
        else:
            return False


def combat_round(hero, opponent):
    
    hero_roll = random.randrange(1, 6)
    opponent_roll = random.randrange(1, 6)
    
    # Both roll the same number
    if hero_roll == opponent_roll:
        print("Simultaneous!")
        hero.attack(opponent)
        if opponent.is_alive():
            opponent.attack(hero)
        elif hero.is_alive():
            hero.attack(opponent)
            
    # Hero gets higher number
    elif hero_roll > opponent_roll:
        hero.attack(opponent)
        if opponent.is_alive():
            opponent.attack(hero)
            
    # Opponent gets higher number
    elif opponent_roll > hero_roll:
        opponent.attack(hero)
        if hero.is_alive():
            hero.attack(opponent)
        
    # ii.) This function returns nothing.
    return None


#*********************************
#           MAIN
#*********************************



def main():
    

    #i.) Create two instances of the Fighter class.
    # The name of the first fighter must be Death_Mongrel; 
    # the second must be Hurt_then_Pain.
    fighter_one = Fighter('Death_Mongrel')
    fighter_two = Fighter('Hurt_then_Pain')
    round_number = 0 
    
    while fighter_one.is_alive() and fighter_two.is_alive():
        round_number += 1
        print('=================== ROUND', round_number, '===================')
        print(fighter_one)
        print(fighter_two)
        
        # Press Enter to Fight

        combat_round(fighter_one, fighter_two)
    
    # Battle is over
    print("The battle is over!")  
    print(fighter_one)
    print(fighter_two)

if __name__ == '__main__':
    main()