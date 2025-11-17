mutable_object = ['Hudson', 'Camden', 'Sydney']

mutable_object[2] = 'Parker'

print('Mutable Object:', mutable_object)

#----------------------------------------------------
            # IMMUTATBLE OBJECTS
#----------------------------------------------------
# immutable_obj = ('Hudson', 'Camden', 'Sydney')
# immutable_obj[1] = 'Parker'

# print(immutable_obj)

#DOES NOT SUPPORT TUPLES ()


# Mutable:
[1, 2, 3] # Lists
{1, 2, 3} # Dictionaries

# Immutable:
"123" # Strings
'123' # Strings
(1, 2, 3) # Tuples

def change_param(some_person):
    print(some_person)
    some_person = "blue ball"
    print (some_person)
    return None

def main():
    person_a = "green ball"
    print (person_a)
    person_a = "red ball"
    print(person_a)
    change_param(person_a)
    print (person_a)
    
if __name__ == '__main__':
    main()