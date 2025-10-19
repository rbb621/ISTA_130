'''
Author: Rich
Date: Today
Class: ISTA 130
Section Leader: Me

Description:
Functions and code that are solutions to today's worksheet.
'''

def squares_string(n):
    '''
    This function takes a positive integer argument. It returns 
    a string representing the squares of all of the numbers 
    between 1 and the argument, inclusive, each pair separated
    by a comma and a space. 
    '''
    result = str(1)
    for i in range(n - 1):
        result += ', ' + str((i + 2) ** 2)
    return result
            
def squares_string_while(n):
    ''' While loop. '''
    result = str(1)
    i = 0
    while i < n - 1:
        result += ', ' + str((i + 2) ** 2)
        i += 1
    return result
            
def oldest(name1, age1, name2, age2, name3, age3):
    '''
    oldest takes 3 pairs of  parameters (6 total).
    Each pair represents a person's name (str) and age (int).
    Return the name of the oldest person.
    '''
    if age1 >= age2 and age1 >= age3:
        return name1
    elif age2 >= age1 and age2 >= age3:
        return name2
    else:
        return name3
        
def price_of_rocks():
    '''
    This function has no parameters. In a while loop, it gets a rock 
    type and a weight from the user. It keeps a running total of the 
    price for all requested rocks. Repeat until the user wants 
    to quit by not entering a rock type or weight. Quartz 
    crystals cost $23 per pound. Garnets cost 
    $160 per pound. Meteorite costs $15.50 per gram. Return the 
    total price of all of the material.
    '''
    total = 0
    while True:
        kind = input('Enter rock type: ')
        wt = input('Enter weight you wish to purchase: ')
        if kind == 'quartz':
            total += float(wt) * 23
        elif kind == 'garnet':
            total += float(wt) * 160
        elif kind == 'meteorite':
            total += float(wt) * 15.5 # this assumes user entering wt in gms
            # total += float(wt) * 454 * 15.5 # this assumes user entering wt in lbs
        else:
            break
    return total

def second_to_last_chars():
    '''
    This function builds and returns a string from 
    strings entered by the user.  The new string consists of
    the second-to-last characters of the user strings.
    '''
    cat = ''
    string = input('Enter string or return to quit: ')
    while string:
        cat += string[len(string) - 2]
        string = input('Enter next string or return to quit: ')
    return cat
    
def roulette(max_bet):
    '''
    This function simulates playing roulette, except that 
    betting on red/black is replaced by betting on odd/even.  The maximum
    bet allowed is float/int max_bet.  It returns the 
    user's net gain/loss when his/her turn ends.
    '''
    total = 0
    while True:
        amt = int(input('Enter your bet amount (max = ' + str(max_bet) + '): '))
        bet = input('Bet a number or odd/even: ')
        spin = random.randint(0, 37)
        if spin == 37:
            print("The ball lands on 00!")
        else:
            print("The ball lands on", str(spin) + '!')
        if bet == 'odd':
            if spin == 0 or spin == 37 or spin % 2 == 0:
                total -= amt
            else:
                total += amt
        elif bet == 'even':
            if spin == 0 or spin == 37 or spin % 2 == 1:
                total -= amt
            else:
                total += amt
        else:
            if bet == '00' and spin == 37 or bet != '00' and int(bet) == spin:
                total += 35 * amt
            else:
                total -= amt
        print('Your total is $' + str(total))
        more = input("Keep playing (y or n): ")
        if more == 'N' or more == 'n':
            return total
            
#==========================================================
def main():
    '''
    Test the solutions to the worksheet.
    '''
    time = '5:30 pm'
    date = "1009" 
    gain = 9
    over = True 
    
    print('time:', time)
    print('date:', date)
    print('gain:', gain)
    print('over:', over)
    print('-' * 40)

    print('time[len(time) - 1] * 2:')
    print(time[len(time) - 1] * 2, ' --- ', type(time[len(time) - 1] * 2))
    print('(time + date) * 2:')
    print((time + date) * 2, ' --- ', type((time + date) * 2))
    print('int(date) < gain or not over:')
    print(int(date) < gain or not over, ' --- ', type(int(date) < gain or not over))
    print('11.0 % gain:')
    print(11.0 % gain, ' --- ', type(11.0 % gain))
    print('11.0 // gain:')
    print(11.0 // gain, ' --- ', type(11.0 // gain))
    print('18 / gain:')
    print(18 / gain, ' --- ', type(18 / gain))
    print('18 // 2 * gain:')
    print(18 // 2 * gain, ' --- ', type(18 // 2 * gain))
    print("time[1] + '-' * 3 + date[3]:")
    print(time[1] + '-' * 3 + date[3], ' --- ', type(time[1] + '-' * 3 + date[3]))
    print("date + '-' + str(gain):")
    print(date + '-' + str(gain), ' --- ', type(date + '-' + str(gain)))
    
    print('\n' + '-' * 40 + '\n')
    
    print('squares_string(4):', squares_string(4))
    print('squares_string(9):', squares_string(9))
    print('squares_string(1):', squares_string(1))
    print('squares_string_while(4):', squares_string_while(4))
    print('squares_string_while(9):', squares_string_while(9))
    print('squares_string_while(1):', squares_string_while(1))
    
    print('\n' + '-' * 40 + '\n')
    
    print('Should be "Treebeard":', oldest('Treebeard', 2500, 'Gandalf', 1625, 'me', 56))
    
    print('\n' + '-' * 40 + '\n')
    
    print(price_of_rocks())
    
    print('\n' + '-' * 40 + '\n')
    
    print(second_to_last_chars())

    print('\n' + '-' * 40 + '\n')
    
    print(roulette(25))


if __name__ == '__main__':
    main()
