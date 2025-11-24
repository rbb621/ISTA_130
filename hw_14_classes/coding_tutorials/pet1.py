'''
Author: <your name>
Date: <the date>
Class: ISTA 130
Section Leader: <your section leader>

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment
import random

# put all of your function / class definitions below this line and then delete this comment
class Pet:
    ''' Class Pet represents animal pets. '''

    def __init__(self, name, animal_type, toys_list):
        '''
        Initialize an instance of an object of type 'Pet' with the following attributes:
        name of pet, species, and a list of their toys
        '''
        self.name = name
        self.animal_type = animal_type
        self.toys_list = toys_list
        return None

    def __repr__(self):
        ''' 
        Return a string representation of a self that contains the Pet's
        name, species, and toy list. 
        '''
        pet_summary = "\nHello!\n"
        pet_summary = pet_summary + "My name is " + self.name + "\n"
        pet_summary = pet_summary + "I am a(n) " + self.animal_type + "\n"
        pet_summary = pet_summary + "My toys are: \n"
        for current_toy in self.toys_list:
            pet_summary = pet_summary + "- " + current_toy + "\n"
        return pet_summary

    def pick_toy(self):
        '''
        Return a toy chosen at random from the Pet object's toy list.
        '''
        return self.toys_list[random.randrange(len(self.toys_list))]



#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    tallulah = Pet('Tallulah','turtle',['ball','plastic palm tree'])
    #print(tallulah.name)
    #print(tallulah.animal_type)
    #print(tallulah.toys_list)
    #print(type(tallulah))
    print(tallulah)
    print(tallulah.pick_toy())

if __name__ == '__main__':
    main()
