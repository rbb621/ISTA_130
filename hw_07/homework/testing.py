import random

'''
Name: Ricky Berliant
Date: 10/16/2025
Section Leader: Sungjoon
Week 8: Homework 5 
Test File: test_pig.py
'''

#PSEUDOCODE
'''
1. Name simple dice game pig
2. Two players
3. Each begin at 0 and take turns
4. If a player rolls 2 or higher, add up the total amount equal to the dice rolled
5. Player has the option to choose if the person wants to roll again.
6. If player chooses yes, he/she will roll again. If no, then player ends the turn with the total amount
on the dice rolled
7. If player rolls a 1, turn ends and earns 0 points
8. Object of game is first player reach 50 points
'''


# Finished
def print_scores(player1, score1, player2, score2):
    print('\n' '--- SCORES\t' + player1 + ':', str(score1) + '\t' + player2 + ':', str(score2) + ' ---')
    
# Finished
def check_for_winner(name, score):
    if score >= 50:
        print('THE WINNER IS:', name + '!!!!!')
        return True
    else:
        return False
        

# Finshed 
def roll_again(player_name):
    while True:
        choice = input(f"Roll again, {player_name}? (Y/N) ")
        if choice == "Y" or choice == "y":
            return True
        elif choice == "N" or choice == "n":
            return False
        else:
            print(f'I don\'t understand: "{choice}". Please enter either "Y" or "N".')


def play_turn(player_name):
    print(f"---------- {player_name}'s turn ----------")
    
    player_score = 0

    while True:
        roll_dice = random.randint(1, 6)

        print(f"\t<<< {player_name} rolls a {roll_dice} >>>")
        
        if roll_dice == 1:
            print("\t!!! PIG! No points earned, sorry", player_name, "!!!")  
            input("(enter to continue)")
            return 0 
        
        player_score += roll_dice
        print("\tPoints:", player_score)
            
        if not roll_again(player_name):
            break

    return player_score
                

def main():
    
    # a) Print two blank lines
    print()
    print()

    # b) Title of Game
    print('Pig Dice')
    
    # c) Enter player 1's name
    name_1 = input('Enter name for player 1: ')
    
    # c) Enter player 2's name
    name_2 = input('Enter name for player 2: ')
    
    # d) Greeting message
    print('\tHello', name_1, 'and', name_2 + ', welcome to Pig Dice!')
    
    # f) Initialize the players’ scores to 0.
    player_1_score = 0
    player_2_score = 0


    # f) Print their scores using the print_scores function.
    print_scores(name_1, player_1_score, name_2, player_2_score)
    

    # g) Enter a while loop in which repeats the following steps:
    while True:
        player_1_score += play_turn(name_1) 
        print_scores(name_1, player_1_score, name_2, player_2_score)
        if check_for_winner(name_1, player_1_score):
            break

        player_2_score += play_turn(name_2)
        print_scores(name_1, player_1_score, name_2, player_2_score)
        if check_for_winner(name_2, player_2_score):
            break
        
        if check_for_winner(name_1, player_1_score) or check_for_winner(name_2, player_2_score):
            break
        

if __name__ == "__main__":
    main()