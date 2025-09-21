'''
Author: Dan Charbonneau
Date: Feb 4 2022
Class: ISTA 130
Section Leader: NA

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment

# put all of your function definitions below this line and then delete this comment
def mileage(num_trips):
    total_mileage = 0
    for i in range (1, num_trips + 1):
        current_trip_mileage = input('Enter mileage for trip ' + str(i) + ':')
        total_mileage = total_mileage + float(current_trip_mileage)
    print('Total mileage = ' + str(total_mileage))
    return None
#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    mileage(4)
    

if __name__ == '__main__':
    main()
