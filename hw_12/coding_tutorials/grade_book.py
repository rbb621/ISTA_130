'''
Name: Ricky Berliant
Date: 11/20/2025
Section Leader: Sungjoon
Week 13: Immutable and Mutable
File: RICKY_BERLIANT_MutableDiscussion.py
'''

# put all of your function definitions below this line and then delete this comment

#PSEUDOCODE

# Step 1: Create a function load grade book with a file name parameter
# Step 2: Create an empty grade dictionary
# Step 3: Open the file grades.txt from the main function and read it line by line
# Step 4: Remove any blank spaces with a strip method
# Step 5: Separate the indexes by commas
# Step 6: Turn the first index by the current index when it first reads the line
# Step 7: Splice the fist index and have the function focus on the grades
# Step 8: Create a list to store float numbers
# Step 9: Convert the grades to float numbers
# Step 10: Check to see if the id is in the grades dictionary
# Step 11: If so, then add the converted grades as floats
# Step 12: If not, then add the regular grade (???)
# Step 13: Return the dictionary


# Load Grade Book Function
# filename parameter from the grades.txt file inside the main() function
def load_grade_book(filename):
    
    # empty dictionary of the grades
    grades_dict = {}
    
    # open the file grades.txt and reads it line by line
    for line in open(filename):
        
        #removes any blank space from strip() and 
        #instead uses the split(',') to sparate the groups in comma
        current_line = line.strip().split(',')
        
        #Targets the first index from the current line 
        current_student_id = current_line[0]
        
        # Removes the first index and will print out the grades
        current_grades = current_line[1:]
        
        #Creates a list to store the float numbers
        current_grades_as_float = []

        #For every grade line will be converted to a float number
        for grade in current_grades:
            current_grades_as_float.append(float(grade))
            
        # Checks to see if the id is in the grades dictionary
        if current_student_id in grades_dict:
            grades_dict[current_student_id].extend(current_grades_as_float)
        else:
            # Prints out a new element
            grades_dict[current_student_id] = current_grades_as_float
    return grades_dict


#PSEUDOCODE

# Step 1: Create a function update grade book 
# Step 2: For the parameters, include a file name parameter, along with a grades dictionary
# Step 3: Open the file grades.txt from the main function and read it line by line
# Step 4: Remove any blank spaces with a strip method
# Step 5: Separate the indexes by commas
# Step 6: Turn the first index by the current index when it first reads the line
# Step 7: Splice the fist index and have the function focus on the grades
# Step 8: Create a list to store float numbers
# Step 9: Convert the grades to float numbers
# Step 10: Check to see if the id is in the grades dictionary
# Step 11: If so, then add the converted grades as floats
# Step 12: If not, then add the new grade
# Step 13: Return the dictionary

def update_grade_book(filename, grades_dict):
    for line in open(filename):
        current_line = line.strip().split(',')
        current_student_id = current_line[0]
        current_grades = current_line[1:]
        current_grades_as_float = []
        for grade in current_grades:
            current_grades_as_float.append(float(grade))
        if current_student_id in grades_dict:
            grades_dict[current_student_id].extend(current_grades_as_float)
        else:
            grades_dict[current_student_id] = current_grades_as_float
    return grades_dict 


#PSEUDOCODE

#1: Createa mean grades function to find the average
#2: Create an empty means dictionary
#3: Have it read the file line and line and print out the average
#4: Sum up all the numbers and then divide the total by the amount of numbers
#5: Return the means dictionary

# Mean Grade Function
def mean_grades(grades_dict):
    
    #Empty Dictionary
    means = {}
    
    # reads the file line by line and then prints out the average
    for student_id in grades_dict:
        means[student_id] = sum(grades_dict[student_id]) / len(grades_dict[student_id])
    return means


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    
    # Loads the content from the text file grades
    load_grade_book('grades.txt')
    test_dict = {'140907':[77,98],'156328':[60,55]}
    
    # Updates the content from the text file grades
    update_grade_book('grades.txt',test_dict)
    
    #Prints out the average grade from the mean_grades function
    print(mean_grades(test_dict))


if __name__ == '__main__':
    main()
