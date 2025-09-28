'''
Author: Dan Charbonneau
Date: Feb 10 2022
Class: ISTA 130
Section Leader: NA

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment
import random

# put all of your function definitions below this line and then delete this comment
def get_weapon():
    '''
    Returns a randomly generated weapon
    '''
    weapon_number = random.randint(1,4)
    if weapon_number == 1:
        return "Space Stone"
    if weapon_number == 2:
        return "Thor's Hammer"
    if weapon_number == 3:
        return "Photon Torpedo"
    if weapon_number == 4:
        return "Lava Bomb"
    
def face_off(p1_name, p2_name):
    '''
    Randomly select weapons for each player and have them face off. 
    The function will print which weapons were selected and which beat which


    Parameters: Player name 1, player name 2

    Return: Name of the winner
    '''
    p1s_weapon = get_weapon()
    p2s_weapon = get_weapon()
    # Space Stone > Thor's Hammer > Photon Torpedo > Lava Bomb
    if p1s_weapon == "Space Stone":
        if p2s_weapon == "Space Stone":
            print("Draw - Both players have", p1s_weapon)
            return None
        else:
            print(p1_name + "'s " + p1s_weapon + " beats " + p2_name + "'s " + p2s_weapon) 
            return p1_name 
    elif p1s_weapon == "Thor's Hammer":
        if p2s_weapon == "Space Stone":
            print(p2_name + "'s " + p2s_weapon + " beats " + p1_name + "'s " + p1s_weapon) 
            return p2_name
        elif p1s_weapon != p2s_weapon:
            print(p1_name + "'s " + p1s_weapon + " beats " + p2_name + "'s " + p2s_weapon) 
            return p1_name
        else:
            print("Draw - Both players have", p1s_weapon)
            return None
    elif p1s_weapon == "Photon Torpedo":
        if p2s_weapon == "Space Stone" or p2s_weapon == "Thor's Hammer":
            print(p2_name + "'s " + p2s_weapon + " beats " + p1_name + "'s " + p1s_weapon) 
            return p2_name
        elif p1s_weapon != p2s_weapon:
            print(p1_name + "'s " + p1s_weapon + " beats " + p2_name + "'s " + p2s_weapon) 
            return p1_name
        else:
            print("Draw - Both players have", p1s_weapon)
            return None
    elif p1s_weapon == "Lava Bomb":
        if p2s_weapon == "Lava Bomb":
            print("Draw - Both players have", p1s_weapon)
            return None
        else: 
            print(p2_name + "'s " + p2s_weapon + " beats " + p1_name + "'s " + p1s_weapon) 
            return p2_name


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    num_rounds_to_play = input("Enter number of rounds to play: ")
    p1_points = 0
    p2_points = 0
    
    for i in range(int(num_rounds_to_play)):
        battle_winner = face_off(player1, player2)
        if battle_winner == player1:
            p1_points += 1
        elif battle_winner == player2:
            p2_points += 1
        print(player1 + ": " + str(p1_points) + " vs. " + player2 + ": " + str(p2_points))
        input("Press enter to continue...")
    if p1_points > p2_points:
        print(player1 + " beats " + player2)
    elif p1_points < p2_points:
        print(player2 + " beats " + player1)
    else:
        print("it's a draw!")


if __name__ == '__main__':
    main()
