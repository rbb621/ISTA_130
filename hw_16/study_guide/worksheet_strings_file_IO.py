'''
In-class examples and solutions to worksheet.
'''

def decorate_word(word):
    '''
    This function takes a word (string) and returns a new string
    that is the argument surrounded by a nice box of asterisks.
    '''
    first_and_last = '*' * (len(word) + 4) + '\n'
    filler = '*' + ' ' * (len(word) + 2) + '*' + '\n'
    inner = '* ' + word + ' *' + '\n'
    return first_and_last + filler + inner + filler + first_and_last

def time_to_seconds(time):
    '''
    This function has one string parameter representing a time in
    format "hours:minutes:seconds", 
    and returns the equivalent number of seconds.
    '''
    colon1 = time.find(':')
    colon2 = time.find(':', colon1 + 1)
    hours = int(time[:colon1]) * 3600
    minutes = int(time[colon1 + 1:colon2]) * 60
    return hours + minutes + int(time[colon2 + 1:])
    
def swap_case(string):
    '''
    This function takes a string and returns a new string with all
    lowercase characters converted to upper and all upper to lower.
    '''
    result = ''
    for ch in string:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            result += ch
    return result
    
def line_nums(fname):
    '''
    This method opens fname and writes a new file with the same content
    but with line numbers.  The new file is called fname stem + _ln + 
    extension.  It returns None.
    '''
    in_file = open(fname, 'r')
    dot = fname.find('.')
    out_file = open(fname[:dot] + '_ln' + fname[dot:], 'w')
    i = 1
    for line in in_file:
        out_file.write(repr(i) + ': ' + line)
        i += 1
    out_file.close()
    in_file.close()
        
def word_search(fname, word):
    '''
    This method opens fname and prints every line containing word,  
    prefixed by its line number and a colon.  It returns None.
    '''
    print('*' * 5, word, '*' * 5)
    file = open(fname, 'r')
    i = 1
    for line in file:
        if word in line:
            print(repr(i) + ':', line.strip())
        i += 1
    file.close()
    
def word_count(fname):
    '''
    This method opens fname and prints the number of words on every line,  
    prefixed by the line's number and a colon.  It assumes that words are
    separated by a single space.  It returns None.
    '''
    file = open(fname, 'r')
    i = 1
    for line in file:
        print(repr(i) + ':', line.count(' ') + 1)
        i += 1
    file.close()
    
def main():
    print(decorate_word('Rocket!'))
    print(decorate_word(''))

    print("Should be 45:", time_to_seconds('0:0:45'))
    print("Should be 7200:", time_to_seconds('2:0:0'))
    print("Should be 180:", time_to_seconds('0:3:0'))
    print("Should be " + str(45 + 7200 + 180) + ":", time_to_seconds('2:3:45'))
    
    print("swap_case('I Don\'t KnOw'):", swap_case('I Don\'t KnOw'))
    
    line_nums('iwalktheline.txt')
    word_search('iwalktheline.txt', 'line')
    print()
    word_search('iwalktheline.txt', 'hat')
    print()
    word_count('iwalktheline.txt')
    
if __name__ == "__main__":
    main()