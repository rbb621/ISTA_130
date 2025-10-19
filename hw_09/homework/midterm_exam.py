import random 

def mystery_number():
    
    #Number Range
    lowest_number = 1
    highest_number = 12
    
    #Guessing the number
    secret_number = random.randint(lowest_number, highest_number)

    #Enter the name
    player_1 = input('Player 1: ')
    player_2 = input('Player 2: ')
    
    while True:
        
        # Player 1's turn
        guess_number = int(input('Your turn to guess, ' + player_1 + '. Enter your guess here: '))
        if guess_number == secret_number:
            print(player_1, 'Wins!!!')
            print('(press enter to continue)')
            input()
            break
        else:
            print('No,', guess_number, 'is not the mystery number.' )

        # Player 2's turn
        guess_number = int(input('Your turn to guess, ' + player_2 + '. Enter your guess here: '))
        if guess_number == secret_number:
            print(player_2, 'Wins!!!')
            print("(press enter to continue)")
            input()
            break
        else:
            print('No,', guess_number, 'is not the mystery number.' )



def find_month(exact_date):
    
    # Show the month part
    month_num = int(exact_date[:2])
    
    if month_num == 1:
        return "January"
    elif month_num == 2:
        return "February"
    elif month_num == 3:
        return "March"
    elif month_num == 4:
        return "April"
    elif month_num == 5:
        return "May"
    elif month_num == 6:
        return "June"
    elif month_num == 7:
        return "July"
    elif month_num == 8:
        return "August"
    elif month_num == 9:
        return "September"
    elif month_num == 10:
        return "October"
    elif month_num == 11:
        return "November"
    elif month_num == 12:
        return "December"
    
def find_day(exact_date):
    
    # Print out the exact date of the month
    day_num = int(exact_date[3:5])
    return day_num


def main():
    exact_month = '01/10/2025'
    exact_day = '10/06/2025'
    mystery_number()
    print(find_month(exact_month))
    print(find_day(exact_day))
    

if __name__ == '__main__':
    main()