'''

Write a function called pig_latin that translates words and phrases into 
'pig latin'*. 

The function will take a single string parameter string_to_translate 
containing a word or phrase (multiple words separated by spaces) and prints the
translated version of that word or phrase. The printed phases should match the 
original string from the parameter, including the same spaces, but translates 
all of the words into pig latin. This function assumes that the 
string arguments used will not contain punctuation.

*Pig latin is a 'language' that places the first letter of a word at the end, 
and adds -yay to to the end. example: 'hello' --> 'ellohyay'
. 
Single character words, like "a" are translated as "ayay"

Below your function definition, 
include a function call for your 
pig_latin function using the string 
"I really like bananas but prefer pineapples" as the argument.
'''

# def pig_latin(word):
#     new_string = ""
    
#     for ch in word:
#         new_string += ch.pop([0]) + ch + ch[0]+ 'ayay'
        
    

# print(pig_latin('"I really like bananas but prefer pineapples'))


def pig_latin(string_to_translate):
    words = string_to_translate.split()    # split into words
    translated_words = []
    
    for word in words:
        if len(word) == 1:                 # single-letter word (ex: "I")
            new_word = word + "ayay"
        else:
            new_word = word[1:] + word[0] + "yay"
        
        translated_words.append(new_word)
    
    print(" ".join(translated_words))


# Function call
pig_latin("I really like bananas but prefer pineapples")


'''

- create a dictionnary
The function has a single parameter filename which is the name of a text file 
that contains comma separated values.
returns a dictionary that has restaurant names as keys 
and a list containing all of the reviews as floats.
'''

# create function restaurant_review
# creat dictionary
# 

def restaurant_review(filename):
    infile = open(filename, 'r')
    review_dict = {}
    review_list = []
    
    for line in infile:
        parts = line.strip().split(",")
        restaurant = parts[0]
        reviews = float(parts[1])
        if restaurant not in review_dict:
            review_dict[restaurant] = review_list
        review_dict[restaurant].append(reviews)
            
    return review_dict

# def restaurant_review(filename):
#     review_dict = {}
    
#     with open(filename, 'r') as infile:
#         for line in infile:
#             parts = line.strip().split(",")
#             restaurant = parts[0]
#             review = float(parts[1])
            
#             if restaurant not in review_dict:
#                 review_dict[restaurant] = []
#             review_dict[restaurant].append(review)
    
#     return review_dict

        
    
restaurant_review('restaurant_reviews.txt')


'''
Define a class named Pet. 

Each Pet object has the following instance variables: name (pet's name: string), 
species (type of animal; string), tricks (list of trick names; list of strings). 
__init__ (5 pts) has parameters corresponding to each instance variable, in the
above order. 
Set instance variables for each of the arguments. 

Write a __repr__ (5 pts) so that a Pet object prints in this format: name the species can do: tricks
For example: 
Mochi the cat can do: jump, snooze dramatically
Pickles the parrot can do: sing horribly, spin in a circle
Tallulah the turtle can do: walk with purpose, ignore commands
(notice that the tricks listed are separated by commas and don't have [ ] or ' ')

Write an instance method called perform (5 pts) that takes no arguments. 

It should print a string following this format: pet performs trick - where the trick performed is a randomly selected trick from the list of the pet's tricks. 

You can import the random module for this. 
Assume that all pets will know at least 1 trick.
For example:
Mochi.perform()
"Mochi performs snooze dramatically"

(3 bonus pts) Below your class definition, create an instance of the Pet class for each of the pets in the examples above
(Mochi, Pickles, Tallulah - use their lowercase names as the variable names). 

Create a list called contestants containing each of the pets you created Pet objects for.  
Loop through the contestants list and have each pet perform once.
'''

# name = string
# animal_type = string
# tricks = string

import random

class Pet:
    def __init__(self, name, species, tricks):
        self.name = name
        self.species = species
        self.tricks = tricks
        return None
        

    def __repr__(self):
        ''' Return a textual representation of self. '''
        output = self.name + ' the' + self.species + "can do: " + self.tricks + ", " + self.tricks + '\n'
        output += self.name + ' the' + self.species + "can do: " + self.tricks + ", " + self.tricks + '\n'        
        output += self.name + ' the' + self.species + "can do: " + self.tricks + ", " + self.tricks + '\n'    
        return output
    
    def perform(self):
        return self.tricks[random.randrange(len(self.tricks))]
    
Mochi the cat can do: jump, snooze dramatically
Pickles the parrot can do: sing horribly, spin in a circle
Tallulah the turtle can do: walk with purpose, ignore commands