'''
Name: Ricky Berliant
Date: 11/5/2025
Section Leader: Sungjoon Shin (SL)
Homework: Extra Credit Lists and Strings
Class: ISTA 130
'''


# Convert Time to Sections
def time_to_seconds(string):
    time = string
    timer = time.split(':')
    hours = int(timer[0])
    minutes = int(timer[1])
    seconds = int(timer[2])
    
    total_time = (hours * 3600) + (minutes * 60) + seconds
    return total_time


# Function: Display Full Name
def full_name(last_first):
    
    name = last_first.split(',')
    first_name = name[1].strip().capitalize() 
    last_name = name[0].strip().capitalize()
    first_last = first_name + ' ' + last_name
    
    return first_last


# Count the Number of Characters In a Word 
def word_lengths(string):
    word = []                
    words = string.split()
    
    for ch in words:
        word.append(len(ch))
    return word


# For every third element
def third(my_list):
    
    for i in range(len(my_list)):
        if i % 3 == 2:
            my_list[i] = 3
    print(my_list)


# Separator to display '---' between the words
def separator(string, delimiter):
    words = string.split()
    word_list = delimiter.join(words)
    
    return word_list
    

# Phone Numbers
def phone_nums(fileName):
    openFile = open(fileName, 'r')
    phone_list = []

    for line in openFile:
        words = line.split()
        for word in words:
            parts = word.split('-')
            if len(parts) == 3:
                is_valid = True
                for i in parts:
                    if not i.isdigit():
                        is_valid = False
                        break
                if is_valid:
                    phone_list.append(word)

    openFile.close()
    return phone_list


    
# R Words
def r_words(fileName):
    file = open(fileName, 'r')
    r_word_list = []
    
    for line in file:
        words = r_word_list
        for word in words:
            if word.startswith('r') or word.startswith('R'):
                r_word_list.append(word)
                
    file.close()
    return r_word_list    


def main():
    print(time_to_seconds('10:3:7'))
    print(full_name('fudd, elmer'))
    print(full_name('duck, donald'))
    print(word_lengths('I heart Rocket.'))
    print(third(['you', 77, True, 0.5, 'me', 'hmm']))
    print(separator('I heart Rocket', '---'))
    print(phone_nums('phone_numbers.txt'))
    
    # R Words
    file = input('Enter a file: ')
    print(r_words(file))

if __name__ == '__main__':
    main()