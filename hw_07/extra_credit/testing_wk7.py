import random

def roulette(balance):
    bonus = 35
        
    while True:
        # Place the bet
        amount_bet = int(input(f"Enter the amount bet {balance}: "))
         
        if amount_bet > balance:
            print("Insuffienct Funds.")
            continue
        elif amount_bet <= 0:
            print("Bet must be greater than 0")
            continue
        
        # Have the player enter the number, or odd or even
        guess_number = int(input("Pick a number (0-36), '00', 'odd', or 'even': "))
        roulette_number = random.randint(1, 5)

        if int(guess_number) >= 0 and int(guess_number) <= 36:
            if int(guess_number) == roulette_number:
                balance += bonus * amount_bet
                print("The number is prints out is:", roulette_number)
                print(f"You won ${bonus * amount_bet}!")
                print(f"Your balance now is ${balance}")
            else:
                print("Sorry, the number it printed out is:", roulette_number)
                balance -= amount_bet
                print(f"You lost ${amount_bet}")
                print(f"Your balance now is ${balance}")

                
        elif str(guess_number) == '00' and roulette_number == 37:
            print("The number is prints out is:", roulette_number)
            balance += bonus * amount_bet
            print(f"You won ${bonus * amount_bet}!")
            print(f"Your balance now is ${balance}")

        # Odd Guess
        elif str(guess_number) == 'odd':
            if roulette_number not in (0, 37) and roulette_number % 2 == 1:
                print('The outcome is:', str(guess_number))
                balance += bonus * amount_bet
                print(f"You won ${bonus * amount_bet}!")
                print(f"Your balance now is ${balance}")
            else:
                print("Sorry, the number it printed out is:", roulette_number)
                balance -= amount_bet
                print(f"You lost ${amount_bet}")
                print(f"Your balance now is ${balance}")
    
        # Even Guess
        elif str(guess_number) == 'even':
            if roulette_number not in (0, 37) and roulette_number % 2 == 0:
                print('The outcome is:', str(guess_number))
                balance += bonus * amount_bet
                print(f"You won ${bonus * amount_bet}!")
                print(f"Your balance now is ${balance}")
            else:
                print("Sorry, the number it printed out is:", roulette_number)
                balance -= amount_bet
                print(f"You lost ${amount_bet}")
                print(f"Your balance now is ${balance}")
        else:
            print("Invalid bet type")
            continue
        
        if balance <= 0:
            print("Game over")
            break
            
        # Continue Playing Prompt?
        while True:
            option = input(f"Would you like to continue? (Y/N): ")
            if option == "Y" or option == 'y':
                break
            elif option == "N" or option == 'n':
                return balance
            else:
                print("Invalid option")
        
        print(f"Your balance is now ${balance}")

def main():
    final_balance = roulette(200)
    
    print(f"Your final balance before exiting is ${final_balance}")


if __name__ == '__main__':
    main()