'''
Author: Dan
Date: Today
Class: ISTA 130
Section Leader: Alf

Description:

'''


###################################
# Function Definitions






###################################
# Main
def main():
    # Create a list that has the values "Arizona", "California", and
    # "New Mexico" in it. 
    my_list = ["Arizona", "California", "New Mexico"]

    # Add the value "Utah" to the end of the list. 
    my_list.append('Utah')

    # Add the value "Oregon" at the beginning of the list. 
    my_list.insert(0, 'Oregon')

    # Use a for loop to change all of the values in the list to uppercase. 
    for i in range(len(my_list)):
        my_list[i] = my_list[i].upper()

    # Use a while loop to change them all to lowercase. 
    i = 0
    while i < len(my_list):
        my_list[i] = my_list[i].lower()
        i += 1

    # Eliminate the first element in the list. 
    my_list.pop(0) 

    # Eliminate the last. 
    removed_value = my_list.pop(-1) 
    
  
if __name__ == "__main__":
    main()
    