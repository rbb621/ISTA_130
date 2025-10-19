'''
Worksheet solutions and in-class examples.
'''

def str_pyramid(string):
    '''
    This function takes a string and prints each letter
    on a line repeated i + 1 times, where i is its 
    position.  It returns None.
    '''
    for i in range(len(string)):
        print(string[i] * (i + 1))
        
def ttable(n):
    '''
    This functions takes a positive integer n and prints
    an n x n times table.  It returns None.
    '''
    header = ' ' * 4 + '|'
    for i in range(n):
        header = header + str(i + 1).rjust(5) 
    print(header)
    print('-' * 4 + '|' + '-' * 5 * n)
    for i in range(n):
        line = str(i + 1).ljust(4) + '|'
        for j in range(n):
            line += str((i + 1) * (j + 1)).rjust(5)
        print(line)
    
def last_3(word):
    '''
    This function takes one string argument called word
    and returns a new string containing the 
    argument's last 3 characters.  If the 
    argument doesn't have 3 characters, return it.
    '''    
    return word[-3:]
    
def dashes_by_element(word):
    if not word: # same as if word == '':
        return ''
    result = ''
    for ch in word:
        result += ch + '-'
    return result[:-1]

def dashes_by_index(word):
    if not word: # same as if word == '':
        return ''
    result = ''
    for i in range(len(word) - 1):
        result += word[i] + '-'
    return result + word[-1]

def dashes_w(word):
    '''
    This function takes one string argument, word, and returns a 
    new string that has the characters of the argument separated by dashes.
    '''
    if not word: # same as if word == '':
        return ''
    result = ''
    i = 0
    while i < len(word) - 1:
        result += word[i] + '-'
        i += 1
    return result + word[-1]

def full_name(name):
    '''
    This function has one string parameter, name, containing
    a string in this format: <last>, <first> with unknown letter case
    and returns a the string <First> <Last> capitalized correctly.
    '''
    comma = name.find(',')
    last = name[:comma]
    first = name[comma + 2:]
    # return first[0].upper() + first[1:].lower + ...
    return first.capitalize() + ' ' + last.capitalize()
    
def full_name2(name):
    '''
    This function has one string parameter, name, containing
    a string in this format: <last>, <first> with unknown letter case
    and returns a the string <First> <Last> capitalized correctly.
    '''
    comma = name.find(',')
    return name[comma + 2:].capitalize() + ' ' + name[:comma].capitalize()
    
def is_num(num_string):
    '''
    Determines if the string parameter num_string is a valid
    representation of an integer or float and returns True if so.
    Otherwise, return False.
    '''
    if not num_string:
        return False # we need this to avoid runtime error indexing empty string
    if num_string[0] == '-':
        num_string = num_string[1:]
    num_string = num_string.replace('.', '', 1)
    return num_string.isdigit()
    
def main():
    '''
    Convert loops, test functions.
    '''
    # First problem solutions:
    word = 'Rocket!'
    print(word[1:-1])
    print(word.upper())
    print(word[:2] + word[-2:])
    print(word[:2] * 3 + word[-2:])
    print(word + '\n' + '-' * len(word))
    print('-----------')
    
    n = 7
    # for loop
    for i in range(n):
        print(str(i + 1) + '-squared is:', str((i + 1)**2))
    print('-----------')
    # equivalent while loop
    i = 0
    while i < n:
        print(str(i + 1) + '-squared is:', str((i + 1)**2))
        i += 1
    print('-----------')
    
    n = 3
    word = 'dog'
    # traverse by element
    for ch in word:
        print(ch * n)
    print('-----------')
    # traverse by index
    for i in range(len(word)):
        print(word[i] * n)
    print('-----------')
    # equivalent while loop
    i = 0
    while i < len(word):
        print(word[i] * n)
        i += 1
    print('-----------')
    
    print(last_3('Rocket'))

    print(dashes_by_element(''))
    print(dashes_by_element('I'))
    print(dashes_by_element('dog'))
    print(dashes_by_index(''))
    print(dashes_by_index('I'))
    print(dashes_by_index('dog'))
    print(dashes_w('dog'))
    
    print()
    ttable(12)
    print()
    ttable(7)
    print()
        
    print(full_name("fudd, elmer"))
    print(full_name2("fudd, elmer"))
    print('False:', is_num(''))
    print('False:', is_num('.'))
    print(is_num('1.'))
    print(is_num('-.1'))
    print(is_num('.1'))
    print(is_num('11.'))
    print(is_num('11.1'))
    print('False:', is_num('-'))
    print('False:', is_num('1.1.1'))
    
if __name__ == '__main__':
    main()
