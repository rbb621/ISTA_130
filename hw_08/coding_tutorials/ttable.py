'''
Author: <your name>
Date: <the date>
Class: ISTA 130
Section Leader: <your section leader>

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment
def ttable(table_dimensions):
    '''
    This function will print a times table of any dimension. 
    Parameters:
    Single int parameter providing the dimensions of the table
    Return:
    None
    '''
    block_width = 5
    header = " " * block_width + "|"
    for i in range(table_dimensions):
        header += str(i+1).rjust(5)
    print(header)
    print(("-" * 5) + "|" + "-" * (table_dimensions*5))
    
    for i in range(table_dimensions):
        new_line_start = str(i+1).rjust(5) + "|" 
        for j in range(table_dimensions): 
            new_line_start += str((i+1) * (j+1)).rjust(5)
        print(new_line_start)



# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    ttable(5)

if __name__ == '__main__':
    main()
