import random

# def pants_fitter():
#     name = input("Enter your name: ")
#     print("Greetings", name, 'welcome to Pants-R-Us')
    
#     waist_size = float(input("Enter your waist size in inches: "))
#     pairs_of_pants = int(input("How many pairs of pants would you like: "))
#     fashion_choice = input("Would you like regular or fancy pants? ")
     
#     regular_pants = 40
#     fancy_pants = 100
#     if waist_size >= 34:
#         return 'large'
#     elif waist_size >= 30:
#         return 'medium'
#     elif waist_size < 30:
#         return 'small' 
    
#     if fashion_choice == 'fancy':
#         price = pairs_of_pants * fancy_pants
#     else:
#         price = pairs_of_pants * regular_pants
        
#     print(pairs_of_pants, 'pairs of', waist_size, fashion_choice, 'pants: $', price)

#     return None


# def digdug(number):
#     for i in range(1, number + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print(i, ': digdug')
#         elif i % 3 == 0:
#             print(i, ': dig')
#         elif i % 5 == 0:
#             print(i, ': dug')


# def species_height(species, inches):

#     if species == 'Human':
#         average = 67
#         if inches > average:
#             print("Above Average")
#         elif inches < average:
#             print("Below Average")
#         else:
#             print("Average")
            
#     if species == 'Klingon':
#         average = 71
#         if inches > average:
#             print("Above Average")
#         elif inches < average:
#             print("Below Average")
#         else:
#             print("Average")


# def sooner_date(month_num_01, day_num_01, month_num_02, day_num_02):
        
#         # August 4th ---> Sepember          
#         if month_num_01 < month_num_02:
#                 if day_num_01 < day_num_02:
#                     print(month_num_01, "/", day_num_01)
#         elif month_num_02 < month_num_01:
#             if day_num_02 < day_num_01:
#                 print(month_num_02, "/", day_num_02)  
#         elif month_num_02 == month_num_01 and day_num_01 == day_num_02:
#             print(month_num_02, "/", day_num_02)



# Write a function called sooner_date that has 4 integer parameters. The first is a number
# between 1 and 12 (inclusive) that represents a month. 1 is January, 2 is February, etc. 
# The second is a number between 1 and 31 (inclusive) that represents a day. 
# The third parameter is another integer representing a month and the fourth is another integer parameter representing
# a day. So essentially you have 2 dates (the first 2 parameters and the second 2 parameters).

# Figure out which date would come sooner, then print out that date in the format month / day.
# Here are some examples of calling the function with different arguments. (The code executed is
# in blue, the output produced is in green):
# sooner_date(1, 1, 1, 2)
# 1 / 1
# sooner_date(2, 5, 1, 3)
# 1 / 3
# sooner_date(8, 25, 7, 30)
# 7 / 30


def roulette(balance):
    roulette_number = random.randint(1, 1)
    bonus = 35
    
    while True:
        amount_bet = int(input(f"Enter the amount bet {balance}: ")) 
        guess_number = input("Pick a number (0-36), '00', 'odd', or 'even': ")
        if int(guess_number) == roulette_number:
            balance += bonus * amount_bet
            print(f"You won ${balance}!")
            print(f"Your balance now is ${balance}")
            
            if amount_bet > balance:
                print("Insuffienct Funds.")
                continue
            elif amount_bet <= 0:
                print("Bet must be greater than 0")
                continue
            elif balance < 0:
                print("Game over!")
            else:
                balance -= amount_bet


        # Yes or No
        option = input(f"Would you like to continue? (Y/N): ")
        if option == "Y" or option == 'y':
            continue
        elif option == "N" or option == 'n':
            return balance
        else:
            print("Invalid option")


def main():
    # digdug(15)
    # species_height("Human", 72)
    # print(sooner_date(4, 2, 3, 12))
    print(roulette(200))

    

if __name__ == '__main__':
    main()