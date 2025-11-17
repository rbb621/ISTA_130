'''
Author: Duane Bryant
Date: Nov 17 2025
Class: ISTA 130
Section Leader: Sungjoon

Description:
Function called load_grade_book. It takes one string argument, a filename. 
The file is in CSV format (comma separated values). Data in CSV files is separated by commas.  
The first value is a student id, which is followed by a series of grades. Build and return a dictionary 
from the file that maps student id's (strings) to a list of grades (floats). The same student may 
have more than one line in the file. For example, if the file's content is
'''


# Function 1: load_grade_book

def load_grade_book(filename):
    '''
  The file is in CSV format (comma separated values). Data in CSV files is separated by commas.  
  The first value is a student id, which is followed by a series of grades.
    '''


    grade_book_dict = {}

    with open(filename, 'r') as input_file: # open the file
        for line in input_file:
            cleaned_line = line.strip() # loop through each line in the file
            values_list = cleaned_line.split(',')  # strip the line and split by commas

            student_id = values_list[0] # student id
            grade_values = [float(num) for num in values_list[1:]] #convert to float

            if student_id not in grade_book_dict: # student not found, it adds a new one
                grade_book_dict[student_id] = grade_values
            else:
                grade_book_dict[student_id].extend(grade_values) # if found add new grades

    return grade_book_dict



# Function 2: add_to_grade_book

def add_to_grade_book(filename, grade_book_dict):
    '''
    In addition to the filename, it takes a grade book dictionary. Instead of creating 
    a grade book dictionary from scratch, this version adds the information in the file 
    to the existing dictionary
    '''

    with open(filename, 'r') as input_file: #open files
        for line in input_file:
            cleaned_line = line.strip() #loops each line
            values_list = cleaned_line.split(',') 

            student_id = values_list[0] #
            grade_values = [float(num) for num in values_list[1:]]

            if student_id not in grade_book_dict: #creates new student if not found
                grade_book_dict[student_id] = grade_values
            else:
                grade_book_dict[student_id].extend(grade_values) # if found, adds grades

    return None #NADA due to it already adding and updating grades....