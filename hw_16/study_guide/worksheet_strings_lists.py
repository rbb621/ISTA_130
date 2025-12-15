''' In-class examples. '''

def time_to_seconds(time):
    '''
    This function has one string parameter representing a time in
    format "hours:minutes:seconds", 
    and returns the equivalent number of seconds.
    '''
    time = time.split(':') # time is now a list of strings
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
    
def full_name(name):
    '''
    This function has one string parameter, name, containing
    a string in this format: <last>, <first> with unknown letter case
    and returns a the string <First> <Last> capitalized correctly.
    '''
    name = name.split(', ') # name is now a list of strings
    return name[1].capitalize() + ' ' + name[0].capitalize()
    
def word_lengths(string):
    '''
    This function takes a string (string) and returns a list
    containing the lengths of the words in string.
    '''
    lengths = []
    words = string.split() # now we have a list of the words in the string
    for word in words:
        lengths.append(len(word))
    return lengths

def word_lengths2(string):
    words = string.split()
    for i in range(len(words)):
        words[i] = len(words[i])
    return words
    
def third(lst): # don't use list as a variable name
    '''
    This function takes a list (lst) and replaces
    every third element with 3.  It returns None.
    '''
    for i in range(len(lst)):
        if i % 3 == 2:
            lst[i] = 3
            
def third2(lst): # don't use list as a variable name
    '''
    This function takes a list (lst) and replaces
    every third element with 3.  It returns None.
    '''
    for i in range(len(lst)):
        if not (i + 1) % 3:
            lst[i] = 3
            
def separator(string, sep):
    '''
    This function takes two strings and returns a new string that
    has the whitespace between words in the first argument (string)
    replaced with sep.
    '''
    string = string.split()
    return sep.join(string)

def separator2(string, sep):
    return sep.join(string.split())
    
def phone_nums(fname):
    '''
    This function takes one string argument, a filename in parameter
    fname, and returns a list of all of the phone numbers in the 
    file.  Assume phone numbers are in format ddd-ddd-dddd.
    '''
    # some pseudocode, always a good idea:
    # open our file
    # we will be updating a variable (building a list) in a loop, so initialize it
    # traverse the file by line:
    #     break the line into words
    #     check each word:
    #         get rid of any punctuation that might mislead us
    #         check the word to see if it's a phone num and update the list if so
    # return the list
    fp = open(fname)
    nums = []
    for line in fp:
        line = line.split()
        for word in line:
            if word[-1] in [',', '.']:
                word = word[:-1]
            word = word.split('-')
            if len(word) == 3 and len(word[0]) == 3 and \
               word[0].isdigit() and len(word[1]) == 3 and \
               word[1].isdigit() and len(word[2]) == 4 and \
               word[2].isdigit():
                nums.append('-'.join(word))
    return nums
    
def r_words(fname):
    '''
    This function takes a filename (fname) and returns a list
    containing all of the words in the file that start
    with 'r' or 'R'.
    '''
    file = open(fname, 'r')
    rwords = []
    for line in file:
        line = line.split() 
        for word in line:
            if word[0] in ['r', 'R']:
                rwords.append(word)
    return rwords
            
print("Should be 45:", time_to_seconds('0:0:45'))
print("Should be 7200:", time_to_seconds('2:0:0'))
print("Should be 180:", time_to_seconds('0:3:0'))
print("Should be " + str(45 + 7200 + 180) + ":", time_to_seconds('2:3:45'))

print(full_name("fudd, elmer"))

print(word_lengths('I heart Rocket.'))

print(third(['you', 77, True, 0.5, 'me', 'hmm'])) # what will this print?
lst = ['you', 77, True, 0.5, 'me', 'hmm']
third(lst)
print(lst)

print(separator('I heart Rocket!', '---'))

print(r_words('worksheet_strings_lists.py'))

