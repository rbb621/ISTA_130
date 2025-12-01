'''
Author: <your name>
Date: <the date>
Class: ISTA 130
Section Leader: <your section leader>

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment


# put all of your function / class definitions below this line and then delete this comment

class Animal:
    '''
    Define a class called Animal . Animal 's initializer takes four arguments corresponding to the
    instance variables name , species , food , and amount . amount is a float, the others are
    strings. food is the type of food the Animal eats, amount is the amount in kilograms of one
    meal. Initialize a fifth instance variable called notes to None .
    '''
    def __init__(self, name, species, food, amount):
        self.name = name
        self.species = species
        self.food = food
        self.amount = amount
        self.notes = None

    def __repr__(self):
        output = self.name.upper() + "\n"
        output += "-"*20  + "\n"
        output += "Species: " + self.species + "\n"
        output += "Food type: " + self.food + "\n"
        output += "Amount: " + str(self.amount) + "\n"
        if self.notes:
            output += "Special comment: " + self.notes + "\n"
        return output
        
    def add_appt(self, dr_name, appt_date, appt_time, reason_for_visit):
        appt_str = self.name + " has an appointment with Dr. " + dr_name + " on " + appt_date + " at " + appt_time + ".\n"
        appt_str += "Reason for appointment: " + reason_for_visit + "\n"
        self.notes += "\n" + appt_str
    
    def clear_notes(self):
        self.notes = None

class Food:
    def __init__(self, name, price, qoh):
        self.name = name
        self.price = price
        self.qoh = qoh
    
    def __repr__(self):
        return "<" + self.name + ", " + str(self.price) + ", " + str(self.qoh) + ">\n"

    def monthly_cost(self, animal):
        return self.price * animal.amount * 2 * 30


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    rocketthedog = Animal('Rocket','dog','dog food',0.25)
    rocketthedog.notes = "Best dog ever!!!\n"
    print(rocketthedog)

    rocketthedog.add_appt('Drew', '4/23/15', '11:00 am', 'rabies shot')
    print(rocketthedog.notes)

    rocketthedog.clear_notes()
    print(rocketthedog)

    kirkland = Food("Costco_generic", 2.00, 15)
    print(kirkland)

    print(kirkland.monthly_cost(rocketthedog))

if __name__ == '__main__':
    main()
