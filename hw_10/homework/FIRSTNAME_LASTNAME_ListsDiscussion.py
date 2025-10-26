'''
Name: Ricky Berliant
Date: 10/31/2025
Section Leader: Sungjoon Shin (SL)
Homework: Lists Discussion

Module: Lists

Filename: FIRSTNAME_LASTNAME_ListsDiscussion.py

Summary: Learning how to manipulate strings by combining lists
and using different types of methods.
'''


'''

Write a function called split that takes a string to be split and a character 
to be used for splitting. 

It returns a list of the words in the string delimited by the character. 

Example calls: split('I heart Rocket!', ' ') --> ['I', 'heart', 'Rocket!']

split('I heart Rocket!', 'e') --> ['I h', 'art Rock', 't!']

'''

# split function
def split(string, delimiter):
    new_str = ""
    words = []
    for ch in string:
        if ch == delimiter:
            words.append(new_str)
            new_str = ""
        else:
            new_str += ch
    words.append(new_str)
    return words

'''

Write a function called underscored. 

It takes a string argument in camelCase ('aStringThatLooksLikeThis'), 
and returns the string converted into python's convention for variables 
('a_string_that_looks_like_this'). 

(Hint: isupper)
underscored('aStringThatLooksLikeThis') --> 'a_string_that_looks_like_this'
'''


# underscored function
def underscored(string):
    new_str = ""
    for ch in string:
        if ch.isupper():
            new_str += "_" + ch.lower()
        else:
            new_str += ch
    return new_str

def main():
    print(underscored('aStringThatLooksLikeThis'))
    print(split('I heart Rocket!', ' '))
    print(split('I heart Rocket!', 'e'))
    

if __name__ == '__main__':
    main()