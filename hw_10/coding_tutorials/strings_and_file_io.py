'''
Author: Dan
Date: Today
Class: ISTA 130
Section Leader: Alf

Description:

'''


###################################
# Function Definitions


def line_nums(filename):
    '''
    It opens the file, reads it and writes a new file with the same
    name but the string '_ln' added to the filename stem.
    The new file should contain the same text as the original but each
    line should start with its line number followed by a colon and a space.
    '''
    oringal_file = open(filename, 'r')
    new_filename = filename[:-4] + '_ln' + filename[len(filename)-4:] 
    ln_file = open(new_filename, 'w')
    line_num = 1
    for line in oringal_file:
        new_line = str(line_num) + ': ' + line
        ln_file.write(new_line)
        line_num = line_num + 1
    oringal_file.close()
    ln_file.close()



###################################
# Main
def main():
   line_nums('iwalktheline.txt')
    
  
if __name__ == "__main__":
    main()
    