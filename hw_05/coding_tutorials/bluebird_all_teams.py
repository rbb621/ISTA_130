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
def bluebird_count(num_observers):
    total_birds = 0
    for i in range(num_observers):
        print('---- Observer ', str(i + 1) , ' ----')
        current_birds_observed = input('Enter number spotted by this observer: ')
        print()
        total_birds += int(current_birds_observed)
    return total_birds

def bluebirds_all_teams():
    num_teams = input('Enter number of teams: ')
    total_regional_birds = 0
    for i in range(int(num_teams)):
        current_num_observers = input('Enter number of observers in your team: ')
        total_birds_for_team = bluebird_count(int(current_num_observers))
        total_regional_birds += total_birds_for_team
    return total_regional_birds
#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    birds_observed_in_region = bluebirds_all_teams()
    print(birds_observed_in_region)

if __name__ == '__main__':
    main()
