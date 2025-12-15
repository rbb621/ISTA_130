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
        
