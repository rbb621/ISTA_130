'''
Name: Ricky Berliant
Date: 11/20/2025
Section Leader: Sungjoon
Week 12: HW8
File: brainbodyweight.py
'''

#==================================================================================

'''
African elephant weighed 6654.0 kilograms
brain weight was 5712.0 grams. 

The African giant pouched rat weighed 1.0 kilogram and its brain weight was 6.6 grams.

Your program will read the data file, collecting the values into lists. It will then allow the
user to view information about an animal, add new animals and/or remove animals.
Once the user is finished modifying the data, the program will convert all of the weights
from kilograms and grams to pounds and write the data out to a new file.

'''
#==================================================================================


#PSEUDOCODE

#Step 1: Name the file brainbodyweight
#Step 2: Create Function called find_insert_position with two parameters
#Step 3: Parameter 1: mammals name. Parameter 2: strings (in alphebetical order)
#Step 4: Return a number from the position index from list of names
#Step 5: Keep in mind that it does insert the name nor change the name list


def find_insert_position(mammals_name, name_list):
    mammals_name = mammals_name.lower()
    
    for i in range(len(name_list)):
        if mammals_name < name_list[i].lower() or mammals_name == name_list[i].lower():
            return i
            
    return len(name_list)

'''

In the file:
1.) Write a function called find_insert_position that takes two parameters. The first
parameter is a string representing a terrestrial mammal's name. The second parameter is
a list of strings in alphabetical order.

i.) The function returns an integer indicating the position (index) in the list of
names such that if you inserted the given mammal's name into the list at that
index the list would still be in alphabetical order.

Note: the function does not insert the name, it does not change the names list in any
way. It simply finds and returns the appropriate integer index.
'''

#==================================================================================

def populate_lists(mammal_names, mammal_body_weights, mammal_brain_weights):
    file = open('BrainBodyWeightKilos.csv', 'r')
    
    for line in file:
        split_parts = line.strip().split(",")

        title_name = split_parts[0].title()           
        split_parts[0].title()
        body_weight = float(split_parts[1])
        brain_weight = float(split_parts[2])
        
        mammal_names.append(title_name)
        mammal_body_weights.append(body_weight)
        mammal_brain_weights.append(brain_weight)

    file.close()

#==================================================================================


def write_converted_csv(fileName, mammal_name, body_weight, brain_weight):
    file = open(fileName, 'w')
    
    for i in range(len(mammal_name)):
        
        name = mammal_name[i].title()

        converted_body_weight = round(body_weight[i] * 2.205, 2)
        converted_brain_weight = round(brain_weight[i] * 0.0022, 2)
    
        file.write(name + "," + str(converted_body_weight) + "," + str(converted_brain_weight) + "\n")

    file.close()


#==================================================================================


def main():
    
    # STEP 1 — Create the 3 empty lists
    names = []
    body = []
    brain = []
    
    # STEP 2 — Read data from CSV into the 3 lists
    populate_lists(names, body, brain)
    
    # STEP 3 — Begin user interaction loop
    while True:
        user = input('\nEnter animal name (or "q" to quit): ')
        animal_name = user.title()
        
        # STEP 4 — If user wants to quit
        if user.lower() == "q":
              write_converted_csv("BrainBodyWeightPounds.csv", names, body, brain)
              break
        
        # STEP 5 — If animal exists in the list
        if animal_name in names:
            index = names.index(animal_name)
            print(animal_name + ": body = " + str(body[index]) + ", brain = " + str(brain[index]))

            # Ask user if they would like to delete the animal
            delete = input('Delete "' + animal_name + '"? (y|n)').lower()
            if delete == 'y':
                names.pop(index)
                body.pop(index)
                brain.pop(index)
            continue


        # STEP 6 — Animal NOT found in the list
        if animal_name not in names:
            print('File does not contain "' + animal_name + '".')
            add_animal_name = input('Add "' + animal_name + '" to file? (y|n)').lower()

        if add_animal_name == 'n':
            continue
              
        # STEP 7 — User wants to add new animal
        if add_animal_name == 'y':
            body_weights_list = float(input(' Enter body weight for "' + animal_name + '" in kilograms: '))
            brain_weights_list = float(input('Enter brain weight for "' + animal_name + '" in grams: '))
 
        
        # STEP 8 — Insert new animal in alphabetical order
        index = find_insert_position(animal_name, names)
        names.insert(index, animal_name)
        body.insert(index, body_weights_list)
        brain.insert(index, brain_weights_list)  
        continue
    
    

if __name__ == '__main__':
    main()


'''
4.) In main:

i.) Create three empty lists to hold mammal names, body weights, and brain
weights.

ii.) Populate the three empty lists you just created.

iii.) Next you will repeatedly ask the user to (note that the prompt is preceded by
a blank line):

Enter animal name (or "q" to quit):
Convert the user's response to title case. 

Depending on the user's response:
●If the name entered by the user is not in your list of names (case
insensitive search):

1.i. Print a message indicating the animal was not found.
-For example, assuming the user entered "Bugbear" you would
print:
File does not contain "Bugbear"

1.ii. Ask the user if he would like to add it. (You can assume the user
will answer either 'y' or 'n'.)

-For example, assuming the user previously entered "Bugbear":
Add "Bugbear" to file? (y|n)

- If the user enters 'n', do nothing (i.e. you'll go back to asking the user to
enter an animal name)

- If the user enters 'y', ask for the body weight and brain weight:
- Continuing the previous example you would ask the user for each of the
two following:

Enter body weight for "Bugbear" in kilograms:
Enter brain weight for "Bugbear" in grams:

& Add the new animal's data to your three lists. Put the values in the
appropriate positions in the lists so that the animals are still all
alphabetized.

● If the name entered by the user is already in your list of names:

i. Print the animal's data:

-For example, assuming the user entered 'Cat'

Cat: body = 3.3, brain = 25.6

ii. Ask the user if he would like to delete the animal. (You can assume
the user will answer either 'y' or 'n'.)

-For example, assuming the user previously entered "Cat":
Delete "Cat"? (y|n)

- If the user enters 'n', do nothing (i.e. you'll go back to asking the user
to enter an animal name)

- If the user enters 'y' delete the mammal's data from your lists.

● If the user entered 'q' you should:
- use the function you wrote for part 2 above to write the data out to
a new file called "BrainBodyWeightPounds.csv" and your
program will end. If at any point you accidentally open this file with
Excel, make sure you close it, because Excel will put a lock on it
and you will not be able to write to it again until you close it.

5.) Verify that your documentation makes sense and that you've added documentation
to each of your functions.

6.) Verify that your program works

7.) Upload your file to the Hw8 Assignments folder on D2L
'''





'''
1.2) RUNNING EXAMPLE

Below is an example of what you might see in a terminal when running this program
(output is in green, user input is in turquoise):

Enter animal name (or "q" to quit): Bugbear

File does not contain "Bugbear".

Add "Bugbear" to file? (y|n) y

Enter body weight for "Bugbear" in kilograms: 1000

Enter brain weight for "Bugbear" in grams:1

Enter animal name (or "q" to quit): Goat
Goat: body = 27.66, brain = 115.0

Delete "Goat"? (y|n) n

Enter animal name (or "q" to quit): Chickenshrimp
File does not contain "Chickenshrimp".

Add "Chickenshrimp" to file? (y|n) n
Enter animal name (or "q" to quit): Bugbear

Bugbear: body = 1000.0 
brain = 1.0

Delete "Bugbear"? (y|n) y
Enter animal name (or "q" to quit): q
'''