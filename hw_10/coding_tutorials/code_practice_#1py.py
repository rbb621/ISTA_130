
# It opens the file, reads it and writes a new file with the same name but the string '_ln' added to the filename stem. 
# For example, if the filename is 'text_file.txt' , the stem is 'textfile' and new
# file for writing should be called 'textfile_ln.txt'
# Assume the filename has an extension and only one dot.
# The new file should contain the same text as the original but each line should 
# start with its line number followed by a colon and a space.
# For example, if the tenth line in the original file is 'I heart Rocket.', 
# the tenth line in the new file should be '10: I heart Rocket.'


def line_nums(fileName):
    
    '''
    
    It opens the file, reads it and writes a new file with the same name but the string '_ln' 
    added to the filename stem. 
    
    For example, if the filename is 'text_file.txt' , the stem is 'textfile' and new
    file for writing should be called 'textfile_ln.txt'
    
    Assume the filename has an extension and only one dot.
    
    The new file should contain the same text as the original but each line should 
    start with its line number followed by a colon and a space.
    For example, if the tenth line in the original file is 'I heart Rocket.', 
    the tenth line in the new file should be '10: I heart Rocket.'
    '''
    new_filename = fileName + "_ln"
    open(fileName, 'r')
    
    for 
    



def main():
    print(line_nums('text_file.txt'))