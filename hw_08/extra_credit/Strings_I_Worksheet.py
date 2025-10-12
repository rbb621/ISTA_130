'''
Name: Ricky Berliant
Date: 10/16/2025
Section Leader: Sungjoon
Week 8: Strings 1 Worksheet
File: Strings_.py
'''

#Question 1
'''
ISTA 130 Strings I Worksheet
What is the output from the following lines of code?

text = 'Rocket!'
print(text[2])
'''
#Output: c

'''
print(text[-1] * 5)
'''
#Output: !!!!!

'''
mystery = text[-2] + text[0] + text[-3] + text[4]
m2 = mystery.upper()
print(m2)
'''
#Output: TREE


'''
print(mystery)
'''
#Output: tRee

'''
print(m2 + m2.lower())
'''
#Output: TREEtree

'''
print(m2 > m2.lower())
'''
#Output: False

'''
print(m2 < m2.lower())
'''
#Output: True


'''
print('REE' in m2)
'''
#Output: True

'''
print('REE' in m2.lower())
'''
#Output: False


 # what kind of traversal is this?
'''
for i in range(len(text)):
    if i % 2 == 1:
        print(text[i])
        
'''

#Output:
    #o
    #k
    #t

# what kind of traversal is this?
'''
for ch in text: 
    if ch > 'e':
    print(ch)
'''
#Output: 
    #o
    #k
    #t


'''
def odds(string):
new_str = ''
for i in range(len(string)):
    if i % 2 == 1:
        new_str += string[i]
return new_str

print(odds(text))
'''
#Output: 
    #o
    #k
    #t



'''
Write a function called first_and_last that takes one string argument
and returns a new string containing the first and last characters 
in the argument. If the argument is the empty string
return None.
'''

def first_and_last(string): 
    if string == "":
        return None
    
    first_string = string[0]
    last_string = string[-1]
    
    return first_string + last_string
    


'''
Write a function called thirds that takes one string argument and returns a new string
consisting of the third, sixth, ninth, etc. characters in the argument. 
If there aren't at least three
characters, return None. What kind of traversal did you use?
'''

def thirds(string):
    
    if len(string) < 3:
        return None
    else:
        return string[2::3]
    


'''
Write a function called count that takes two string arguments. The first is a nonempty string
and the second is a single character. Return the number of times the character appears in the
string. What kind of traversal did you use?
'''


def count(string, target):
    count = 0
    for ch in string:
        if ch == target:
            count += 1
    return count
        
    

# '''
# Write a function called smallest that takes one nonempty string argument and returns the
# smallest character that is not a space, tab, or newline. Assume the first character in the string is
# not a space, tab, or newline. What kind of traversal did you use?
# '''

def smallest(string):
    smallest_char = string[0]
    
    for ch in string:
        if ch in (' ', '\t', '\n'):
            continue
        if ch < smallest_char:
            smallest_char = ch
    return smallest_char

    

    

'''
Write a function called alphabetize that takes three string arguments and prints them in
alphabetical order, one per line, starting with the smallest. Do not distinguish between capital
and small letters
'''

def alphabetize(string_1, string_2, string_3):

    kingdom_hearts = [string_1, string_2, string_3]
    
    kingdom_hearts.sort(key=str.lower)
    
    for characters in kingdom_hearts:
        print(characters)
    
    
def main():
    print(alphabetize('sora', 'donald', 'goofy'))
    print(first_and_last('Hunter x Hunter'))
    print(thirds('Genshin Impact'))
    print(count('Fire Emblem', 'e'))
    print(smallest('Shrek'))

    
    
if __name__ == '__main__':
    main()
    
