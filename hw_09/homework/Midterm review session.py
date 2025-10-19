

# Loops breaks and returns
added_variable = 0
for i in range(3):
    added_variable = added_variable + i
    for j in range(3):
        added_variable = added_variable + j
        if added_variable == 5:
            break
    if added_variable == 5:
        break


def add_stuff_and_stop_at_five(added_variable):
    added_variable = 0
    for i in range(3):
        added_variable = added_variable + i
        for j in range(3):
            if added_variable == 5:
                return added_variable
            added_variable = added_variable + j

add_stuff_and_stop_at_five(3)

# Example of when to use a while True loop  
def keep_going():
    while True:
        user_answer = input('Do you want to continue? y/n: ')
        if user_answer == 'y' or user_answer == 'Y':
            return user_answer
        elif user_answer == 'N' or user_answer == 'n':
            return user_answer
        else:
            print('try again')
            continue

# Functions within functions
def do_something(a,b):
    store_variable = a * b
    return store_variable

def do_something_else(a,b,c):
    store_variable = do_something(a,b) + c
    return store_variable

test = do_something_else(2,5,3)
type(test) 

# do_something(2,5) + 3
# 10 + 3
# a * b + c
# 2 * 5 + 3
# 13

test = do_something(2,5)
type(test) 
# evaluates to an int because the expression 'do_something(2,5)'
# returns a variable that is an int

test = print('hello')
type(test)
# evaluates to None because print returns None


def keep_going():

    user_answer = input('(Y)/(N): ')

    # k / 3 - k // 3

    if user_answer == 'y' or user_answer == 'Y':
        print('yes')

    if user_answer == 'y' or True:
        print('yes')

    if 'Y':   
        print('yes')
    if True:   
        print('yes')

