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

class Zoo:
    def __init__(self, fname_animals, fname_food):
        self.animals = {}
        a_file = open(fname_animals, 'r')
        for line in a_file:
            current_line = line.strip().split(',')
            while current_line[0] in self.animals:
                current_line[0] = current_line[0] + '-2'
            self.animals[current_line[0]] = Animal(current_line[0],current_line[1],current_line[2],float(current_line[3]))
        a_file.close()
        self.food = {}
        f_file = open(fname_food, 'r')
        for line in f_file:
            current_line = line.strip().split(',')
            self.food[current_line[0]] = Food(current_line[0],float(current_line[1]),float(current_line[2]))
        f_file.close()

    def reorder(self, food_obj):
        total_food_needed_per_meal = 0
        for animal in self.animals:
            if food_obj.name == self.animals[animal].food:
                total_food_needed_per_meal += self.animals[animal].amount
        if food_obj.qoh >= total_food_needed_per_meal * 2 * 7:
            return None
        else:
            return (total_food_needed_per_meal * 2 * 30) - (food_obj.qoh)
    
    def get_order(self):
        order = {}
        for food in self.food:
            order[food] = self.reorder(self.food[food])
        return order



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

    my_zoo = Zoo('animals.csv', 'food.csv')
    print(my_zoo.animals)
    print(my_zoo.food)
    
    ######
    print("*" * 20)
    my_horsemeat = Food("horsemeat", 4.5, 500)
    print(my_zoo.reorder(my_horsemeat))
    
    ########
    print("*" * 20)
    print(my_zoo.get_order())

if __name__ == '__main__':
    main()
