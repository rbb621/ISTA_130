'''
Name: Ricky Berliant
Date: 11/13/2025
Section Leader: Sungjoon Shin (SL)
Homework: ISTA 130 HW7

Module: String Manipulation, File Reading & Writing

Summary: This program creates and modifies a Mad Libs text file by replacing 
specific keywords such as PLURAL NOUN, NOUN, ADJECTIVE, VERB, and VERB PAST. 
It also analyzes the files content to count vowels, consonants, whitespace, 
and punctuation. Once finished, it prints a summary report.
'''

# Print Report Function
def print_report(fileName):
    open_fileName = open(fileName, 'r')
    
    # Initializing values
    count_vowels = 0
    count_consonants = 0
    count_whitespace = 0
    count_punctuation = 0
    total_char = 0
    
    # Creating sets
    vowel_set = 'aeiouAEIOU'
    consonant_set = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    # Setting File Name in the center of the report
    title = fileName
    header_line = title.center(25, '-')

    # Counting the instances
    for line in open_fileName:
        for ch in line:
            total_char += 1
            if ch in vowel_set:
                count_vowels += 1
            elif ch in consonant_set:
                count_consonants += 1
            elif ch.isspace():
                count_whitespace += 1
            else:
                count_punctuation += 1
                
    # Calculating Percentages
    percent_vowels = round((count_vowels / total_char) * 100, 1)
    percent_consonants = round((count_consonants / total_char) * 100, 1)
    percent_whitespace = round((count_whitespace / total_char) * 100, 1)
    percent_punctuation = round((count_punctuation / total_char) * 100, 1)
    
    # Output
    print()
    print(header_line)
    print('Vowels:'.ljust(20) + str(count_vowels).rjust(5))
    print('Consonants:'.ljust(20) + str(count_consonants).rjust(5))
    print('Whitespace:'.ljust(20)+ str(count_whitespace).rjust(5))
    print('Punctuation:'.ljust(20)+ str(count_punctuation).rjust(5))
    print('-------------------------')
    print('Total:'.ljust(20)+ str(total_char).rjust(5))
    print('Percent vowels:'.ljust(20) + str(percent_vowels).rjust(5))
    print('Percent consonants:'.ljust(20)+ str(percent_consonants).rjust(5))
    print('Percent spaces:'.ljust(20)+ str(percent_whitespace).rjust(5))
    print('Percent punctuation:'.ljust(20)+ str(percent_punctuation).rjust(5))
    print('=========================')
    print()
    open_fileName.close()
            

# Replacing Parts of Speech Function
def replace_parts_of_speech(line, part_of_speech):

    # Every line
    count = line.count(part_of_speech)
    
    # For each prompt, it will ask the user to enter a word
    for i in range(count):
        prompt = part_of_speech.lower()
        word_entry = input("Enter " + prompt + ': ')
        line = line.replace(part_of_speech, word_entry, 1)
    return line

# Creates a Mad Lib Function
def complete_mad_lib(fileName):
    file_reader = open(fileName, 'r')
    
    # Creates a new Mad Lib Function that begins with "MAD_"
    new_file_name = "MAD_" + fileName
    
    file_writer = open(new_file_name, 'w')
    
    # Replaces parts of the speech words with a new word entered
    for line in file_reader:
        line = replace_parts_of_speech(line, "PLURAL NOUN")
        line = replace_parts_of_speech(line, "VERB PAST")
        line = replace_parts_of_speech(line, "VERB")
        line = replace_parts_of_speech(line, "NOUN")
        line = replace_parts_of_speech(line, "ADJECTIVE")
        file_writer.write(line)
    
    # Once the program is finished
    file_reader.close()
    file_writer.close()

# Main Function
def main():

    file_name = input('Enter file name: ')
    
    # Print Report
    print_report(file_name)
    
    # Complete Mad Lib
    complete_mad_lib(file_name)    

if __name__ == '__main__':
    main()