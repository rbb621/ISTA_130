
'''
Name: Ricky Berliant
Date: 12/4/2025
Class: ISTA 130
Section Leader: Sungjoon Shin
Assignment: Extra Credit Week 14
'''


class Animal:
    def __init__(self, name, species, food, amount):
        self.name = name
        self.species = species
        self.food = food
        self.amount = amount
        self.notes = None
        return None
        

    def __repr__(self):
        output = '-------------------- \n'
        output += self.name + '\n'  
        output += 'Species: ' + self.species + '\n'
        output += 'Food type: ' + self.food + '\n'
        output += 'Amount per meal: ' + str(self.amount) + '\n'
        return output

    
    def add_appt(self, doctor, date, time, reason):
        output = self.name + ' has an appt with ' + doctor + ' on ' + date + ' at ' + time + '\n'
        output += 'Reason for appt: ' + reason + '\n'
        self.notes = output
        
        
    def clear_notes(self):
        self.notes = None

class Food:
    def __init__(self, name, price, qoh):
        self.name = name
        self.price = price
        self.qoh = qoh
        
    def __repr__(self):
        output = '<' + self.name + ',' + self.price + ',' + self.qoh + '>'
        return output
    
    def monthly_cost(self, animal):
        total_meals = 30 * 2
        total_amount = total_meals * animal.amount
        return total_amount * self.price


def main():
    pet_name = Animal('Hachi', 'Dog', 'dogfood', 5.99)
    print(pet_name)
    
    pet_food = Food('Target', 2.00, 15)
    print(pet_food)
