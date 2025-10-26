'''
Name: Ricky Berliant
Class: ISTA 130
Section Leader: Sungjoon Shin (SL)
Date: 11/29/2025
Assignment: Week 10 Extra Credit
'''


'''
#1
Write a function called time_to_seconds has one string parameter representing a time in
format "hours:minutes:seconds" (e.g. "10:3:7"), and returns the equivalent number of
seconds. There is more than one way to do this, but the find method may be helpful.
'''


def time_to_seconds(time_string):
    part = time_string.split(':')
    hours = int(part[0])
    minute = int(part[1])
    second = int(part[2])
    
    total_seconds = (hours * 3600) + (minute + 60) + second
    return total_seconds


'''
#2
Write a function called swap_case that takes a string and returns a new string with
all lowercase characters converted to upper and all upper to lower.
'''

def swap_case(string):

    new_str = ""
    for ch in string:
        if ch.islower():
            new_str += ch.upper()
        elif ch.isupper():
            new_str += ch.lower()
        else:
            new_str += ch
    return new_str
   

    
'''
#3
Write a function called line_nums that takes a filename (string) argument. 

It opens the file, reads it and writes a new file with the same 
name but the string '_ln' added to the filename stem. 

For example, if the filename is 'textfile.txt', 

the stem is 'textfile' and new file for writing should be called
'textfile_ln.txt'. 

Assume the filename has an extension and only one dot. 

The new file should contain the same text as the original 
but each line should start with its line number followed by a colon 
and a space. 

For example, if the tenth
line in the original file is 'I heart Rocket.', 
the tenth line in the new file should be
'10: I heart Rocket.'
'''

def line_nums(fileName):
    parts = fileName.split('.')
    stem = parts[0]
    ext = parts[1]
    new_filename = stem + '_ln' + ext

    inFile = open(fileName, 'r')
    outFile = open(new_filename, 'w')
    
    line_number = 1


    for line in inFile:
        outFile.write(str(line_number) + ':' + line)
        line_number += 1
        
    inFile.close()
    outFile.close()

        
'''
#4
Write a function called word_search that takes two string arguments, a filename and a word.
The function prints "***** <word> *****" and then every line that contains the word with its
line number added as above. (Hint: there are methods called isupper, islower, upper, and
lower).
'''

def word_search(filename, word):

    # Step 1 + 2: print header
    print("***** " + word + " *****")

    # Step 3: open file
    file = open(filename, "r")

    # Step 4: line counter
    line_number = 1

    # Step 5: print any line that contains the word
    for line in file:
        if word.lower() in line.lower():
            print(str(line_number) + ": " + line.strip())
        line_number += 1

    # Step 6: close file
    file.close()


'''
Write code that does the following. Create a list that has the values "Arizona",
"California", and "New Mexico" in it. Add the value "Utah" to the end of the
list. Add the value "Oregon" at the beginning of the list. Use a for loop to change all of
the values in the list to uppercase. Use a while loop to change them all to lowercase.
Eliminate the first element in the list. Eliminate the last. (Hint: append, insert, pop).
'''

# Step 1: create list
states = ["Arizona", "California", "New Mexico"]

# Step 2: append Utah as last element
states.append("Utah")

# Step 3: insert Oregon at beginning as first element
states.insert(0, "Oregon")

# Step 4: convert all values to uppercase
for i in range(len(states)):
    states[i] = states[i].upper()

# Step 5: convert all values to lowercase using while loop
i = 0
while i < len(states):
    states[i] = states[i].lower()
    i += 1

# Step 6: remove first element
states.pop(0)

# Step 7: remove last element
states.pop()

# Print results
print("Final list of states:", states)


'''
#5
Write a function called add_elements. It takes two list arguments and returns a new list.
Each element in the new list is the sum of the elements at the same position in the arguments.
You may assume the lists are the same length. For example:
add_elements([1, 2, 1, 3], [7, 14, 6, 33]) --> [8, 16, 7, 36].

'''

def add_elements(list1, list2):
    updated_list = []
    
    for i in range(len(list1)):
        updated_list.append(list1[i] + list2[i]) 

    return updated_list
    



'''
#6
Write a function called join that takes a list of strings and a string separator and returns a
string consisting of the strings in the list separated by the separator. Example calls:
join(['I', 'heart', 'Rocket!'], ' ') --> 'I heart Rocket!'
join(['I', 'heart', 'Rocket!'], '--') --> 'I--heart--Rocket!'
'''

def join(string, separator):
    new_str = ""
    
    for i in range(len(string)):
        new_str += string[i]
        if i < len(string) - 1 :
            new_str += separator
    return new_str
        



def main():
    #1: time to seconds
    print(time_to_seconds('10:3:7'))
    
    #2: swap case
    print(swap_case('THE flintstones'))
    
    #3: line nums
    print(line_nums('textfile.txt'))
    
    #4: word search
    print(word_search('wordsearch_states.txt', 'Ricky Berliant'))
    
    #5: add elements
    print(add_elements([1, 2, 1, 3], [7, 14, 6, 33]))
    
    #6: join
    print(join(['I', 'heart', 'Rocket!'], ' '))
    print(join(['I', 'heart', 'Rocket!'], '--'))



if __name__ == '__main__':
    main()