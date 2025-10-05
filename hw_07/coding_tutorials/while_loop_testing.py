i = 0

while i < 10:
    print(i)
    i += 1
print('after the while loop, it prints out', i)






m = 100

while m > 10:
    print(m)
    m -= 1
print('after the while loop, it prints out', m)





i = 0
word = 'gas'

while i < 10:
    print(i, '', word)
    i += 1
    word = ' gas' * i
print('Done')
print(i, '', word)
print('i =', i, ', word =', word)


i = 0
word = 'gas'

# when it's always True, it does a infinite loop
while i >= 0:
    print(i, '', word)
    i += 1
    word = 'gas' * i
print('Done')
print(i, '', word)


i = 0
word = 'gas'

# You need to add a aritmetic value to control the while loop
while i < 10:
    print(i, '', word)
    i += 1
    word = 'gas ' * i
print('Done')
print(i, '', word)


# Choose entry condition
# True must execute the code
# False - won't run at all
# Make sure to indent the statements
# Eventually, the the condition become false to break the loop

# *******************************
#         Basic Example
# *******************************
word = 'lost'
wrong = True

while wrong:
    guess = input('Guess the word: ')
    if guess == word:
        wrong = False
    else:
        print()
        print('Wrong!')

print('GOT IT!')

# *******************************
#         Instead do this
# *******************************

word = 'lost'
guessed_it = False

while not guessed_it:
    guess = input('Guess the word: ')
    if guess == word:
        guessed_it = True
    else:
        print()
        print('Wrong!')

print()
print('You did it!')


def guess_word(word):
    guessed_it = False
    count = 0
    
    while not guessed_it:
        guess = input('Guess the word: ')
        count += 1
        if guess == word:
            guessed_it = True
        else:
            print('Wrong')
         
    return count

def main():
     word = 'jimmy'
     guesses = guess_word(word)
     print('You took', guesses, 'guesses')
     
if __name__ == '__main__':
     main()


def guess_word(word):
    guessed_it = False
    count = 0
    
    while not guessed_it:
        guess = input('Guess the word: ')
        count += 1
        if guess == word:
            guessed_it = True
        else:
            print('Wrong')         
    return count

def main():
    word = 'jimmy'
    guesses = guess_word(word)
    
    if guesses == 1:
        print('You took', guesses, 'guess')
    else:
        print('You took', guesses, 'guesses')


     
if __name__ == '__main__':
    main()
