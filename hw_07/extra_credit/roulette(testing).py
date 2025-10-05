import random

def roulette(balance):
    bonus = 35
        
    while True:
        # Place the bet
        amount_bet = int(input(f"Enter the amount bet ${balance}: "))
         
        if amount_bet > balance:
            print("Insuffienct Funds.")
            continue
        elif amount_bet <= 0:
            print("Bet must be greater than 0")
            continue
        
        # Have the player enter the number, or odd or even
        guess_number = input("Pick a number (0-36), '00', 'odd', or 'even': ")
        roulette_number = random.randint(0, 37)

        # Convert 37 to '00' for display
        if roulette_number == 37:
            displayed_number = "00"
        else:
            displayed_number = str(roulette_number)

        # Exact number bet
        if guess_number.isdigit() and 0 <= int(guess_number) <= 36:
            if int(guess_number) == roulette_number:
                print("The number that came up is:", displayed_number)
                balance = bonus_prize(balance, bonus, amount_bet)
            else:
                print("Sorry, the number that came up is:", displayed_number)
                balance = profit_loss(balance, amount_bet)

        # '00' bet
        elif guess_number == '00' and roulette_number == 37:
            print("The number that came up is:", displayed_number)
            balance = bonus_prize(balance, bonus, amount_bet)

        # Odd Guess
        elif guess_number == 'odd':
            if roulette_number in (0, 37):
                print("The number that came up is:", displayed_number)
                print("House number — no odd/even win.")
                balance = profit_loss(balance, amount_bet)
            else:
                if roulette_number % 2 == 1:
                    print("The outcome is:", displayed_number, "(odd)")
                    balance = bonus_prize(balance, 1, amount_bet)
                else:
                    print("Sorry, the number that came up is:", displayed_number)
                    balance = profit_loss(balance, amount_bet)
    
        # Even Guess
        elif guess_number == 'even':
            if roulette_number in (0, 37):
                print("The number that came up is:", displayed_number)
                print("House number — no odd/even win.")
                balance = profit_loss(balance, amount_bet)
            else:
                if roulette_number % 2 == 0:
                    print("The outcome is:", displayed_number, "(even)")
                    balance = bonus_prize(balance, 1, amount_bet)
                else:
                    print("Sorry, the number that came up is:", displayed_number)
                    balance = profit_loss(balance, amount_bet)

        else:
            print("Invalid bet type.")
            continue
        
        if balance <= 0:
            print("Game over")
            break
            
        # Continue Playing Prompt?
        while True:
            option = input("Would you like to continue? (Y/N): ")
            if option.lower() == "y":
                break
            elif option.lower() == "n":
                return balance
            else:
                print("Invalid option")
        
        print(f"Your balance is now ${balance}")


# Add from the bet 
def bonus_prize(balance, bonus, amount_bet):
    winnings = bonus * amount_bet
    balance += winnings
    print(f"You won ${winnings}!")
    print(f"Your balance now is ${balance}")
    return balance
    
# Subtract from the bet
def profit_loss(balance, amount_bet):
    balance -= amount_bet
    print(f"You lost ${amount_bet}")
    print(f"Your balance now is ${balance}")
    return balance

def main():
    print(roulette(200))
    
    
if __name__ == '__main__':
    main()
