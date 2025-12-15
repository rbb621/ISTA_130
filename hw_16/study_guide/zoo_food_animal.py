class Animal:
    ''' 
    Each Animal object represents an individual animal
    in a zoo.  It has a name, species, and feeding
    requirements information.
    '''
    def __init__(self, name, animal_type, food, amount):
        ''' 
        Initialize an Animal object.  Parameter name is a
        string (for inst var name), animal_type (species)
        is a string, food (food) is a string containing the 
        type of food the animal eats (e.g. 'hay'), and amount
        (amount) is a float giving the amount the animal
        eats in kg in one meal.  Return None.
        '''
        self.name = name
        self.species = animal_type
        self.food = food  # string
        self.amount = amount # This animal requires this amt of food twice a day.
        self.notes = None
        
    def __repr__(self):
        ''' Return a textual representation of self. '''
        result = self.name.upper() + '\n' + '-' * 20 + '\n'
        result += "Species: " + self.species + '\n'        
        result += "Food type: " + self.food + '\n'
        result += "Amount per meal: " + str(self.amount) + ' kg\n'
        if self.notes:
            result += "Special comment: " + self.notes + '\n'
        return result
        
    def add_appt(self, doctor, date, time, reason):
        '''
        Assign a string to self.notes describing an appt
        using string parameters doctor, data, time, and
        reason.  Return None.
        '''
        appt_str = self.name + ' has an appt with Dr. ' + doctor + \
          ' on ' + date + ' at ' + time + '.\n'
        appt_str += 'Reason for appt: ' + reason + '\n'
        self.notes = appt_str
        
    def clear_notes(self):
        ''' Set self.notes to None.  Return None. '''
        self.notes = None
        
class Food:
    '''
    Food objects contain information about a given kind of
    food (e.g. hay) for use by the zoo in managing their 
    animals' feeding.
    '''
    def __init__(self, name, price, quantity_on_hand):
        ''' 
        Initialize a Food object.  Parameter name is a
        string (for inst var name), price (price) 
        contains the price per kilogram and is a float, and 
        quantity_on_hand (qoh) is a float representing
        the amount of the food at the zoo in kg.  Return None.
        '''
        self.name = name
        self.price = price
        self.qoh = quantity_on_hand
        
    def __repr__(self):
        ''' Return a textual representation of self. '''
        return "<" + self.name + ', ' + str(self.price) + ', ' + str(self.qoh) + '>\n'
        
    def monthly_cost(self, animal):
        ''' Returns the cost to feed the Animal animal for 30 days. '''
        return 60 * animal.amount * self.price
        
class Zoo:
    '''
    A Zoo object represents a zoo and has the information
    necessary to make sure the animals are fed.
    '''
    def __init__(self, animal_file, food_file):
        '''
        Initialize a zoo object.  It contains a dictionary
        mapping animal names (e.g.) 'Annie' to Animal objects.
        It contains another dictionary mapping food types (e.g.
        'hay') to Food objects.  Both dictionaries are initialized
        by reading data from files.  Filenames are parameters.
        Return None.
        '''
        self.animals = {}
        af = open(animal_file, 'r')
        for line in af:
            line = line.strip().split(',')
            line[3] = float(line[3])
            while line[0] in self.animals:
                line[0] += '-2'
            self.animals[line[0]] = Animal(line[0], line[1], line[2], line[3])
        af.close()
        self.food = {}
        ff = open(food_file, 'r')
        for line in ff:
            line = line.strip().split(',')
            self.food[line[0]] = Food(line[0], float(line[1]), float(line[2]))
        ff.close()
        
    def reorder(self, food):
        ''' 
        food is a Food object.
        Reorder food if there is less than 7 days supply. 
        Return a months supply (30 days) if so, None if not.
        '''
        one_day = 0
        for animal in self.animals:
            if food.name == self.animals[animal].food:
                one_day += 2 * self.animals[animal].amount
        if food.qoh < 7 * one_day:
            return 30 * one_day
        return None
        
    def get_order(self):
        '''
        Return a dictionary mapping each food type to the
        amount the zoo currently needs to order.
        '''
        order = {}
        for food in self.food:
            order[food] = self.reorder(self.food[food])
        return order
                
z = Zoo('animals.csv', 'food.csv')   
for animal in z.animals:
    print(z.animals[animal])
print(z.food)
print(z.get_order())
  
        
        
        
        
        
        
        
        
        