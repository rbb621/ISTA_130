'''
Name: Ricky Berliant
Date: 10/16/2025
Section Leader: Sungjoon
Week 8: Strings 1 Worksheet
File: Strings_.py
'''


'''
1. Given a variable word that holds a string, write a line of code that prints 
   the string without its first and last characters. 
   
2. Write a line of code that prints the string in uppercase.

3. Write a line of code that prints a similar string, but the first pair of 
   letters is repeated three times. 

4. Write a line of code that prints the string and then on the next line prints
   a dash underneath each letter of the string.

5. Write a line of code that prints a string consisting of the first two and 
   the last two characters in the string.
'''

word = "dragon ball z"

#1. without the letter D and letter Z
print(word[1:-1])


# 2. Write a line of code that prints the string in uppercase.
print(word.upper()) 

# 3. First pair of letters is repeated three times. 
print(word[2:] * 3 + word[:2])


# 4.
print(word)
print('-' * len(word))

# 5. 
print(word[:2] + word [-2:])



'''
Convert this for loop, which traverses by element, into a for loop that traverses by index.
Then convert it into a while loop. You will have to use string indexing.
for ch in word:
print(ch * n)
'''

# for ch in len(word):
#     print(ch * len(word))

'''
Write a function called last_3 that takes one string argument and returns a new string
containing the argument's last 3 characters. If the argument doesn't have 3 characters, return it.
Use string slicing.
'''

def last_3(string):
    if len(string) < 3:
        return string
    return string[-3:]


'''
Write a function called dashes that takes one string argument and returns a new string that has
the characters of the argument separated by dashes. dashes('dog') returns 'd-o-g'.
Write it two ways, using different types of loops. Can you traverse by element?
'''

def dashes(string):
    blank_string = ""
    for i in string:
        if string != blank_string:
            print('-'.join(string))
            blank_string += "-"

    return blank_string
        


def while_dashes(string):
    blank_string = ""
    i = 0
    while i < len(string):
        blank_string += string[i]
        if string != blank_string:
            print('-'.join(string))
        i += 1
    return blank_string


'''
Write a function called full_name whose string argument has format "last, first"
(letters may be upper or lowercase) and returns the string "First Last". Examples:
full_name("fudd, elmer") -> "Elmer Fudd"
full_name("DUCK, donald") -> "Donald Duck"
There is more than one way to do this, but the find method may be helpful.
'''

def full_name(last, first):
    
    print(last.find('S'))
    
    



'''
Write a Boolean function called is_num that takes a string and returns True if the string can
safely be passed to the float typecasting function (or int), False otherwise. The isdigit
string method will be helpful.
'''

def is_num(string):
    


def main():
    print(last_3('Hollow Knight'))
    print(dashes('Sonic'))
    print(while_dashes('Eminem'))
    print(full_name('simpson', 'homer'))
    print(is_num('60'))
    

if __name__ == '__main__':
    main()