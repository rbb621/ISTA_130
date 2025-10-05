'''
IN CLASS EXAMPLE
'''

import random

def practice_odd_even():
    done = False
    correct = 0
    wrong = 0
    while not done:
        number = random.randint(0,100)
        valid_guess = False
        while not valid_guess:
            print('Number:', number)
            guess = input('Odd or Even? (enter O for odd, E for even): ')
            if guess == 'O' or guess == 'E':
                valid_guess = True
            else:
                print('\nInvalid entry:', guess)

        evaluate_odd_even(number, guess)
        done = not guess_another()
    return None

def evaluate_odd_even(number, guess):
    correct = False
    if number % 2 == 0:
        answer = 'E'
        long_answer = 'even'
    else:
        answer = 'O'
        long_answer = 'odd'

    output = str(number) + ' is ' + long_answer
    if guess == answer:
        print('Yes!', output, '!')
        correct = True
    else:
        print('Sorry,', output)
    return correct

def practice_multiplication():
    done = False
    while not done:
        a = random.randint(0,12)
        b = random.randint(0,12)
        print('Problem:', a, '*', b)
        guess = input('Enter your answer: ')
        output = str(a) + ' * ' + str(b)  + ' is ' + str(a * b)
        if int(guess) == (a * b):
            print('Correct!', a, '*', b, 'is', (a * b))
        else:
            print('Sorry,', a, '*', b, 'is', (a * b))

        done = not guess_another()
    return

# def show_answer(correct, question, answer, correct_answer):
#     if correct:
#         print 'Yes! ' + question + ' is ' + answer
#     else:
#         print 'Sorry, ' + question + ' is ' + correct_answer

def guess_another():
    valid_entry = False
    while not valid_entry:
        again = input('\nGuess another? (Y/N) ')
        if again == 'N' or again == 'n':
            valid_entry = True
            keep_guessing = False
        elif again == 'Y' or again == 'y':
            valid_entry = True
            keep_guessing = True
        else:
            print('\nInvalid entry:', again)
    return keep_guessing

#======================
def main():
    name = input('Enter your name: ')
    print('Greetings', name, ' welcome to the Basic Math Tutor')

    done = False
    menu = '\n1.) odd/even\n2.) multiplication\n3.) quit\n'
    while not done:
        print(menu)
        choice = input('\tChoice:')
        if choice == '1':
            practice_odd_even()
        elif choice == '2':
            practice_multiplication()
        elif choice == '3':
            done = True
        else:
            print('Invalid choice:', choice)

    print('Goodbye')

if __name__ == '__main__':
    main()
