'''
Name: Ricky Berliant
Date: 11/5/2025
Section Leader: Sungjoon Shin (SL)
Homework: ISTA 130 HW6

Module: Strings and File I/O

Summary: Learning how to test out the files by opening and modifying them.
Also, to feel more comfortable using string indexing, slicing, and methods.
Combining everything I mentioned will help understand how the functions work
and when to use them in practice.
'''


def US_to_EU(date_string):
    phone_num = date_string.split('/')
    phone_num = [phone_num[1], phone_num[0], phone_num[2]]
    separator = "."
    my_string = separator.join(phone_num)

    return my_string

def is_phone_num(date_string):   
     
    digit = date_string.split('-')
    
    if len(digit) != 3:
        return False
    
    if (len(digit[0]) == 3 and digit[0].isdigit()) and \
       (len(digit[1]) == 3 and digit[1].isdigit()) and \
       (len(digit[2]) == 4 and digit[2].isdigit()):
        return True
    else:
        return False
    

def redact_line(line):
    for i in range(len(line) - 12):
        if ((
            i == 0 or line[i - 1] == " ") \
            and line[i + 12] in " \n" \
            and is_phone_num(line[i:i + 12])):
            
            line = line[:i] + line[i:].replace(line[i:i + 12], 'XXX-XXX-XXXX', 1)
    return line


def redact_file(fileName):
    original_fileName = open(fileName, 'r')
    output_fileName = fileName[:-4] + '_redacted' + fileName[-4:] 
    redactedFile = open(output_fileName, 'w')
    
    for line in original_fileName:
        redactedLine = redact_line(line)
        redactedFile.write(redactedLine)

    original_fileName.close()
    redactedFile.close()


def plagiarism(file_1, file_2):
    
    fileName_1 = open(file_1)    
    
    for line_1 in fileName_1:
        fileName_2 = open(file_2)
        for line_2 in fileName_2:
            if line_2 == line_1:
                return True
        fileName_2.close()        
    else:
        fileName_1.close()
        return False
    

# count word function
def count_word(fileName, keyword):
    fileOpen = open(fileName, 'r')
    count = 0
    
    for line in fileOpen:
        count += line.count(keyword)
        
    fileOpen.close()
    return count