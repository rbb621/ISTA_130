# Exercise: Apples

# Let's use integer division and the modulus operator to solve a simple story problem:

# ➔ A family receives a box of apples in the mail.
# Rather than bicker, they decide to divide the apples up evenly ,
# and feed any remaining apples to Wilbur, their pet pot-bellied pig.

# ➔ Write a function called fruit_distributor that takes two parameters. The
# first is an integer for the number of pieces of fruit.
# The second is an integer for the number of people to distribute the fruit among. 

# The function prints out the number of pieces per person and the number left over.
# // does integer division
# % gets the remainder

def fruit_distributor(num_fruit_received, num_people):
    num_pieces_per_person = num_fruit_received // num_people
    num_leftover_wilbur = num_fruit_received % num_people
    
    print('You have received ' + str(num_fruit_received) + ' fruit which will be divided among ' + str(num_people) + ' people and Wilbur')
    print('Each person will receive ' + str(num_pieces_per_person) + ' fruit')
    print('Wilbur will receive ' + str(num_leftover_wilbur) + ' fruit')
    return None
    


def main():
    fruit_distributor(7, 2)
    

if __name__ == '__main__':
    main()