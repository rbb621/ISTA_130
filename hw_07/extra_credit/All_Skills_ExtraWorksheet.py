import random

'''
Name: Ricky Berliant
Date: 10/16/2025
Section Leader: Sungjoon
Week 7: Traversing Strings
File: traversing_strings.py
'''


'''

time = '5:30 pm'
date = "1009"
gain = 9
over = True


Expression                            Value                          Type

time [len (time) - 1] * 2            'mm'                       <class 'str'>        


(time + date) * 2                   '5:30 pm10095:30 pm1009'    <class 'str'>


int (date) < gain or not over       False                       <class 'bool'>


11.0 % gain                         2.0                        <class 'float'>


11.0 // gain                        1.0                        <class 'float'>


18 / gain                           2.0                        <class 'float'>


'''

def squares_string(num):
    result = ""
    i = 1
    while i <= num:
        square = i ** 2
        if i <= num:
            result += str(square) + ", "     
        else:
            result += str(square)
        i += 1
    return result   

def squares_string(num):
    result = ""
    for i in range(1, num, + 1):
        square = i ** 2
        if i < num:
            result += str(square) + ", "
        else:
            result += str(square)
    return result



def oldest(name1, age1, name2, age2, name3, age3):

    if age1 > age2 and age1 > age3:  
        return name1
    elif age2 > age1 and age2 > age3:
        return name2
    else:
        return name3

def second_to_last_chars():
    result = ""
    while True:
        user_input = input('Enter a word: ')
        if user_input == "": 
            break 
        else:
            result += user_input[-2]
    return result


def roulette(balance):
    bonus = 35
    odd_even_bonus = 1
        
    while True:
        # Place the bet
        amount_bet = int(input("Enter the amount bet Balance: $" + str(balance) + ": "))
         
        if amount_bet > balance:
            print("Insufficient Funds.")
            continue
        elif amount_bet <= 0:
            print("Bet must be greater than 0")
            continue
        
        # Player’s guess
        guess_number = input("Pick a number (0-36), '00', 'odd', or 'even': ")
        roulette_number = random.randint(0, 37)
        
        if roulette_number == 37:
            displayed_number = "00"
        else:
            displayed_number = str(roulette_number)

        # Exact number guess
        if guess_number.isdigit() and 0 <= int(guess_number) <= 36:
            if int(guess_number) == roulette_number:
                balance = bonus_prize(balance, bonus, amount_bet, displayed_number)
            else:
                balance = profit_loss(balance, amount_bet, displayed_number)

        # 00 Guess
        elif guess_number == '00':
            if roulette_number == 37:
                balance = bonus_prize(balance, bonus, amount_bet, displayed_number)
            else:
                balance = profit_loss(balance, amount_bet, displayed_number)

        # Odd Guess
        elif guess_number == 'odd':
            if roulette_number == 0 or roulette_number == 37:
                balance = bonus_prize(balance, amount_bet, displayed_number)
            elif roulette_number % 2 == 1:
                balance = bonus_prize(balance, odd_even_bonus, amount_bet, displayed_number)
            else:
                balance = profit_loss(balance, amount_bet, displayed_number)

        # Even Guess
        elif guess_number == 'even':
            if roulette_number == 0 or roulette_number == 37:
                balance = bonus_prize(balance, bonus, amount_bet, displayed_number)
            elif roulette_number % 2 == 0:
                balance = bonus_prize(balance, odd_even_bonus, amount_bet, displayed_number)
            else:
                balance = profit_loss(balance, amount_bet, displayed_number)
        
        # Game Over
        if balance <= 0:
            print("Game over")
            break
            
        while True:
            option = input("Would you like to continue? (Y/N): ")
            if option == "Y" or option == "y":
                break
            elif option == "N" or option == "n":
                return balance
            else:
                print("Invalid option")
        
        print("Your balance is now $", balance)

def bonus_prize(balance, bonus, amount_bet, roulette_number):
    print("The outcome is:", roulette_number)
    winnings = bonus * amount_bet
    balance += winnings
    print("You won $", winnings)
    print("Your balance now is $", balance)
    return balance
    
def profit_loss(balance, amount_bet, roulette_number):
    print("Sorry, the number it printed out is:", roulette_number)
    balance -= amount_bet
    print("You lost $", amount_bet)
    print("Your balance now is $", balance)
    return balance   

def main():
    print(squares_string(5))
    print(oldest('Ricky', 37, 'Max', 35, 'Andy', 31))
    print(second_to_last_chars())
    print(roulette(200))
    
if __name__ == '__main__':
    main()
