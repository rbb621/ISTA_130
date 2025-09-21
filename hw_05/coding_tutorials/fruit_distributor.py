'''
Author: Dan Charbonneau
Date: Feb 4 2022
Class: ISTA 130
Section Leader: Wilbur the potbelly pig

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment


# put all of your function definitions below this line and then delete this comment
def fruit_distributor(num_fruit_received, num_people):
    num_fruit_per_person = num_fruit_received // num_people
    num_fruit_for_wilbur = num_fruit_received % num_people
    print('You have received ' + str(num_fruit_received) + ' fruit which will be divided among ' + str(num_people) + ' people and Wilbur')
    print('Each person will receive ' + str(num_fruit_per_person) + ' fruit')
    print('Wilbur will receive ' + str(num_fruit_for_wilbur) + ' fruit')
    return None


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    fruit_distributor(7,2)
    

if __name__ == '__main__':
    main()
